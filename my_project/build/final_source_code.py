import sqlite3
from tabulate import tabulate
import os
conn = sqlite3.connect('C:\\Users\\haris\\Desktop\\Sqlite_project\\warehouse\\warehouse.db')

# Menu for sqlite3 Warehouse Management project
def Warehouse_menu():
    while True:
        print('''
              --------------------------
              Warehouse menu:
              --------------------------
              1. Warehouse Registration 
              2. Warehouse Search
              3. Warehouse Update 
              0. Previous menu
              ''')
        W_option = int(input("Enter your option: "))
        if W_option == 1:
            w_address = input("Enter Warehouse address: ")
            w_city = input("Enter location of warehouse city: ")
            w_state = input("Enter the state of warehouse: ")
            w_email = input("Enter warehouse's e-mail address: ")
            w_phone = input("Enter warehouse's phone number: ")
            print(f"Warehouse Address: {w_address}\nWarehouse City: {w_city}\nWarehouse State: {w_state}\nWarehouse Email: {w_email}\nWarehouse Phone: {w_phone}")
            c = conn.cursor()
            c.execute('''INSERT INTO Warehouse(warehouse_address, warehouse_city, warehouse_state, warehouse_email, warehouse_phone) VALUES (?, ?, ?, ?, ?)''',(w_address, w_city, w_state, w_email, w_phone))
            conn.commit()
        elif W_option == 2:
            WCity = input("Enter the warehouse city: ")
            WCity = WCity.upper()
            print('\n')
            c = conn.cursor()
            c.execute("SELECT warehouse_id, warehouse_address, warehouse_city, warehouse_state, warehouse_email, warehouse_phone FROM Warehouse WHERE upper(warehouse_city)= ?",(WCity,))
            results =tabulate(c.fetchall(),headers=["warehouse_id", "warehouse_address", "warehouse_city", "warehouse_state", "warehouse_email", "warehouse_phone"])
            if results:
                print(results)
                print('\n')
            conn.commit()
        elif W_option == 3:
            w_identity = input("Enter Warehouse id: ")
            w_address = input("Enter Warehouse address: ")
            w_city = input("Enter location of warehouse city: ")
            w_state = input("Enter the state of warehouse: ")
            w_email = input("Enter warehouse's e-mail address: ")
            w_phone = input("Enter warehouse's phone number: ")
            c = conn.cursor()
            c.execute('''UPDATE Warehouse SET warehouse_address=?, warehouse_city=?, warehouse_state=?, warehouse_email=?, warehouse_phone=? WHERE Warehouse_id =?''', (w_address,w_city, w_state, w_email, w_phone,w_identity))
            conn.commit()
        elif W_option == 0:
            MainMenu()
        else:
            print("Invalid Option")

def Supplier_menu():
    while True:
        print('''
              --------------------------
              Supplier menu:
              --------------------------
              1. Supplier Registration 
              2. Supplier Search
              3. Supplier Update 
              0. Previous menu
              ''')
        S_option = int(input("Enter your option: "))
        if S_option == 1:
            s_name = input("Enter supplier's name: ")
            s_contact_person = input("Enter contact person name for supplier: ")
            s_email = input("Enter supplier's e-mail address: ")
            s_phone = input("Enter supplier's phone number: ")
            s_address = input("Enter supplier's address: ")
            s_city = input("Enter supplier's city: ")
            print(f"Supplier Name: {s_name}\nContact Person: {s_contact_person}\nSupplier Email: {s_email}\nSupplier Phone: {s_phone}\nSupplier Address: {s_address}\nSupplier City: {s_city}")
            c = conn.cursor()
            c.execute('''INSERT INTO Supplier(supplier_name, contact_person, supplier_email, supplier_phone, supplier_address, supplier_city) VALUES (?, ?, ?, ?, ?, ?)''',(s_name, s_contact_person, s_email, s_phone, s_address, s_city))
            conn.commit()
        elif S_option == 2:
            SName = input("Enter supplier's name: ")
            SName = SName.upper()
            print('\n')
            c = conn.cursor()
            c.execute("SELECT supplier_id, supplier_name, supplier_address, supplier_city, contact_person, supplier_email, supplier_phone FROM Supplier WHERE upper(supplier_name)= ?",(SName,))
            results =tabulate(c.fetchall(),headers=["supplier_id", "supplier_name", "supplier_address", "supplier_city", "contact_person", "supplier_email", "supplier_phone"])
            if results:
                print(results)
                print('\n')
            conn.commit()
        elif S_option == 3:
            s_identity = input("Enter Supplier id: ")
            s_address = input("Enter Supplier address: ")
            s_city = input("Enter Supplier city: ")
            s_email = input("Enter Supplier's e-mail address: ")
            s_phone = input("Enter Supplier's phone number: ")
            c = conn.cursor()
            c.execute('''UPDATE Supplier SET supplier_address=?, supplier_city=?, supplier_email=?, supplier_phone=? WHERE supplier_id =?''', (s_address,s_city, s_email, s_phone, s_identity))
            conn.commit()
        elif S_option == 0:
            MainMenu()
        else:
            print("Invalid Option")

