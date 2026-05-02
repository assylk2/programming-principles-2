import json
import csv
from connect import get_connection

conn = get_connection()
cur = conn.cursor()


# =========================
# HELPERS
# =========================
def get_group_id(name):
    cur.execute("SELECT id FROM groups WHERE name=%s", (name,))
    row = cur.fetchone()

    if row:
        return row[0]

    cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (name,))
    return cur.fetchone()[0]


# =========================
# ADD CONTACT
# =========================
def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group: ")

    gid = get_group_id(group)

    cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """, (name, email, birthday, gid))

    cid = cur.fetchone()[0]

    while True:
        phone = input("Phone (stop to finish): ")
        if phone == "stop":
            break

        ptype = input("Type (home/work/mobile): ")

        cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES (%s, %s, %s)
        """, (cid, phone, ptype))

    conn.commit()
    print("✅ Added")


# =========================
# CSV IMPORT
# =========================
def import_csv():
    with open("contacts.csv") as f:
        reader = csv.DictReader(f)

        for row in reader:
            gid = get_group_id(row["group"])

            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (row["name"], row["email"], row["birthday"], gid))

            cid = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s)
            """, (cid, row["phone"], row["type"]))

    conn.commit()
    print("✅ CSV imported")


# =========================
# FILTER BY GROUP
# =========================
def filter_group():
    g = input("Group: ")

    cur.execute("""
        SELECT c.name, c.email, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (g,))

    for r in cur.fetchall():
        print(r)


# =========================
# SEARCH
# =========================
def search():
    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))

    for r in cur.fetchall():
        print(r)


# =========================
# SORT
# =========================
def sort_contacts():
    s = input("Sort by (name/birthday/created_at): ")

    if s not in ["name", "birthday", "created_at"]:
        s = "name"

    cur.execute(f"SELECT name,email,birthday FROM contacts ORDER BY {s}")

    for r in cur.fetchall():
        print(r)


# =========================
# PAGINATION
# =========================
def paginate():
    limit = 5
    offset = 0

    while True:
        cur.execute("SELECT * FROM contacts LIMIT %s OFFSET %s", (limit, offset))

        rows = cur.fetchall()
        for r in rows:
            print(r)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        else:
            break


# =========================
# EXPORT JSON
# =========================
def export_json():
    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name,
        json_agg(json_build_object('phone', p.phone, 'type', p.type))
        FROM contacts c
        LEFT JOIN phones p ON c.id = p.contact_id
        LEFT JOIN groups g ON c.group_id = g.id
        GROUP BY c.id, g.name
    """)

    data = []
    for r in cur.fetchall():
        data.append({
            "name": r[0],
            "email": r[1],
            "birthday": str(r[2]),
            "group": r[3],
            "phones": r[4]
        })

    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Exported")


# =========================
# IMPORT JSON
# =========================
def import_json():
    with open("contacts.json") as f:
        data = json.load(f)

    for c in data:
        cur.execute("SELECT id FROM contacts WHERE name=%s", (c["name"],))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{c['name']} exists (skip/overwrite): ")

            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (c["name"],))

        gid = get_group_id(c["group"])

        cur.execute("""
            INSERT INTO contacts(name,email,birthday,group_id)
            VALUES (%s,%s,%s,%s)
            RETURNING id
        """, (c["name"], c["email"], c["birthday"], gid))

        cid = cur.fetchone()[0]

        for p in c["phones"]:
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s,%s,%s)
            """, (cid, p["phone"], p["type"]))

    conn.commit()
    print("✅ Imported")


# =========================
# PROCEDURES
# =========================
def add_phone_proc():
    name = input("Name: ")
    phone = input("Phone: ")
    ptype = input("Type: ")

    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))
    conn.commit()


def move_group_proc():
    name = input("Name: ")
    group = input("Group: ")

    cur.execute("CALL move_to_group(%s,%s)", (name, group))
    conn.commit()


def create_search_function():
    cur.execute("""
    CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
    RETURNS TABLE(
        name TEXT,
        email TEXT,
        phone TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        c.name::TEXT,
        c.email::TEXT,
        p.phone::TEXT
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$;
    """)
    conn.commit()
    print("✅ search_contacts function created")


# =========================
# MENU
# =========================
def menu():
    while True:
        print("""
1 Add contact
2 Import CSV
3 Filter by group
4 Search
5 Sort
6 Pagination
7 Export JSON
8 Import JSON
9 Add phone
10 Move group
0 Exit
""")

        c = input("Choose: ")

        if c == "1": add_contact()
        elif c == "2": import_csv()
        elif c == "3": filter_group()
        elif c == "4": search()
        elif c == "5": sort_contacts()
        elif c == "6": paginate()
        elif c == "7": export_json()
        elif c == "8": import_json()
        elif c == "9": add_phone_proc()
        elif c == "10": move_group_proc()
        elif c == "99": create_search_function()
        elif c == "0": break


if __name__ == "__main__":
    menu()
    cur.close()
    conn.close()