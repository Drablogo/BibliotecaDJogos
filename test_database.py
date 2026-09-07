from database.database import create_database
from database.database import update_game_genre
from database.database import get_library_games


create_database()


update_game_genre(
    1,
    "Platform"
)

update_game_genre(
    2,
    "Platform"
)

update_game_genre(
    3,
    "Action-Adventure"
)

update_game_genre(
    4,
    "Action Platformer"
)


games = get_library_games()

print(games)