from connect import connect

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    
    conn.commit()
    cur.close()
    conn.close()
    
    print("Saved!")

def show_contacts():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    
    for r in rows:
        print(r)
    
    cur.close()
    conn.close()

def search():
    pattern = input("Search: ")
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    
    for r in rows:
        print(r)
    
    cur.close()
    conn.close()

def pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    
    for r in rows:
        print(r)
    
    cur.close()
    conn.close()

def delete():
    value = input("Name or phone to delete: ")
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("CALL delete_contact(%s)", (value,))
    
    conn.commit()
    cur.close()
    conn.close()
    
    print("Deleted!")

def bulk_insert():
    names = input("Names (comma): ").split(",")
    phones = input("Phones (comma): ").split(",")
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("CALL insert_many_contacts(%s, %s)", (names, phones))
    
    conn.commit()
    cur.close()
    conn.close()

def menu():
    while True:
        print("\n1.Add 2.Show 3.Search 4.Pagination 5.Delete 6.Bulk 7.Exit")
        ch = input("Choose: ")
        
        if ch == "1":
            add_contact()
        elif ch == "2":
            show_contacts()
        elif ch == "3":
            search()
        elif ch == "4":
            pagination()
        elif ch == "5":
            delete()
        elif ch == "6":
            bulk_insert()
        elif ch == "7":
            break

menu()