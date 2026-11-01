CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    contact_email TEXT UNIQUE NOT NULL
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    stock_quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    min_threshold INTEGER DEFAULT 10, -- Triggers low-stock notice
    supplier_id INTEGER,
    FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id)
);
