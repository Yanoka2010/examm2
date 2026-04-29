-- Скрипт структуры БД для задания ГИА ДЭ БУ
-- Предметная область: магазин электрозапчастей

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS products_category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS products_manufacturer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS products_supplier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS products_unit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    abbreviation VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS products_product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    quantity INTEGER NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    discount DECIMAL(5, 2) NOT NULL DEFAULT 0 CHECK (discount >= 0 AND discount <= 100),
    image VARCHAR(100),
    category_id BIGINT NOT NULL,
    manufacturer_id BIGINT NOT NULL,
    supplier_id BIGINT NOT NULL,
    unit_id BIGINT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES products_category(id) ON DELETE CASCADE,
    FOREIGN KEY (manufacturer_id) REFERENCES products_manufacturer(id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES products_supplier(id) ON DELETE CASCADE,
    FOREIGN KEY (unit_id) REFERENCES products_unit(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS orders_orderstatus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS orders_pickuppoint (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address VARCHAR(300) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS orders_order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_number VARCHAR(50) NOT NULL UNIQUE,
    order_date DATETIME NOT NULL,
    delivery_date DATETIME,
    customer_id INTEGER NOT NULL,
    status_id BIGINT NOT NULL,
    pickup_point_id BIGINT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES auth_user(id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES orders_orderstatus(id) ON DELETE CASCADE,
    FOREIGN KEY (pickup_point_id) REFERENCES orders_pickuppoint(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS orders_orderitem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quantity INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    order_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders_order(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products_product(id) ON DELETE CASCADE,
    CONSTRAINT orders_orderitem_order_id_product_id_uniq UNIQUE (order_id, product_id)
);
