-- =========================================================
-- PL/pgSQL Functions & Procedures for EasyKost
-- 1) sm_user_pr_register_user
-- 2) sm_user_fn_authenticate_user
-- 3) sm_user_pr_record_login_activity
-- 4) sm_user_pr_generate_user_otp
-- 5) sm_user_pr_verify_user_otp
-- 6) sm_owner_pr_request_property_verification
-- 7) sm_adm_pr_review_property_verification
-- 8) sm_adm_pr_ban_user_account
-- 9) sm_adm_pr_unban_user_account
-- =========================================================


-- =========================================================
-- 1. sm_user_pr_register_user
--    Registrasi user + generate OTP awal
-- =========================================================
CREATE OR REPLACE PROCEDURE sm_user_pr_register_user(
    IN  p_full_name      VARCHAR,
    IN  p_email          VARCHAR,
    IN  p_phone_number   VARCHAR,
    IN  p_password       VARCHAR,
    IN  p_role           user_role,
    IN  p_gender         CHAR(1),
    IN  p_birth_date     DATE DEFAULT NULL,
    OUT p_user_id        INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_otp_code VARCHAR(6);
BEGIN
    -- Cek duplikasi email
    IF EXISTS (
        SELECT 1
        FROM USERS
        WHERE email = p_email
    ) THEN
        RAISE EXCEPTION 'Email % sudah terdaftar', p_email;
    END IF;

    -- Cek duplikasi nomor telepon
    IF EXISTS (
        SELECT 1
        FROM USERS
        WHERE phone_number = p_phone_number
    ) THEN
        RAISE EXCEPTION 'Nomor telepon % sudah terdaftar', p_phone_number;
    END IF;

    -- Insert user baru dengan status akun pending
    INSERT INTO USERS (
        full_name,
        email,
        phone_number,
        password,
        role,
        account_status,
        birth_date,
        gender
    )
    VALUES (
        p_full_name,
        p_email,
        p_phone_number,
        p_password,   -- catatan: idealnya sudah di-hash
        p_role,
        'pending',
        p_birth_date,
        p_gender
    )
    RETURNING user_id INTO p_user_id;

    -- Generate kode OTP 6 digit (000000–999999)
    v_otp_code := lpad(
        (floor(random() * 1000000))::INT::TEXT,
        6,
        '0'
    );

    -- Simpan OTP ke tabel VERIFICATION
    INSERT INTO VERIFICATION (
        user_id,
        otp_code,
        otp_expire,
        otp_status
    )
    VALUES (
        p_user_id,
        v_otp_code,
        now() + INTERVAL '15 minutes',
        'active'
    );

    RAISE NOTICE 'User % berhasil diregistrasi, OTP: %', p_user_id, v_otp_code;
END;
$$;

-- =========================================================
-- 1. UJI COBA sm_user_pr_register_user
--    Registrasi user baru + OTP awal
-- =========================================================

-- Contoh: registrasi user customer baru
CALL sm_user_pr_register_user(
    'Devi Maulani',         -- p_full_name
    'devi@example.com',     -- p_email
    '081234567890',         -- p_phone_number
    'devi1234',             -- p_password (demo)
    'customer',             -- p_role (enum user_role)
    'F',                    -- p_gender
    '2004-05-10'            -- p_birth_date
    -- OUT p_user_id akan muncul di hasil pemanggilan
);

-- Cek hasil registrasi user (ganti ID dengan hasil OUT p_user_id)
-- SELECT * FROM USERS WHERE user_id = <hasil_p_user_id>;

-- =========================================================
-- 2. sm_user_fn_authenticate_user
--    Validasi login (email + password, status != banned)
-- =========================================================
CREATE OR REPLACE FUNCTION sm_user_fn_authenticate_user(
    p_email    VARCHAR,
    p_password VARCHAR
)
RETURNS TABLE(
    user_id INT,
    role user_role,
    account_status account_status
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        u.user_id,
        u.role,
        u.account_status
    FROM USERS u
    WHERE 
        u.email = p_email
        AND u.password = p_password   -- catatan: demo (real: hashing)
        AND u.account_status <> 'banned';

    IF NOT FOUND THEN
        RETURN;
    END IF;
END;
$$;

-- =========================================================
-- 2. UJI COBA sm_user_fn_authenticate_user
--    Login menggunakan email + password
-- =========================================================

-- Contoh: login dengan user yang baru diregistrasi di atas
SELECT *
FROM sm_user_fn_authenticate_user(
    'devi@example.com',   -- p_email
    'devi1234'            -- p_password
);

-- Coba login dengan password salah
SELECT *
FROM sm_user_fn_authenticate_user(
    'devi@example.com',
    'salahpassword'
);

-- =========================================================
-- 3. sm_user_pr_record_login_activity
--    Update LAST_LOGIN dan log aktivitas login (opsional)
-- =========================================================
CREATE OR REPLACE PROCEDURE sm_user_pr_record_login_activity(
    p_user_id     INT,
    p_ip_address  VARCHAR DEFAULT NULL,
    p_device      VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Cek user ada atau tidak
    IF NOT EXISTS (SELECT 1 FROM USERS WHERE user_id = p_user_id) THEN
        RAISE EXCEPTION 'User dengan ID % tidak ditemukan', p_user_id;
    END IF;

    -- Update LAST_LOGIN
    UPDATE USERS
    SET last_login = now()
    WHERE user_id = p_user_id;

    -- Insert ke log jika tabel tersedia
    IF EXISTS (
        SELECT 1 FROM information_schema.tables
        WHERE table_name = 'user_login_log'
    ) THEN
        INSERT INTO user_login_log(
            user_id,
            login_time,
            ip_address,
            device
        )
        VALUES(
            p_user_id,
            now(),
            p_ip_address,
            p_device
        );
    END IF;

    RAISE NOTICE 'Aktivitas login user % berhasil dicatat.', p_user_id;
END;
$$;

-- =========================================================
-- 3. UJI COBA sm_user_pr_record_login_activity
--    Update LAST_LOGIN + log ke USER_LOGIN_LOG (jika ada)
-- =========================================================

-- Asumsi: user dengan ID 1 sudah ada
CALL sm_user_pr_record_login_activity(
    1,                    -- p_user_id
    '192.168.1.10',       -- p_ip_address
    'Android'             -- p_device
);

-- Cek kolom last_login di USERS
-- SELECT user_id, last_login FROM USERS WHERE user_id = 1;

-- Jika punya tabel user_login_log, cek isi log
-- SELECT * FROM user_login_log WHERE user_id = 1 ORDER BY login_time DESC;

-- =========================================================
-- 4. sm_user_pr_generate_user_otp
--    Generate / resend OTP untuk user tertentu
-- =========================================================
CREATE OR REPLACE PROCEDURE sm_user_pr_generate_user_otp(
    p_user_id    INT,
    OUT p_otp_code VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Generate kode OTP 6 digit (000000–999999)
    p_otp_code := lpad(
        (floor(random() * 1000000))::INT::TEXT,
        6,
        '0'
    );

    -- Cek apakah sudah ada OTP aktif untuk user ini
    IF EXISTS (
        SELECT 1
        FROM VERIFICATION
        WHERE user_id = p_user_id
          AND otp_status = 'active'
    ) THEN
        -- Update OTP aktif yang sudah ada
        UPDATE VERIFICATION
        SET
            otp_code   = p_otp_code,
            otp_expire = now() + INTERVAL '15 minutes',
            otp_status = 'active'
        WHERE user_id = p_user_id
          AND otp_status = 'active';
    ELSE
        -- Insert OTP baru jika belum ada
        INSERT INTO VERIFICATION (
            user_id,
            otp_code,
            otp_expire,
            otp_status
        )
        VALUES (
            p_user_id,
            p_otp_code,
            now() + INTERVAL '15 minutes',
            'active'
        );
    END IF;

    RAISE NOTICE 'OTP baru untuk user % adalah %', p_user_id, p_otp_code;
END;
$$;


-- =========================================================
-- 4. UJI COBA sm_user_pr_generate_user_otp
--    Resend / generate OTP baru untuk user
-- =========================================================

-- Asumsi: user dengan ID 1 sudah ada
CALL sm_user_pr_generate_user_otp(
    1   -- p_user_id
    -- OUT p_otp_code akan tampil di hasil pemanggilan
);

-- Lihat OTP yang tersimpan di tabel VERIFICATION
-- SELECT * FROM VERIFICATION WHERE user_id = 1 ORDER BY otp_expire DESC;

-- =========================================================
-- 5. sm_user_pr_verify_user_otp
--    Verifikasi OTP dan aktivasi akun
-- =========================================================
CREATE OR REPLACE PROCEDURE sm_user_pr_verify_user_otp(
    p_user_id    INT,
    p_otp_code   VARCHAR,
    OUT p_is_valid BOOLEAN
)
LANGUAGE plpgsql
AS $$
BEGIN
    p_is_valid := FALSE;

    -- Cek user ada atau tidak
    IF NOT EXISTS (
        SELECT 1 FROM USERS WHERE user_id = p_user_id
    ) THEN
        RAISE EXCEPTION 'User dengan ID % tidak ditemukan', p_user_id;
    END IF;

    -- Cek OTP yang cocok, active, dan belum kedaluwarsa
    IF NOT EXISTS (
        SELECT 1
        FROM VERIFICATION
        WHERE user_id    = p_user_id
          AND otp_code   = p_otp_code
          AND otp_status = 'active'
          AND otp_expire >= now()
    ) THEN
        RAISE NOTICE 'OTP tidak valid atau sudah kedaluwarsa untuk user %', p_user_id;
        RETURN;
    END IF;

    -- Update status OTP menjadi used
    UPDATE VERIFICATION
    SET otp_status = 'used'
    WHERE user_id    = p_user_id
      AND otp_code   = p_otp_code
      AND otp_status = 'active'
      AND otp_expire >= now();

    -- Update status akun user menjadi active
    UPDATE USERS
    SET account_status = 'active'
    WHERE user_id = p_user_id;

    p_is_valid := TRUE;
    RAISE NOTICE 'Verifikasi OTP berhasil, akun user % diaktifkan', p_user_id;
END;
$$;


-- =========================================================
-- 5. UJI COBA sm_user_pr_verify_user_otp
--    Verifikasi OTP dan aktivasi akun user
-- =========================================================

-- 5.1. Ambil OTP yang masih aktif untuk user 1
-- (jalankan SELECT ini, lalu copy nilai otp_code-nya)
-- SELECT otp_code
-- FROM VERIFICATION
-- WHERE user_id = 1 AND otp_status = 'active'
-- ORDER BY otp_expire DESC
-- LIMIT 1;

-- Misal hasilnya adalah '927614', panggil prosedur:
CALL sm_user_pr_verify_user_otp(
    1,          -- p_user_id
    '927614',   -- p_otp_code (ganti dengan nilai sebenarnya)
    NULL        -- OUT p_is_valid akan muncul di hasil pemanggilan
);

-- Cek status akun user
-- SELECT user_id, account_status FROM USERS WHERE user_id = 1;

-- =========================================================
-- 6. sm_owner_pr_request_property_verification
--    Owner mengajukan verifikasi kepemilikan kost
-- =========================================================
CREATE OR REPLACE PROCEDURE sm_owner_pr_request_property_verification(
    p_property_id     INT,
    p_nik             VARCHAR,
    p_document_image  VARCHAR,
    p_property_image  VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Cek property ada atau tidak
    IF NOT EXISTS (
        SELECT 1
        FROM PROPERTY
        WHERE property_id = p_property_id
    ) THEN
        RAISE EXCEPTION 'Property dengan ID % tidak ditemukan', p_property_id;
    END IF;

    -- Cek apakah property sudah pernah diajukan verifikasi
    IF EXISTS (
        SELECT 1
        FROM PROPERTYVERIFICATION
        WHERE property_id = p_property_id
    ) THEN
        RAISE EXCEPTION 'Property dengan ID % sudah memiliki permohonan verifikasi', p_property_id;
    END IF;

    -- Cek keunikan NIK
    IF EXISTS (
        SELECT 1
        FROM PROPERTYVERIFICATION
        WHERE nik = p_nik
    ) THEN
        RAISE EXCEPTION 'NIK % sudah digunakan untuk verifikasi property lain', p_nik;
    END IF;

    -- Insert permohonan verifikasi
    INSERT INTO PROPERTYVERIFICATION (
        property_id,
        nik,
        document_image,
        property_image
    )
    VALUES (
        p_property_id,
        p_nik,
        p_document_image,
        p_property_image
    );

    -- Update status verifikasi property menjadi pending
    UPDATE PROPERTY
    SET verification = 'pending'
    WHERE property_id = p_property_id;

    RAISE NOTICE 'Permohonan verifikasi untuk property % berhasil dibuat.', p_property_id;
END;
$$;

-- =========================================================
-- 6. UJI COBA sm_owner_pr_request_property_verification
--    Owner mengajukan verifikasi property
-- =========================================================

-- Asumsi: property dengan ID 101 milik owner sudah ada di tabel PROPERTY
CALL sm_owner_pr_request_property_verification(
    101,                         -- p_property_id
    '3201140904020007',          -- p_nik
    '/img/docs/ktp_101.jpg',     -- p_document_image
    '/img/property/kostA.jpg'    -- p_property_image
);

-- Cek permohonan verifikasi
-- SELECT * FROM PROPERTYVERIFICATION WHERE property_id = 101;

-- Cek status verifikasi property
-- SELECT property_id, verification FROM PROPERTY WHERE property_id = 101;

-- =========================================================
-- 7. sm_adm_pr_review_property_verification
--    Admin menyetujui / menolak verifikasi property
-- =========================================================
CREATE OR REPLACE PROCEDURE sm_adm_pr_review_property_verification(
    p_property_verification_id INT,
    p_admin_id                 INT,
    p_is_approved              BOOLEAN,
    p_notes                    TEXT DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_property_id INT;
    v_new_status  VARCHAR;
BEGIN
    -- Cek permohonan verifikasi ada atau tidak
    SELECT property_id
    INTO v_property_id
    FROM PROPERTYVERIFICATION
    WHERE property_verification_id = p_property_verification_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Permohonan verifikasi dengan ID % tidak ditemukan', 
            p_property_verification_id;
    END IF;

    -- Tentukan status baru
    IF p_is_approved THEN
        v_new_status := 'verified';
    ELSE
        v_new_status := 'rejected';
    END IF;

    -- Update status verifikasi di PROPERTY
    UPDATE PROPERTY
    SET verification = v_new_status
    WHERE property_id = v_property_id;

    -- Simpan info review jika kolomnya tersedia
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'propertyverification'
          AND column_name = 'review_admin_id'
    ) THEN
        UPDATE PROPERTYVERIFICATION
        SET
            review_admin_id = p_admin_id,
            review_notes    = p_notes,
            reviewed_at     = now()
        WHERE property_verification_id = p_property_verification_id;
    END IF;

    RAISE NOTICE 'Review verifikasi property % diset ke status % oleh admin %', 
        v_property_id, v_new_status, p_admin_id;
END;
$$;

-- =========================================================
-- 7. UJI COBA sm_adm_pr_review_property_verification
--    Admin menyetujui / menolak verifikasi property
-- =========================================================

-- Cari ID permohonan verifikasi untuk property 101
-- SELECT property_verification_id
-- FROM PROPERTYVERIFICATION
-- WHERE property_id = 101
-- ORDER BY property_verification_id DESC
-- LIMIT 1;

-- Misal hasilnya 10, admin 1 menyetujui verifikasi:
CALL sm_adm_pr_review_property_verification(
    10,                                      -- p_property_verification_id
    1,                                       -- p_admin_id
    TRUE,                                    -- p_is_approved (TRUE = approve)
    'Dokumen lengkap dan sesuai data KTP'    -- p_notes
);

-- Cek status verifikasi property
-- SELECT property_id, verification FROM PROPERTY WHERE property_id = 101;

-- Jika kolom review_admin_id dsb ada, cek:
-- SELECT * FROM PROPERTYVERIFICATION WHERE property_verification_id = 10;

-- =========================================================
-- 8. sm_adm_pr_ban_user_account
--    Admin membanned akun user
-- =========================================================
CREATE OR REPLACE PROCEDURE sm_adm_pr_ban_user_account(
    p_user_id  INT,
    p_admin_id INT,
    p_reason   TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_current_status account_status;
BEGIN
    -- Cek user ada atau tidak
    SELECT account_status
    INTO v_current_status
    FROM USERS
    WHERE user_id = p_user_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'User dengan ID % tidak ditemukan', p_user_id;
    END IF;

    -- Jika sudah banned, tidak perlu update lagi
    IF v_current_status = 'banned' THEN
        RAISE NOTICE 'User dengan ID % sudah berstatus banned', p_user_id;
        RETURN;
    END IF;

    -- Update status user menjadi banned
    UPDATE USERS
    SET account_status = 'banned'
    WHERE user_id = p_user_id;

    -- Insert ke USER_BAN_LOG jika tabel tersedia
    IF EXISTS (
        SELECT 1 
        FROM information_schema.tables
        WHERE table_name = 'user_ban_log'
    ) THEN
        INSERT INTO user_ban_log (
            user_id,
            admin_id,
            reason,
            banned_at
        )
        VALUES (
            p_user_id,
            p_admin_id,
            p_reason,
            now()
        );
    END IF;

    -- Opsional: set semua property user menjadi tidak aktif jika kolom is_active ada
    IF EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'property'
          AND column_name = 'is_active'
    ) THEN
        UPDATE PROPERTY
        SET is_active = FALSE
        WHERE user_id = p_user_id;
    END IF;

    RAISE NOTICE 'User % berhasil dibanned oleh admin %, alasan: %',
        p_user_id, p_admin_id, p_reason;
END;
$$;

-- =========================================================
-- 8. UJI COBA sm_adm_pr_ban_user_account
--    Admin membanned akun user
-- =========================================================

-- Asumsi: user dengan ID 2 ada dan belum banned
CALL sm_adm_pr_ban_user_account(
    2, 
    1, 
    'Melanggar aturan kost berulang kali'
);

-- Cek status user
-- SELECT user_id, account_status FROM USERS WHERE user_id = 2;

-- Jika tabel user_ban_log ada, cek log
-- SELECT * FROM user_ban_log WHERE user_id = 2 ORDER BY banned_at DESC;

-- Coba ban ulang user yang sama (untuk menguji NOTICE "sudah banned")
CALL sm_adm_pr_ban_user_account(
    2,
    1,
    'Percobaan ban kedua'
);

-- =========================================================
-- 9. sm_adm_pr_unban_user_account
--    Admin mengembalikan status akun dari banned ke active
-- =========================================================
CREATE OR REPLACE PROCEDURE sm_adm_pr_unban_user_account(
    p_user_id  INT,
    p_admin_id INT,
    p_reason   TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_current_status  account_status;
    v_restore_status  account_status;
BEGIN
    -- Cek user ada atau tidak
    SELECT account_status
    INTO v_current_status
    FROM USERS
    WHERE user_id = p_user_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'User dengan ID % tidak ditemukan', p_user_id;
    END IF;

    -- Cek apakah user benar-benar banned
    IF v_current_status <> 'banned' THEN
        RAISE NOTICE 'User dengan ID % tidak dalam status banned', p_user_id;
        RETURN;
    END IF;

    -- Default status baru = active
    v_restore_status := 'active';

    -- Jika di USER_BAN_LOG ada kolom previous_status, coba pakai nilai tersebut
    IF EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'user_ban_log'
          AND column_name = 'previous_status'
    ) THEN
        SELECT previous_status
        INTO v_restore_status
        FROM user_ban_log
        WHERE user_id = p_user_id
        ORDER BY banned_at DESC
        LIMIT 1;

        IF NOT FOUND THEN
            v_restore_status := 'active';
        END IF;
    END IF;

    -- Update status user dari banned ke status baru
    UPDATE USERS
    SET account_status = v_restore_status
    WHERE user_id = p_user_id;

    -- Catat aksi unban di USER_BAN_LOG jika tabel tersedia
    IF EXISTS (
        SELECT 1 
        FROM information_schema.tables
        WHERE table_name = 'user_ban_log'
    ) THEN
        INSERT INTO user_ban_log (
            user_id,
            admin_id,
            reason,
            banned_at
        )
        VALUES (
            p_user_id,
            p_admin_id,
            'UNBAN: ' || COALESCE(p_reason, ''),
            now()
        );
    END IF;

    RAISE NOTICE 'User % berhasil di-unban oleh admin %, status baru: %',
        p_user_id, p_admin_id, v_restore_status;
END;
$$;

-- =========================================================
-- 9. UJI COBA sm_adm_pr_unban_user_account
--    Admin mengembalikan status banned -> active
-- =========================================================

-- Asumsi: user 2 saat ini berstatus banned
CALL sm_adm_pr_unban_user_account(
    2, 
    1,
    'Banding dikabulkan oleh admin'
);

-- Cek status user
-- SELECT user_id, account_status FROM USERS WHERE user_id = 2;

-- Jika tabel user_ban_log ada, cek riwayat ban/unban
-- SELECT * FROM user_ban_log WHERE user_id = 2 ORDER BY banned_at DESC;


-- =========================================================
-- END OF FILE
-- =========================================================
