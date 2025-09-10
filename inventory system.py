import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="12345",  
    database="inventory_store")
cur = conn.cursor()

def login():
    u = input("Username: ")
    p = input("Password: ")
    cur.execute("select * from users WHERE username=%s AND password=%s", (u, p))
    if cur.fetchone():
        print(" Login successful")
        return True
    else:
        print("Invalid login")
        return False

def add_item():
    name = input("Item name: ")
    qty = int(input("Quantity: "))
    cur.execute("insert into inventory (item, qty) VALUES (%s, %s)", (name, qty))
    conn.commit()
    print(" Item added!")

def list_items():
    cur.execute("select * from inventory")
    for r in cur.fetchall():
        print(f"ID:{r[0]} | {r[1]} | Qty:{r[2]}")

def update_item():
    id = int(input("Item ID: "))
    qty = int(input("New Quantity: "))
    cur.execute("update inventory set qty=%s where id=%s", (qty, id))
    conn.commit()
    print("Item updated!")

def delete_item():
    id = int(input("Item ID: "))
    cur.execute("delete from inventory where id=%s", (id,))
    conn.commit()
    print("item deleted")

def menu():
    while True:
        print("\n1. Add Item\n2. List Items\n3. Update Item\n4. Delete Item\n5. Exit")
        ch = input("Choose: ")
        if ch == "1": add_item()
        elif ch == "2": list_items()
        elif ch == "3": update_item()
        elif ch == "4": delete_item()
        elif ch == "5": break
        else: print(" Invalid choice")

if login():
    menu()

cur.close()
conn.close()
