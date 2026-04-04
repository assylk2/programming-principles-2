from connect import connect
import csv

# ADD contact
def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


# SHOW all
def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


# UPDATE
def update_contact(old_name, new_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET name=%s WHERE name=%s",
        (new_name, old_name)
    )

    conn.commit()
    cur.close()
    conn.close()


# DELETE
def delete_contact(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE name=%s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()


# CSV IMPORT
def insert_from_csv(file):
    conn = connect()
    cur = conn.cursor()

    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()


# MENU
while True:
    print("\n1.Add 2.Show 3.Update 4.Delete 5.Import CSV 6.Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        insert_contact(name, phone)

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        old = input("Old name: ")
        new = input("New name: ")
        update_contact(old, new)

    elif choice == "4":
        name = input("Delete name: ")
        delete_contact(name)

    elif choice == "5":
        insert_from_csv("contacts.csv")

    elif choice == "6":
        break