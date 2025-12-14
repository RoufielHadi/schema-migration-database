migration v20251118 {
  desc "create shop v1"
  author roufiel
  db postgres
  schema shop {
    enum order_status { PENDING, PAID, SHIPPED, CANCELLED }

    table users {
      id int primary;
      email varchar(120) unique not null;
      full_name varchar(100) not null;
      created_at timestamp default now();
    }

    table products {
      id int primary;
      name varchar(120) not null;
      price int not null;
      created_at timestamp default now();
    }

    table orders {
      id int primary;
      user_id int not null;
      status order_status default PENDING;
      created_at timestamp default now();
      fk(user_id) references users(id);
      index idx_orders_user(created_at, user_id);
    }

    table order_items {
      id int primary;
      order_id int not null;
      product_id int not null;
      qty int not null;
      fk(order_id) references orders(id);
      fk(product_id) references products(id);
    }

    seed users {
      id=1, email="admin@example.com", full_name="Admin", created_at=now();
      id=2, email="user@example.com", full_name="User", created_at=now();
    }
  }
}
