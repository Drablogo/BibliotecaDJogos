import pygame
import sys
import config

from database.database import (
    create_database,
    get_library_games,
    get_game_by_id
)

from screens.home import HomeScreen
from screens.add import AddScreen
from screens.games import GamesScreen
from screens.game_details import GameDetailsScreen
from screens.game_edit import GameEditScreen


# ==========================================
# INICIALIZAÇÃO
# ==========================================

pygame.init()


# ==========================================
# CRIA / ATUALIZA O BANCO
# ==========================================

create_database()


# ==========================================
# JANELA
# ==========================================

screen = pygame.display.set_mode(
    [
        config.window.WIDTH,
        config.window.HEIGHT
    ]
)

pygame.display.set_caption(
    config.window.TITLE
)

pygame.display.set_icon(
    config.window.ICON
)


# ==========================================
# CRIA AS TELAS
# ==========================================

home_screen = HomeScreen(
    screen,
    config
)

add_screen = AddScreen(
    screen,
    config
)

games_screen = GamesScreen(
    screen,
    config
)


# ==========================================
# TELA ATUAL
# ==========================================

current_screen = home_screen


# ==========================================
# MÚSICA
# ==========================================

config.sound.BGM.play(
    loops=-1,
    fade_ms=500
)


# ==========================================
# CLOCK
# ==========================================

clock = pygame.time.Clock()


# ==========================================
# LOOP PRINCIPAL
# ==========================================

while True:

    for event in pygame.event.get():

        # ==================================
        # FECHAR JANELA
        # ==================================

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        # ==================================
        # ESC - FECHAR PROGRAMA
        # ==================================

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                pygame.quit()
                sys.exit()

        # ==================================
        # EVENTO DA TELA ATUAL
        # ==================================

        action = current_screen.handle_event(event)

        # ==================================
        # HOME
        # ==================================

        if action == "home":

            current_screen = home_screen

        # ==================================
        # ADD
        # ==================================

        elif action == "add":

            current_screen = add_screen

        # ==================================
        # GAMES
        # ==================================

        elif action == "games":

            current_screen = games_screen

        # ==================================
        # GAME DETAILS
        # ==================================

        elif action and action[0] == "game_details":

            selected_game = action[1]

            current_screen = GameDetailsScreen(
                screen,
                config,
                selected_game
            )

        # ==================================
        # EDIT GAME
        # ==================================

        elif action and action[0] == "edit_game":

            selected_game = action[1]

            current_screen = GameEditScreen(
                screen,
                config,
                selected_game
            )

        # ==================================
        # GAME UPDATED
        # ==================================

        elif action == "game_updated":

            updated_game = get_game_by_id(
                current_screen.game_id
            )

            current_screen = GameDetailsScreen(
                screen,
                config,
                updated_game
            )

        # ==================================
        # CANCEL EDIT
        # ==================================

        elif action == "cancel_edit":

            game = get_game_by_id(
                current_screen.game_id
            )

            current_screen = GameDetailsScreen(
                screen,
                config,
                game
            )

        # ==================================
        # GAME REMOVED
        # ==================================

        elif action == "game_removed":

            games_screen.games = get_library_games()

            current_screen = games_screen

        # ==================================
        # BACK
        # ==================================

        elif action == "back":

            current_screen = games_screen

        # ==================================
        # GAME ADDED
        # ==================================

        elif action == "game_added":

            games_screen.games = get_library_games()

            current_screen = games_screen

    # ======================================
    # BACKGROUND
    # ======================================

    screen.blit(
        config.skin.BG,
        (0, 0)
    )

    # ======================================
    # DESENHA A TELA ATUAL
    # ======================================

    current_screen.draw()

    # ======================================
    # ATUALIZA A JANELA
    # ======================================

    pygame.display.update()

    # ======================================
    # FPS
    # ======================================

    clock.tick(60)


pygame.quit()