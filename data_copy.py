# import sqlite3

# # Connect to the database
# conn = sqlite3.connect('database/db.sqlite')
# cursor = conn.cursor()

# # Create a new table with the desired data type for the 'date' column
# cursor.execute("CREATE TABLE IF NOT EXISTS roznamcha_new (roznamcha_id INTEGER PRIMARY KEY AUTOINCREMENT, khata_id INTEGER, accounts_id INTEGER, date DATE, cash_type TEXT, refrences TEXT, description TEXT, cash_in INTEGER DEFAULT 0, cash_out INTEGER DEFAULT 0, remaining INTEGER, accounts_remaining INTEGER DEFAULT 0, FOREIGN KEY(khata_id) REFERENCES khata(khata_id), FOREIGN KEY(accounts_id) REFERENCES accounts(accounts_id))")

# # Copy data from the old table to the new table
# # cursor.execute("INSERT INTO roznamcha_new (khata_id, accounts_id, date, cash_type, refrences, description, cash_in, cash_out, remaining, accounts_remaining) SELECT khata_id, accounts_id, strftime('%d-%m-%Y', date), cash_type, refrences, description, cash_in, cash_out, remaining, accounts_remaining FROM roznamcha")
# # Fetch data from the old table
# cursor.execute("SELECT * FROM roznamcha where date between '2023-07-01' and '2023-07-30'")
# # rows = cursor.fetchall()
# # cursor.execute("SELECT * FROM roznamcha")
# rows = cursor.fetchall()
# for row in rows:
#     print(row[3],end=' ')
# # Convert the date format and insert data into the new table
# # for row in rows:
# #     roznamcha_id, khata_id, accounts_id, date_str, cash_type, refrences, description, cash_in, cash_out, remaining, accounts_remaining = row
# #     # Convert the date format 'day/month/year' to 'year-month-day'
# #     date_parts = date_str.split('/')
# #     date = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
# #     # Insert the converted data into the new table
# #     cursor.execute("INSERT INTO roznamcha_new (khata_id, accounts_id, date, cash_type, refrences, description, cash_in, cash_out, remaining, accounts_remaining) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (khata_id, accounts_id, date, cash_type, refrences, description, cash_in, cash_out, remaining, accounts_remaining))

# # # Drop the old table
# # cursor.execute("DROP TABLE roznamcha")

# # # # Rename the new table to the original table name
# # cursor.execute("ALTER TABLE roznamcha_new RENAME TO roznamcha")

# # Commit the changes and close the connection
# conn.commit()
# conn.close()
