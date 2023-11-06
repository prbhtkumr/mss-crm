import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql', 'r') as schema_file:
    connection.executescript(schema_file.read())

cur = connection.cursor()

cur.executemany("INSERT INTO leads (name, company, address, phone, email) VALUES (?, ?, ?, ?, ?)",
                [
                    ('Aryan Patel', 'InnoTech India', '123 MG Road, Mumbai', '9876543210', 'aryan.patel@email.com'),
                    ('Neha Gupta', 'TechGuru Solutions', '456 Park Street, Delhi', '8765432109', 'neha.gupta@email.com'),
                    ('Rajesh Kumar', 'DigitalScape', '789 Gandhi Nagar, Bangalore', '7654321098', 'rajesh.kumar@email.com'),
                    ('Meera Singh', 'WebMasters India', '101 Jubilee Road, Kolkata', '6543210987', 'meera.singh@email.com')
                ])

connection.commit()
connection.close()

