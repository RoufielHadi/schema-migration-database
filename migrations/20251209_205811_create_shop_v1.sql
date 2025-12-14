-- MIGRATION
-- MIGRATION ID: v20251118
-- DESC: create shop v1
-- AUTHOR: roufiel
-- DB: postgres
-- CHECKSUM: 3381facb39fdbeaec3f965991136088098c1c1ca1be4a5dc49f1af77aa948d98
--

-- UP
CREATE SCHEMA IF NOT EXISTS "shop";

DO $$ BEGIN
  CREATE TYPE "shop"."order_status" AS ENUM ('PENDING', 'PAID', 'SHIPPED', 'CANCELLED');
EXCEPTION
  WHEN duplicate_object THEN NULL;
END $$;

CREATE TABLE IF NOT EXISTS "shop"."users" (
  "id" int PRIMARY KEY,
  "email" varchar(120) NOT NULL UNIQUE,
  "full_name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT now()
);

CREATE TABLE IF NOT EXISTS "shop"."products" (
  "id" int PRIMARY KEY,
  "name" varchar(120) NOT NULL,
  "price" int NOT NULL,
  "created_at" timestamp DEFAULT now()
);

CREATE TABLE IF NOT EXISTS "shop"."orders" (
  "id" int PRIMARY KEY,
  "user_id" int NOT NULL,
  "status" "shop"."order_status" DEFAULT 'PENDING',
  "created_at" timestamp DEFAULT now()
);

CREATE TABLE IF NOT EXISTS "shop"."order_items" (
  "id" int PRIMARY KEY,
  "order_id" int NOT NULL,
  "product_id" int NOT NULL,
  "qty" int NOT NULL
);

ALTER TABLE "shop"."orders"
  ADD CONSTRAINT "fk_orders_user_id" FOREIGN KEY ("user_id")
  REFERENCES "shop"."users" ("id");

CREATE INDEX IF NOT EXISTS "idx_orders_user" ON "shop"."orders" ("created_at", "user_id");

ALTER TABLE "shop"."order_items"
  ADD CONSTRAINT "fk_order_items_order_id" FOREIGN KEY ("order_id")
  REFERENCES "shop"."orders" ("id");

ALTER TABLE "shop"."order_items"
  ADD CONSTRAINT "fk_order_items_product_id" FOREIGN KEY ("product_id")
  REFERENCES "shop"."products" ("id");

INSERT INTO "shop"."users" ("id", "email", "full_name", "created_at") VALUES (1, 'admin@example.com', 'Admin', now());

INSERT INTO "shop"."users" ("id", "email", "full_name", "created_at") VALUES (2, 'user@example.com', 'User', now());

-- DOWN
DROP TABLE IF EXISTS "shop"."order_items";
DROP TABLE IF EXISTS "shop"."orders";
DROP TABLE IF EXISTS "shop"."products";
DROP TABLE IF EXISTS "shop"."users";
DROP TYPE IF EXISTS "shop"."order_status";
