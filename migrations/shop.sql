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