def Logistics_menu():
    while True:
        print('''
              --------------------------
              Logistics menu:
              --------------------------
              1. Logistics Registration 
              2. Logistics Search
              3. Logistics Update 
              0. Previous menu
              ''')
        L_option = int(input("Enter your option: "))
        if L_option == 1:
            L_name = input("Enter Logistics provider's name: ")
            L_address = input("Enter Logistics provider's address: ")
            L_phone = input("Enter Logistics provider's phone number: ")
            L_email = input("Enter Logistics provider's e-mail address: ")
            L_track_url = input("Enter Logistics provider's tracking url: ")
            print(f"Logistics provider's name: {L_name}\nLogistics provider's address: {L_address}\nLogistics provider's phone: {L_phone}\nLogistics provider's email: {L_email}\nLogistics provider's tracking url: {L_track_url}")
            c = conn.cursor()
            c.execute('''INSERT INTO Logistics_Provider(provider_name, provider_address, provider_phone, provider_email, tracking_url) VALUES (?, ?, ?, ?, ?)''',(L_name, L_address, L_phone, L_email, L_track_url))
            conn.commit()
        elif L_option == 2:
            LName = input("Enter Logistics provider's name: ")
            LName = LName.upper()
            print('\n')
            c = conn.cursor()
            c.execute("SELECT provider_id, provider_name, provider_address, provider_phone, provider_email, tracking_url FROM Logistics_Provider WHERE upper(provider_name)= ?",(LName,))
            results =tabulate(c.fetchall(),headers=["provider_id", "provider_name", "provider_address", "provider_phone", "provider_email", "tracking_url"])
            if results:
                print(results)
                print('\n')
            conn.commit()
        elif L_option == 3:
            L_identity = input("Enter Logistics provider's id: ")
            L_address = input("Enter Logistics provider's address: ")
            L_email = input("Enter Logistics provider's e-mail address: ")
            L_phone = input("Enter Logistics provider's phone number: ")
            c = conn.cursor()
            c.execute('''UPDATE Logistics_Provider SET provider_address=?, provider_email=?, provider_phone=? WHERE provider_id =?''', (L_address, L_email, L_phone, L_identity))
            conn.commit()
        elif L_option == 0:
            MainMenu()
        else:
            print("Invalid Option")

