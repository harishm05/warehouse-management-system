CREATE TABLE IF NOT EXISTS Customer(
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cust_name TEXT NOT NULL,
        cust_addr TEXT NOT NULL,
        cust_city TEXT NOT NULL,
        cust_state TEXT NOT NULL,
        cust_email TEXT NOT NULL,
        cust_phone TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS Customer_Order_Details(
        sub_order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        sell_price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        tax_rate REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS Customer_Order(
        customer_id INTEGER NOT NULL,
        order_id INTEGER PRIMARY KEY,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        delivery_date DATE DEFAULT (date(CURRENT_DATE,'+7 days')),
        total_amount REAL NOT NULL,
        FOREIGN KEY(customer_id) REFERENCES Customer(customer_id),
        FOREIGN KEY(order_id) REFERENCES Customer_Order_Details(order_id)
);
CREATE TABLE IF NOT EXISTS Customer_Payment(
        customer_id INTEGER NOT NULL,
        order_id INTEGER NOT NULL,
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        payment_status TEXT,
        payment_mode TEXT,
        FOREIGN KEY(customer_id) REFERENCES Customer(customer_id),
        FOREIGN KEY(order_id) REFERENCES Customer_Order(order_id)
);
CREATE TABLE IF NOT EXISTS Warehouse(
        warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT,
        warehouse_address TEXT NOT NULL,
        warehouse_city TEXT NOT NULL,
        warehouse_state TEXT NOT NULL,
        warehouse_email TEXT NOT NULL,
        warehouse_phone TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS Logistics_Provider(
        provider_id INTEGER PRIMARY KEY AUTOINCREMENT,
        provider_name TEXT NOT NULL,
        provider_address TEXT NOT NULL,
        provider_phone TEXT NOT NULL,
        provider_email TEXT NOT NULL,
        tracking_url TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS Customer_Shipment(
        shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        shipment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        shipment_status TEXT NOT NULL,
        warehouse_id INTEGER NOT NULL,
        provider_id INTEGER NOT NULL,
        tracking_reference TEXT NOT NULL,
        FOREIGN KEY(order_id) REFERENCES Customer_Order(order_id),
        FOREIGN KEY(provider_id) REFERENCES Logistics_Provider(provider_id),
        FOREIGN KEY(warehouse_id) REFERENCES Warehouse(warehouse_id)
);
CREATE TABLE IF NOT EXISTS Supplier(
        supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
        supplier_name TEXT NOT NULL,
        supplier_address TEXT NOT NULL,
        supplier_city TEXT NOT NULL,
        contact_person TEXT NOT NULL,
        supplier_email TEXT NOT NULL,
        supplier_phone TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS Product_Inventory(
        warehouse_id INTEGER NOT NULL,
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        product_descrip TEXT NOT NULL,
        buy_price REAL NOT NULL,
        sell_price REAL NOT NULL,
        tax_rate REAL NOT NULL,
        quantity INTEGER NOT NULL,
        category TEXT NOT NULL,
        supplier_id INTEGER NOT NULL,
        FOREIGN KEY(warehouse_id) REFERENCES Warehouse(warehouse_id),
        FOREIGN KEY(supplier_id) REFERENCES Supplier(supplier_id)
);
CREATE TABLE IF NOT EXISTS Supplier_Order(
        supplier_id INTEGER NOT NULL,
        sup_order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        delivery_date DATE DEFAULT (date(CURRENT_DATE,'+7 days')),
        shipment_status TEXT NOT NULL,
        FOREIGN KEY(supplier_id) REFERENCES Supplier(supplier_id),
        FOREIGN KEY(product_id) REFERENCES Product_Inventory(product_id)
);
CREATE TABLE IF NOT EXISTS Supplier_Payment(
        sup_order_id INTEGER NOT NULL,
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        payment_amount REAL NOT NULL,
        payment_reference TEXT NOT NULL,
        payment_duedate DATE DEFAULT (date(CURRENT_DATE,'+60 days')),
        payment_status TEXT NOT NULL,
        payment_mode TEXT NOT NULL,
        FOREIGN KEY(sup_order_id) REFERENCES Supplier_Order(sup_order_id)
);