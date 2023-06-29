import mysql.connector
import time
import json

with open(r'../statics/dbStatics.json', 'r') as file:
    data = json.load(file)
    hostname = data['values']['hostname']
    username = data['values']['username']
    password = data['values']['password']
    database = data['values']['database']

print("Attempting Connection", end="")
for x in range(7):print(".", end="");time.sleep(1)

connection = mysql.connector.connect(host=hostname, user=username, password=password)
print("Success")

print("Creating Database", end="")
for x in range(7):print(".", end="");time.sleep(1)

cdbCursor = connection.cursor()
cdbCursor.execute(f"CREATE DATABASE {database}")
print("Created")


print("Attempting Connection to Database", end="")
for x in range(7):print(".", end="");time.sleep(1)
connection = mysql.connector.connect(host=hostname, user=username, password=password, database=database)
print("Success")

print("Creating Tables", end="")
for x in range(7):print(".", end="");time.sleep(1)
mycursor = connection.cursor()
mycursor.execute("""
    CREATE TABLE vouchers (
        id INT PRIMARY KEY AUTO_INCREMENT, 
        voucherNo INT UNIQUE,
        accountHead VARCHAR(255),
        paidTo VARCHAR(255),
        rupeesNo INT,
        rupeesText VARCHAR(255),
        onAccountOf VARCHAR(255),
        byChequeNoCash VARCHAR(255),
        bankAccount VARCHAR(255),
        onDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""
)

        # accountHeadOther VARCHAR(255),
print("Done")

print("Initializing Data", end="")
for x in range(7):print(".", end="");time.sleep(1)
mycursor = connection.cursor()
mycursor.execute("""
    INSERT INTO vouchers(
        voucherNo,
        accountHead,
        paidTo,
        rupeesNo,
        rupeesText,
        onAccountOf,
        byChequeNoCash,
        bankAccount 
    )
    VALUES(
        0,
        'Head',
        'Paid To',
        3,
        'Three',
        'Dummy',
        '234',
        '5446'
    )"""
)
connection.commit()
print("Done")

time.sleep(3)
print("You can close the window Now")