import sqlite3
import os

class DBHandler:
    def __init__(self):
        self.db_name = "database/db.sqlite"
        if not os.path.isfile(self.db_name):
            # create db
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Database {self.db_name} created successfully")
        else:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Database {self.db_name} already exists")
            
        self.create_table("users", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, contact TEXT, username TEXT, password TEXT")
        self.create_table("business", "id INTEGER PRIMARY KEY AUTOINCREMENT, business_name TEXT, business_email TEXT, business_address TEXT, business_contact TEXT, business_owner TEXT")
        self.create_table("khata",columns="khata_id INTEGER PRIMARY KEY AUTOINCREMENT, khata_name TEXT")
        self.create_table(table_name="accounts", columns="accounts_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, address TEXT, balance_type TEXT, balance REAL,khata_id INTEGER, FOREIGN KEY(khata_id) REFERENCES khata(khata_id)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS account_details (account_details_id INTEGER PRIMARY KEY AUTOINCREMENT, account_id INTEGER, date TEXT, refrence TEXT DEFAULT 'account created', description TEXT, cash_in REAL DEFAULT 0, cash_out REAL DEFAULT 0, remaining REAL, FOREIGN KEY(account_id) REFERENCES accounts(accounts_id))")
        # self.create_table('business', 'id INTEGER PRIMARY KEY AUTOINCREMENT, business_name TEXT, business_email TEXT, business_address TEXT, business_contact TEXT, business_owner TEXT')
        # self.create_table('products', 'product_id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT, uom TEXT, product_stock INTEGER DEFAULT 0')
        self.conn.execute("CREATE TABLE IF NOT EXISTS roznamcha (roznamcha_id INTEGER PRIMARY KEY AUTOINCREMENT, khata_id INTEGER, accounts_id INTEGER, date TEXT, refrences TEXT, description TEXT,cash_in INTEGER DEFAULT 0, cash_out INTEGER DEFAULT 0,remaining INTEGER, FOREIGN KEY(khata_id) REFERENCES khata(khata_id), FOREIGN KEY(accounts_id) REFERENCES accounts(accounts_id))")
        # self.conn.execute("CREATE TABLE IF NOT EXISTS sales (sale_id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER, customer_id INTEGER, date TEXT, quantity INTEGER, rate INTEGER, total_amount INTEGER, cash_paid INTEGER, cash_received INTEGER,  sub_total INTEGER, FOREIGN KEY(product_id) REFERENCES products(product_id), FOREIGN KEY(customer_id) REFERENCES customers(customer_id))")
        # self.conn.execute("CREATE TABLE IF NOT EXISTS suppliers (supplier_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, address TEXT, balance_type TEXT, balance REAL)")
        # self.conn.execute('''CREATE TABLE IF NOT EXISTS stock(stock_id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER, date TEXT, supplier_id INTEGER, stock INTEGER, rate REAL, amount REAL, paid_amount REAL, FOREIGN KEY(product_id) REFERENCES products(product_id), FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id))''')
        # self.conn.execute(f"CREATE TABLE IF NOT EXISTS supplier_cash_paid (id INTEGER PRIMARY KEY AUTOINCREMENT,supplier_id INTEGER,date TEXT,payment_method TEXT,cash_paid REAL,remaining REAL,description TEXT DEFAULT 'Cash Paid',quantity INTEGER DEFAULT 0,rate REAL DEFAULT 0,amount REAL DEFAULT 0,FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id))")
        # self.conn.execute(f"CREATE TABLE IF NOT EXISTS customer_cash_received (id INTEGER PRIMARY KEY AUTOINCREMENT,customer_id INTEGER,date TEXT,payment_method TEXT,cash_received REAL DEFAULT 0,remaining REAL,description TEXT DEFAULT 'Cash Received',quantity INTEGER DEFAULT 0,rate REAL DEFAULT 0,amount REAL DEFAULT 0,cash_paid REAL DEFAULT 0,FOREIGN KEY(customer_id) REFERENCES customers(customer_id))")



    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def check_table(self, table_name):
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        if self.cursor.fetchall():
            return True
        return False


    def insert(self, table_name, columns, values):
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
        self.conn.commit()

    def select(self, table_name, columns, condition):
        self.cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {condition}")
        return self.cursor.fetchall()

    def select_all(self, table_name, columns):
        self.cursor.execute(f"SELECT {columns} FROM {table_name}")
        return self.cursor.fetchall()

    def update(self, table_name, columns, values, condition):
        self.cursor.execute(f"UPDATE {table_name} SET {columns} = {values} WHERE {condition}")
        self.conn.commit()

    def delete(self, table_name, condition):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.conn.commit()

    def close(self):
        self.conn.close()

    def authenticate(self,username, password):
        self.cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
        if self.cursor.fetchall():
            return True
        return False


    