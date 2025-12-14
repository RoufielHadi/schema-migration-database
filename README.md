# DatabaseSchemaDSL (ANTLR4 + Python)

Project scaffold untuk DSL skema & migrasi database dengan ANTLR4 (target Python). Dirancang untuk Vibe Code/Windsurf.

- Bahasa/grammar: `grammar/DBSchema.g4`
- Implementasi: `src/` (AST, Visitor, Validator, Generator, CLI)
- Contoh DSL: `examples/shop.dsl`
- Output migrasi: `migrations/*.sql`
- Parser hasil generate: `generated/`
- Referensi: `/mnt/data/028_Roufiel Hadi_Rencana Domail Specific Language.pdf`

## Prasyarat
- Java 11+ (untuk menjalankan ANTLR Tool)
- ANTLR jar 4.13.2 (letakkan di `C:\tools\antlr\antlr-4.13.2-complete.jar` atau set env `ANTLR_JAR`)
- Python 3.10+

```bash
pip install -r requirements.txt
```

## Generate Grammar (VS Code/Windsurf)
- Buka `grammar/DBSchema.g4`
- Tekan `Ctrl+Shift+B` → Task: "Generate ANTLR (Python)"
- File Python hasil generate akan muncul di folder `generated/`

Perintah manual (alternatif):
```bash
java -cp "C:\tools\antlr\antlr-4.13.2-complete.jar" org.antlr.v4.Tool -Dlanguage=Python3 grammar/DBSchema.g4 -o generated
```

## CLI
Gunakan modul CLI sederhana:

- Parse dan snapshot AST (JSON):
```bash
python -m src.cli.dslc compile-dsl examples/shop.dsl
```
- Diff dua snapshot:
```bash
python -m src.cli.dslc diff .snapshots/<old>.json .snapshots/<new>.json
```
- Generate migration SQL (UP & DOWN) dari DSL:
```bash
python -m src.cli.dslc migrate up --target postgres --apply
```
Catatan: `--apply` tidak mengeksekusi SQL (sengaja demi keamanan). Review file `.sql` dan jalankan manual di DB Anda.

## Struktur Folder
- `.vscode/tasks.json` → Task generate ANTLR
- `grammar/DBSchema.g4` → Grammar ANTLR4
- `src/ast` → Kelas AST (Schema, Table, Column, Enum, FK, Index, Seed)
- `src/visitor/SchemaBuilderVisitor.py` → Visitor tree → AST
- `src/validator/SemanticValidator.py` → Validasi semantik & diff (flag destructive)
- `src/generator/PostgreSQLGenerator.py` → Generator SQL Postgres
- `src/cli/dslc.py` → CLI (compile, compile-dsl, diff, migrate up/down)
- `src/main.py` → Contoh runner yang menghasilkan migrations SQL
- `examples/shop.dsl` → Contoh DSL lengkap
- `tests/test_postgres_generator.py` → Unit test minimal (pytest)

## Menjalankan Contoh
1. Generate grammar → `Ctrl+Shift+B`
2. Jalankan parser + buat snapshot:
   ```bash
   python -m src.cli.dslc compile-dsl examples/shop.dsl
   ```
3. Hasilkan migrasi:
   ```bash
   python -m src.cli.dslc migrate up --target postgres
   ```
   File akan disimpan ke `migrations/<timestamp>_create_shop_v1.sql` (nama berdasarkan DESC)

## Catatan
- Generator menamai constraint FK: `fk_<table>_<col>`
- `CREATE TABLE IF NOT EXISTS` dan `DROP TABLE IF EXISTS` (DOWN urut terbalik)
- Enum dibuat via `CREATE TYPE` dibungkus `DO $$ BEGIN ... EXCEPTION WHEN duplicate_object THEN NULL; END $$;`
- Nilai default fungsi (mis. `now()`) dibiarkan tanpa quote. Nilai enum tanpa quote (mis. `PENDING`) akan di-quote sebagai label enum.
- Beberapa operasi DOWN destruktif diberi TODO untuk review manual.

## Testing
```bash
pytest -q
```

## Keamanan
- CLI tidak mengeksekusi SQL ke DB secara otomatis.
- Deteksi perubahan destruktif (drop column/shorten varchar) diberi flag `destructive: true` di hasil diff.

## Lisensi
MIT
