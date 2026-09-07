import sqlite3


DB_PATH = "database/games.db"


# =================================================
# CRIAR / ATUALIZAR BANCO
# =================================================

def create_database():

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            platform TEXT NOT NULL,
            year INTEGER,
            cover TEXT,
            genre TEXT,
            developer TEXT,
            description TEXT
        )
        """
    )

    # ==============================================
    # MIGRAÇÕES
    # ==============================================

    cursor.execute(
        "PRAGMA table_info(games)"
    )

    columns = [
        column[1]
        for column in cursor.fetchall()
    ]

    if "cover" not in columns:

        cursor.execute(
            """
            ALTER TABLE games
            ADD COLUMN cover TEXT
            """
        )

    if "genre" not in columns:

        cursor.execute(
            """
            ALTER TABLE games
            ADD COLUMN genre TEXT
            """
        )

    if "developer" not in columns:

        cursor.execute(
            """
            ALTER TABLE games
            ADD COLUMN developer TEXT
            """
        )

    if "description" not in columns:

        cursor.execute(
            """
            ALTER TABLE games
            ADD COLUMN description TEXT
            """
        )

    # ==============================================
    # USER GAMES
    # ==============================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user_games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id INTEGER UNIQUE,
            FOREIGN KEY (game_id)
            REFERENCES games(id)
        )
        """
    )

    connection.commit()
    connection.close()


# =================================================
# INSERIR JOGO
# =================================================

def insert_game(
    name,
    platform,
    year,
    cover,
    genre=None,
    developer=None,
    description=None
):

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO games (
            name,
            platform,
            year,
            cover,
            genre,
            developer,
            description
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            platform,
            year,
            cover,
            genre,
            developer,
            description
        )
    )

    connection.commit()
    connection.close()


# =================================================
# PEGAR TODOS OS JOGOS
# =================================================

def get_games():

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, platform, year
        FROM games
        ORDER BY name
        """
    )

    games = cursor.fetchall()

    connection.close()

    return games


# =================================================
# PEGAR UM JOGO PELO ID
# =================================================

def get_game_by_id(game_id):

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            name,
            platform,
            year,
            cover,
            genre,
            developer,
            description
        FROM games
        WHERE id = ?
        """,
        (game_id,)
    )

    game = cursor.fetchone()

    connection.close()

    return game


# =================================================
# ADICIONAR À BIBLIOTECA
# =================================================

def add_game_to_library(game_id):

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO user_games (game_id)
        VALUES (?)
        """,
        (game_id,)
    )

    connection.commit()
    connection.close()


# =================================================
# PEGAR JOGOS DA BIBLIOTECA
# =================================================

def get_library_games():

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            games.id,
            games.name,
            games.platform,
            games.year,
            games.cover,
            games.genre,
            games.developer,
            games.description
        FROM user_games
        JOIN games
            ON user_games.game_id = games.id
        ORDER BY games.name
        """
    )

    games = cursor.fetchall()

    connection.close()

    return games


# =================================================
# REMOVER DA BIBLIOTECA
# =================================================

def remove_game_from_library(game_id):

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM user_games
        WHERE game_id = ?
        """,
        (game_id,)
    )

    connection.commit()
    connection.close()


# =================================================
# ATUALIZAR CAPA
# =================================================

def update_game_cover(game_id, cover):

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE games
        SET cover = ?
        WHERE id = ?
        """,
        (cover, game_id)
    )

    connection.commit()
    connection.close()


# =================================================
# ATUALIZAR JOGO
# =================================================

def update_game(
    game_id,
    name,
    platform,
    year,
    cover,
    genre,
    developer,
    description
):

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE games
        SET
            name = ?,
            platform = ?,
            year = ?,
            cover = ?,
            genre = ?,
            developer = ?,
            description = ?
        WHERE id = ?
        """,
        (
            name,
            platform,
            year,
            cover,
            genre,
            developer,
            description,
            game_id
        )
    )

    connection.commit()
    connection.close()