def Product_menu():
    while True:
        print('''
              --------------------------
              Product menu:
              --------------------------
              1. Product Registration 
              2. Product Search
              3. Product Update 
              0. Previous menu
              ''')
        P_option = int(input("Enter your option: "))
        if P_option == 1:
            P_name = input("Enter product's name: ")
            P_descrip = input("Enter product's description: ")
            P_buy_price = float(input("Enter product's buying price: "))
            P_sell_price = float(P_buy_price*1.25)
            P_taxrate = float(input("Enter product's tax rate: "))
            P_quantity = int(input("Enter quantity of product: "))
            P_category = input("Enter category of product: ")
            P_sup_id = int(input("Enter supplier id: "))
            P_warehouse_id = int(input("Enter warehouse id: "))
            print(f"Product's name: {P_name}\nProduct's description: {P_descrip}\nProduct's buying price: {P_buy_price}\nProduct's selling price: {P_sell_price}\nProduct's tax rate: {P_taxrate}\nQuantity of product: {P_quantity}\nCategory of product: {P_category}\nSupplier id: {P_sup_id}\nWarehouse id: {P_warehouse_id}")
            c = conn.cursor()
            c.execute('''INSERT INTO Product_Inventory(product_name, product_descrip, buy_price, sell_price, tax_rate, quantity, category, supplier_id, warehouse_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',(P_name, P_descrip, P_buy_price, P_sell_price, P_taxrate, P_quantity, P_category, P_sup_id, P_warehouse_id))
            conn.commit()
        elif P_option == 2:
            PCategory = input("Enter product's category: ")
            PCategory = PCategory.upper()
            print('\n')
            c = conn.cursor()
            c.execute("SELECT product_id, product_name, product_descrip, buy_price, sell_price, tax_rate, quantity, category, supplier_id, warehouse_id FROM Product_Inventory WHERE upper(category)= ?",(PCategory,))
            results =tabulate(c.fetchall(),headers=["prod_id", "prod_name", "prod_descrip", "buy_price", "sell_price", "tax_rate", "quantity", "category", "supplier_id", "warehouse_id"])
            if results:
                print(results)
                print('\n')
            conn.commit()
        elif P_option == 3:
            P_identity = input("Enter Product's id: ")
            P_name = input("Enter updated product name: ")
            P_prod_descrip = input("Enter new description: ")
            P_buy_price = float(input("Enter product's buying price: "))
            P_sell_price = float(P_buy_price*1.25)
            P_taxrate = float(input("Enter product's tax rate: "))
            P_quantity = int(input("Enter updated quantity of product: "))
            P_category = input("Enter updated category: ")
            P_sup_id = int(input("Enter updated supplier id: "))
            P_warehouse_id = int(input("Enter updated warehouse id: "))
            c = conn.cursor()
            c.execute('''UPDATE Product_Inventory SET warehouse_id=?, product_name=?, product_descrip=?, buy_price=?, sell_price=?, tax_rate=?, quantity=?, category=?, supplier_id=? WHERE product_id =?''', (P_warehouse_id, P_name, P_prod_descrip, P_buy_price, P_sell_price, P_taxrate, P_quantity, P_category, P_sup_id, P_identity))
            conn.commit()
        elif P_option == 0:
            MainMenu()
        else:
            print("Invalid Option")

def Customer_menu():
    while True:
        print('''
              --------------------------
              Customer menu:
              --------------------------
              1. Customer Registration 
              2. Customer Search
              3. Customer Update 
              0. Previous menu
              ''')
        C_option = int(input("Enter your option: "))
        if C_option == 1:
            cust_name = input("Enter Customer's name: ")
            cust_addr = input("Enter Customer's address: ")
            cust_city = input("Enter Customer's city: ")
            cust_state = input("Enter Customer's state: ")
            cust_email = input("Enter Customer's email: ")
            cust_phone = input("Enter Customer's phone number: ")
            print(f"Customer's name: {cust_name}\nCustomer's address: {cust_addr}\nCustomer's city: {cust_city}\nCustomer's state: {cust_state}\nCustomer's email: {cust_email}\nCustomer's phone number: {cust_phone}")
            c = conn.cursor()
            c.execute('''INSERT INTO Customer(cust_name, cust_addr, cust_city, cust_state, cust_email, cust_phone) VALUES (?, ?, ?, ?, ?, ?)''',(cust_name, cust_addr, cust_city, cust_state, cust_email, cust_phone))
            conn.commit()
        elif C_option == 2:
            CName = input("Enter Customer's name: ")
            CName = CName.upper()
            print('\n')
            c = conn.cursor()
            c.execute("SELECT customer_id, cust_name, cust_addr, cust_city, cust_state, cust_email, cust_phone FROM Customer WHERE upper(cust_name)= ?",(CName,))
            results =tabulate(c.fetchall(),headers=["cust_id", "cust_name", "cust_addr", "cust_city", "cust_state", "cust_email", "cust_phone"])
            if results:
                print(results)
                print('\n')
            conn.commit()
        elif C_option == 3:
            cust_identity = input("Enter Customer's id: ")
            cust_name = input("Enter updated customer's name: ")
            cust_addr = input("Enter updated customer's address: ")
            cust_city = input("Enter updated customer's city: ")
            cust_state = input("Enter updated customer's state: ")
            cust_email = input("Enter updated customer's email: ")
            cust_phone = input("Enter updated customer's phone number: ")
            c = conn.cursor()
            c.execute('''UPDATE Customer SET cust_name=?, cust_addr=?, cust_city=?, cust_state=?, cust_email=?, cust_phone=? WHERE customer_id =?''', (cust_name, cust_addr, cust_city, cust_state, cust_email, cust_phone, cust_identity))
            conn.commit()
        elif C_option == 0:
            MainMenu()
        else:
            print("Invalid Option")

def Customer_Order():
    while True:
        print('''
              --------------------------
              Customer order menu:
              --------------------------
              1. Order creation
              2. Order pending list
              3. Order search
              4. Order payment status update
              5. Order shipment list  
              6. Shipment status search / update
              7. Order Invoice
              0. Previous menu
              ''')
        C_order_option = int(input("Enter your option: "))
        if C_order_option == 1:
            inp = 'y'
            inp = inp.lower()
            t_customer_id = int(input("Enter customer id: "))
            c = conn.cursor()
            c.execute("SELECT CAST(UNIXEPOCH() AS INTEGER)")
            t_order_id = c.fetchone()[0]
            c.execute('''CREATE TEMP TABLE Temp_cust_order(
                      order_id INTEGER,
                      product_id INTEGER,
                      quantity INTEGER,
                      sell_price REAL,
                      tax_rate REAL
            )''')
            while inp == 'y':
                t_product_id = int(input("Enter product id: "))
                t_quantity = int(input("Enter quantity of product: "))
                c.execute("SELECT sell_price FROM Product_Inventory WHERE product_id= ?",(t_product_id,))
                t_sell_price = c.fetchone()[0]
                c.execute("SELECT tax_rate FROM Product_Inventory WHERE product_id= ?", (t_product_id,))
                t_tax_rate = c.fetchone()[0]
                c.execute('''INSERT INTO Temp_cust_order(order_id, product_id, quantity, sell_price, tax_rate) VALUES (?, ?, ?, ?, ?)''', (t_order_id, t_product_id, t_quantity, t_sell_price, t_tax_rate))
                while True:
                    inp = input("Do you want to order more (y/n): ")
                    inp = inp.lower()
                    if inp in ['y', 'n']:
                        break
                    else:
                        print("Invalid input. Please enter y or n")
            c.execute('''INSERT INTO Customer_Order_Details(order_id, product_id, quantity, sell_price, tax_rate) SELECT * FROM Temp_cust_order''')
            c.execute("SELECT SUM(quantity*sell_price*(1+tax_rate)) FROM Temp_cust_order WHERE order_id= ?",(t_order_id,))
            t_total_amount = c.fetchone()[0]
            c.execute('''INSERT INTO Customer_order(customer_id, order_id, total_amount) VALUES (?, ?, ?)''', (t_customer_id, t_order_id, t_total_amount))
            c.execute("DROP TABLE Temp_cust_order")
            t_payment_status = "validating"
            t_payment_mode = "Online"
            c.execute("INSERT INTO Customer_Payment(customer_id, order_id, payment_status, payment_mode) VALUES (?, ?, ?, ?)", (t_customer_id, t_order_id, t_payment_status, t_payment_mode))
            conn.commit()
        elif C_order_option == 2:
            print('\n')
            c = conn.cursor()
            c.execute('''SELECT CP.customer_id, CP.order_id, CO.order_date, CP.payment_status, CP.payment_mode FROM Customer_Payment CP,Customer_Order CO WHERE CP.payment_status='validating' AND CP.order_id=CO.order_id LIMIT 5''')
            results =tabulate(c.fetchall(),headers=["customer_id", "order_id", "order_date", "payment_status", "payment_mode"])
            if results:
                print(results)
                print('\n')
            conn.commit()
        elif C_order_option == 3:
            t_order_id = int(input("Enter order id: "))
            print('\n')
            c = conn.cursor()
            c.execute("SELECT customer_id, order_id, payment_id, payment_status, payment_mode FROM Customer_payment WHERE order_id= ?",(t_order_id,))
            results =tabulate(c.fetchall(),headers=["customer_id", "order_id", "payment_id", "payment_status", "payment_mode"])
            if results:
                print(results)
                print('\n')
            conn.commit()
        elif C_order_option == 4:
            t_order_id = int(input("Enter your order id: "))
            t_status = str(input("Is the payment done?(y/n): "))
            t_status = t_status.lower()
            if t_status == 'y':
                t_payment_status = "Success"
                t_shipment_status = "Order is being prepared..."
                t_tracking_reference = "Will be updated soon"
                t_provider_id = int(input("Enter the logistics provider id: "))
                c = conn.cursor()
                c.execute('''SELECT warehouse_id FROM Product_Inventory PI, Customer_Order_Details COD WHERE COD.product_id=PI.product_id AND order_id= ?''',(t_order_id,))
                t_warehouse_id = c.fetchone()[0]
                c.execute('''UPDATE Customer_Payment SET payment_status=? WHERE order_id=?''',(t_payment_status, t_order_id))
                c.execute('''INSERT INTO Customer_Shipment(order_id, shipment_status, warehouse_id, provider_id, tracking_reference) VALUES(?, ?, ?, ?, ?)''', (t_order_id, t_shipment_status, t_warehouse_id, t_provider_id, t_tracking_reference))
                c.execute("SELECT product_id, quantity FROM Customer_Order_details WHERE order_id= ?",(t_order_id,))
                records = c.fetchall()
                for row in records:
                    c.execute('''UPDATE Product_Inventory SET quantity= quantity-? WHERE product_id=?''',(row[1], row[0]))
                conn.commit()
            else:
                t_payment_status = "Order Cancelled"
                c = conn.cursor()
                c.execute('''UPDATE Customer_Payment SET payment_status=? WHERE order_id=?''',(t_payment_status, t_order_id))
                conn.commit()
        elif C_order_option == 5:
            print('\n')
            c = conn.cursor()
            t_shipment_status = "Order is shipped"
            c.execute("SELECT order_id, shipment_status, warehouse_id, tracking_reference FROM Customer_Shipment WHERE shipment_status!= ? LIMIT 5",(t_shipment_status,))
            results =tabulate(c.fetchall(),headers=["order_id", "shipment_status", "warehouse_id", "tracking_reference"])
            if results:
                print(results)
                print('\n')
            conn.commit()
        elif C_order_option == 6:
            t_order_id = int(input("Enter your order id: "))
            print('\n')
            c = conn.cursor()
            c.execute('''SELECT shipment_status FROM Customer_Shipment WHERE order_id =?''',(t_order_id,))
            t_shipment_status = c.fetchone()[0]
            c.execute('''SELECT order_id, shipment_date, shipment_status, provider_name, CS.provider_id, tracking_reference FROM Customer_Shipment CS, Logistics_Provider LP WHERE CS.provider_id = LP.provider_id AND order_id =?''',(t_order_id,))
            results =tabulate(c.fetchall(),headers=["order_id", "shipment_date", "shipment_status", "provider_name", "provider_id", "tracking_reference"])
            if results:
                print(results)
                print('\n')
            if t_shipment_status != "Order is shipped":
                t_status = str(input("Is the order ready for shipment?(y/n): "))
                t_status = t_status.lower()
                if t_status == 'y':
                    t_shipment_status = "Order is shipped"
                    c = conn.cursor()
                    c.execute('''SELECT ABS(RANDOM()) AS tf ''')
                    t_tracking_reference = c.fetchone()[0]
                    c.execute('''SELECT CURRENT_TIMESTAMP''')
                    t_shipment_date = c.fetchone()[0]
                    t_provider_id = int(input("Enter the logistics provider id: "))
                    c.execute('''UPDATE Customer_Shipment SET shipment_status=?, shipment_date=?, provider_id=?, tracking_reference=? WHERE order_id=?''',(t_shipment_status, t_shipment_date, t_provider_id, t_tracking_reference, t_order_id))
            conn.commit()
        elif C_order_option == 7:
            t_order_id = int(input("Enter the invoice order id: "))
            print('\n')
            print("------------------------------------------------------------------------------------------------")
            print(f"                                 Invoice for Order id: {t_order_id}                            ")
            print("------------------------------------------------------------------------------------------------")
            c = conn.cursor()
            c.execute('''SELECT cust_name, cust_addr, cust_city, cust_state, cust_phone, order_id FROM Customer C, Customer_Order CO WHERE CO.customer_id= C.customer_id AND order_id=?''',(t_order_id,))
            records = c.fetchall()
            for row in records:
                print("Name: ",row[0])
                print("Address: ", row[1])
                print("City: ",row[2])
                print("State: ", row[3])
                print("Phone no: ", row[4])
                print("Order id: ", row[5])
            print("------------------------------------------------------------------------------------------------")
            c.execute('''SELECT product_name, COD.quantity, COD.sell_price, COD.tax_rate, (COD.quantity*COD.sell_price*(1+COD.tax_rate)) subtotal FROM Customer_Order_details COD, Product_Inventory PI WHERE COD.product_id= PI.product_id AND order_id=?''',(t_order_id,))
            results =tabulate(c.fetchall(),headers=["product_name", "quantity", "sell_price", "tax_rate", "sub_total"])
            if results:
                print(results)
            print('\n')
            c.execute('''SELECT order_date, delivery_date, total_amount FROM Customer_Order WHERE order_id=?''',(t_order_id,))
            results =tabulate(c.fetchall(),headers=["order_date", "delivery_date", "total_amount"])
            if results:
                print(results)
            conn.commit()
            print("------------------------------------------------------------------------------------------------")
        elif C_order_option == 0:
            MainMenu()
        else:
            print("Invalid Option")

def Supplier_Order():
    while True:
        print('''
              --------------------------
              Supplier order menu:
              --------------------------
              1. Shortage of goods
              2. Order creation
              3. Supplier pending order
              4. Supplier order cancellation
              5. Supplier order receiving
              6. Order payment update
              0. Previous menu
              ''')
        Supp_order_option = int(input("Enter your option: "))
        if Supp_order_option == 1:
            t_quantity = 75
            c = conn.cursor()
            c.execute("SELECT product_id, product_name, quantity, supplier_id FROM Product_Inventory WHERE quantity < ?", (t_quantity,))
            shortage_products = c.fetchall()
            if shortage_products:
                print("Shortage of Goods Report:")
                print('\n')
                headers = ["Prod_ID", "Prod_Name", "Quantity", "Supp_id"]
                print(tabulate(shortage_products, headers=headers))
            else:
                print("No shortage of goods")
            conn.commit()  
        elif Supp_order_option == 2:
            t_product_id = int(input("Enter the product id: "))
            c = conn.cursor()
            c.execute('''SELECT supplier_id FROM Product_Inventory WHERE product_id=?''',(t_product_id,))
            t_supplier_id = c.fetchone()[0]
            t_new_quantity = int(input("Enter the quantity of product: "))
            t_shipment_status = "Order submitted"
            c.execute('''INSERT INTO Supplier_Order(supplier_id, product_id, quantity, shipment_status) VALUES (?, ?, ?, ?)''', (t_supplier_id, t_product_id, t_new_quantity, t_shipment_status))
            conn.commit()
        elif Supp_order_option == 3:
            print("Supplier pending list")
            print('\n')
            t_shipment_status = "Order submitted"       
            c = conn.cursor()
            c.execute('''SELECT supplier_id, sup_order_id, product_id, quantity, shipment_status FROM Supplier_Order WHERE shipment_status=?''',(t_shipment_status,))
            results =tabulate(c.fetchall(),headers=["supplier_id", "supplier_order_id", "product_id", "quantity", "shipment_status"])
            if results:
                print(results)
                print('\n')
            conn.commit()
        elif Supp_order_option == 4:
            t_sup_order_id = int(input("Enter the supplier order id: "))
            print('\n')
            t_status = str(input("Do you want to cancel the order?(y/n): "))
            t_shipment_status = "Order cancelled"
            t_status = t_status.lower()
            if t_status == 'y':
                c = conn.cursor()
                c.execute('''UPDATE Supplier_Order SET shipment_status=? WHERE sup_order_id=?''',(t_shipment_status, t_sup_order_id))
                conn.commit()
        elif Supp_order_option == 5:
            t_sup_order_id = int(input("Enter the supplier order id: "))
            t_shipment_status = "Order recieved"
            t_new_quantity = int(input("Enter the quantity of product: "))
            c.execute('''SELECT UNIXEPOCH()''')
            t_payment_reference = c.fetchone()[0]
            t_payment_status = "Payment Initiated"
            t_payment_mode = "Cheque payment"
            c = conn.cursor()
            c.execute('''SELECT product_id FROM Supplier_Order WHERE sup_order_id=?''',(t_sup_order_id,))
            t_product_id = c.fetchone()[0]
            c.execute('''SELECT (buy_price*?) FROM Product_Inventory WHERE product_id=?''',(t_new_quantity, t_product_id,))
            t_payment_amount = c.fetchone()[0]
            c.execute('''UPDATE Supplier_Order SET shipment_status=?, quantity=? WHERE sup_order_id=?''',(t_shipment_status, t_new_quantity, t_sup_order_id))
            c.execute('''INSERT INTO Supplier_Payment(sup_order_id, payment_reference, payment_status, payment_mode, payment_amount) VALUES(?, ?, ?, ?, ?)''',(t_sup_order_id, t_payment_reference, t_payment_status, t_payment_mode, t_payment_amount))
            c.execute('''UPDATE Product_Inventory SET quantity= quantity+? WHERE product_id=?''',(t_new_quantity, t_product_id))
            conn.commit()
        elif Supp_order_option == 6:
            t_sup_order_id = int(input("Enter the supplier order id: "))
            t_payment_status = "Payment Initiated"
            c = conn.cursor()
            c.execute('''SELECT sup_order_id, payment_amount, payment_reference, payment_duedate, payment_mode FROM Supplier_Payment WHERE payment_status=? LIMIT 5''',(t_payment_status,))
            print('\n')
            results =tabulate(c.fetchall(),headers=["supplier_order_id", "payment_amount", "payment_reference", "payment_duedate", "payment_mode"])
            if results:
                print(results)
                print('\n')
            t_payment_status = "Payment Completed"
            c.execute('''SELECT CURRENT_DATE''')
            t_payment_duedate= c.fetchone()[0]
            c.execute('''UPDATE Supplier_Payment SET payment_status=?, payment_duedate=? WHERE sup_order_id=?''', (t_payment_status, t_payment_duedate, t_sup_order_id))
            conn.commit()
        elif Supp_order_option == 0:
            MainMenu()
        else:
            print("Invalid Option")

def MainMenu():
    while True:
        print('''
          ----------------------
          Main Menu
          ----------------------
          1. Warehouse
          2. Supplier
          3. Logistics Provider
          4. Product Inventory
          5. Customer
          6. Customer's order
          7. Supplier's order   
          0. Exit
          ''')
        option = int(input("Enter your option: "))
        if option == 1:
            Warehouse_menu()
        elif option == 2:
            Supplier_menu()
        elif option == 3:
            Logistics_menu()
        elif option == 4:
            Product_menu()
        elif option == 5:
            Customer_menu()
        elif option == 6:
            Customer_Order()
        elif option == 7:
            Supplier_Order()
        elif option == 0:
            conn.close()
            os._exit(0)
        else:
            print("Invalid option")

MainMenu()
