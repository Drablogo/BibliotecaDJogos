import sqlite3


DATABASE = "database/games.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def create_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            platform TEXT,
            year INTEGER
        )
    """)

    connection.commit()
    connection.close()


def insert_game(name, platform, year):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM games
        WHERE name = ? AND platform = ?
    """, (name, platform))

    existing_game = cursor.fetchone()

    if existing_game is None:

        cursor.execute("""
            INSERT INTO games (name, platform, year)
            VALUES (?, ?, ?)
        """, (name, platform, year))

    connection.commit()
    connection.close()


def get_games():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, platform, year
        FROM games
    """)

    games = cursor.fetchall()

    connection.close()

    return games