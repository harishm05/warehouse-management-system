# Warehouse Management System (WMS)
    The Warehouse Management System (WMS) is a software application designed to streamline and optimize warehouse operations, including inventory management, order processing, and reporting. The system is built using Python and SQLite and supports key functionalities like registering warehouses, managing suppliers, processing orders, and generating insightful reports.

## Folder Structure:

``` plaintext
my_project/
├── build/                                        # Contains compiled code and other build artifacts
│   ├── final_source_code.py                      # Final Python code
│   ├── final_database.sql                        # Final SQL schema
│   ├── final_database.db                         # Final SQLite database
│   └── application.exe                           # Executable file
├── src/                                          # Source code and scripts
│   ├── warehouse_v1.py
│   ├── warehouse_v2.py
│   └── warehouse_source_code_final_version.py    # Main application script
├── database/                                     # Database and SQL files
│   ├── warehouse_db_final_20240504.db
│   └── warehouse_sql_final_version.sql
├── docs/                                         # Documentation
│   ├── Database_schema.xlsx                      # Database schema in Excel format
│   ├── Flowchart.png                             # Flowchart image for application workflow
│   ├── Project_plan.txt                          # Project planning document
│   └── Project_report.pdf                        # Detailed project report
└── README.md                                     # Project overview and setup instructions
```

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)

## Features
- **Warehouse Management**: Register, search, and update warehouses.
- **Supplier Management**: Manage supplier information and track inventory.
- **Logistics**: Register logistics providers and manage shipment tracking.
- **Product Inventory**: Track inventory with product registration, categorization, and quantity updates.
- **Customer Management**: Handle customer details and order histories.
- **Order Processing**: Create, search, and manage customer and supplier orders with real-time status updates.
- **Data Integrity**: Validates and handles user inputs to ensure data reliability.

## Technologies Used
- **Programming Language**: Python
- **Database**: SQLite with SQLite3 module
- **ER Diagram Tool**: DBeaver
- **Modules**: 
  - `sqlite3` for database operations
  - `tabulate` for formatting query results into tables
  - `os` for file handling and system interactions
- **IDE**: Visual Studio Code

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/warehouse-management-system.git
   ```
2. Change the project directory:
   ```bash
   cd warehouse-management-system
   ```
3. Install the required Python modules:
   ```bash
   pip install tabulate
   ```
4. Ensure that an SQLite database file named `warehouse.db` is located in the specified directory (adjust file path as needed in the code).

## Usage
1. Run the Python script:
   ```bash
   python final_source_code.py
   ```
2. Follow the on-screen instructions to navigate the menu:
    -**Main Menu**:             Choose from Warehouse, Supplier, Logistics Provider, Product Inventory, Customer, Customer Order, or Supplier Order options.
    -**Warehouse Management**:  Register a new warehouse or update details of an existing one.
    -**Supplier Management**:   Register, search, and update suppliers.
    -**Order Management**:      Create new orders for customers or suppliers, check pending orders, and update shipment statuses.
    -**Generate Reports**:      Generate reports and invoices based on order and inventory data.

## Example Code Snippets
Here's an example of how new warehouse is registered.

```python
def register_warehouse():
    w_address = input("Enter Warehouse address: ")
    w_city = input("Enter location of warehouse city: ")
    w_state = input("Enter the state of warehouse: ")
    w_email = input("Enter warehouse's email address: ")
    w_phone = input("Enter warehouse's phone number: ")
    c = conn.cursor()
    c.execute(
        '''INSERT INTO Warehouse (warehouse_address, warehouse_city, warehouse_state, warehouse_email, warehouse_phone) 
        VALUES (?, ?, ?, ?, ?)''',
        (w_address, w_city, w_state, w_email, w_phone)
    )
    conn.commit()
```
## Future Enhancements

The WMS project can be enhanced with additional features:

    -Barcode Scanning: Integrate barcode scanning for faster inventory management.
    -Real-time Reporting and Analytics: Generate real-time insights into warehouse performance.
    -Mobile Application Support: Develop a companion mobile app for on-the-go management.
    -Predictive Inventory Management: Use analytics to forecast demand and optimize inventory replenishment.

> **Acknowledgments**  
> - [Python Documentation](https://docs.python.org/3/library/)
> - [SQLite Documentation](https://sqlite.org/doclist.html)
> - [Tabulate Library](https://pypi.org/project/tabulate/)

