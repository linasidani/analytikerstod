import sqlite3

DB = "app.db"


def get_connection():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS Person (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            notes TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS Organisation (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            country TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS Event (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            date TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS PersonOrganisation (
            person_id INTEGER,
            organisation_id INTEGER,
            role TEXT,
            PRIMARY KEY (person_id, organisation_id),
            FOREIGN KEY (person_id) REFERENCES Person(id),
            FOREIGN KEY (organisation_id) REFERENCES Organisation(id)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS PersonEvent (
            person_id INTEGER,
            event_id INTEGER,
            PRIMARY KEY (person_id, event_id),
            FOREIGN KEY (person_id) REFERENCES Person(id),
            FOREIGN KEY (event_id) REFERENCES Event(id)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS Log (
            id INTEGER PRIMARY KEY,
            what TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close() 
if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully!")

    def add_person(name,notes):
        conn = get_connection()

        cur = conn.execute(
            "INSERT INTO Person (name, notes) VALUES (?, ?) ",
            (name, notes)
        )

        new_id = cur.lastrowid

        conn.commit()
        conn.close()

        return new_id

    def find_people(q):
        conn = get_connection()

        rows = conn.execute(
             "SELECT * FROM Person WHERE name LIKE ?",
             (f"%{q}%",)
        ) .fetchall()

        conn.close()

        return rows

    def add_log(what):
        conn = get_connection()

        conn.execute(
            "INSERT INTO Log (what) VALUES (?)",
            (what,)
        )
        conn.commit()
        conn.close()

def find_organisations_for(person_id):
    conn = get_connection()

    rows = conn.execute("""
        SELECT Organisation.*
        FROM Organisation
        JOIN PersonOrganisation
            ON Organisation.id = PersonOrganisation.organisation_id
        WHERE PersonOrganisation.person_id = ?
    """, (person_id,)).fetchall()

    conn.close()

    return rows

if __name__ == "__main__":
    create_tables()

    add_person("Test Person", "Fictional test data")

    print([dict(row) for row in find_people("test")])
