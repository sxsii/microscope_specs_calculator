import sqlite3

DB_NAME = "microscope.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            measured_size REAL NOT NULL,
            microscope_type TEXT NOT NULL,
            magnification INTEGER NOT NULL,
            real_size REAL NOT NULL,
            output_unit TEXT NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()


def save_record(
    username,
    measured_size,
    microscope_type,
    magnification,
    real_size,
    output_unit
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO calculations (
            username,
            measured_size,
            microscope_type,
            magnification,
            real_size,
            output_unit
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            username,
            measured_size,
            microscope_type,
            magnification,
            real_size,
            output_unit
        )
    )

    conn.commit()
    conn.close()


def get_records():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM calculations")

    records = cursor.fetchall()

    conn.close()

    return records