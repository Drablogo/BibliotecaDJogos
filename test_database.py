from database.database import create_database
from database.database import insert_game
from database.database import get_games


create_database()

insert_game("Super Mario World", "SNES", 1990)
insert_game("Sonic the Hedgehog", "Mega Drive", 1991)
insert_game("The Legend of Zelda", "NES", 1986)
insert_game("Castlevania", "NES", 1986)


games = get_games()

print(games)