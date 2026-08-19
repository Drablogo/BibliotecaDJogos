import pygame

from config import font
from database.database import get_games


class AddScreen:
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config

        self.title_font = config.font.LOGO
        self.menu_font = config.font.SEARCH

        self.panel_img = config.skin.ADD_PANEL

        self.title = self.title_font.render(
            "ADD GAME",
            True,
            "Dark green"
        )

        self.title_x = 960
        self.title_y = 165

        self.games = get_games()

        self.selected_game = None

        self.list_x = 855
        self.list_y = 210
        self.list_spacing = 45

        self.game_rects = []

        self.add_button = self.menu_font.render(
            "ADD",
            True,
            "Dark green"
        )

        self.add_button_rect = self.add_button.get_rect()
        self.add_button_rect.centerx = 960
        self.add_button_rect.y = 400

    def draw(self):
        self.screen.blit(
            self.panel_img,
            (810, 130)
        )

        title_rect = self.title.get_rect()
        title_rect.centerx = self.title_x
        title_rect.y = self.title_y

        self.screen.blit(
            self.title,
            title_rect
        )

        self.game_rects = []

        mouse_pos = pygame.mouse.get_pos()

        for index, game in enumerate(self.games):

            game_id, name, platform, year = game

            y = self.list_y + index * self.list_spacing

            game_text = self.menu_font.render(
                name,
                True,
                "gray"
            )

            text_rect = game_text.get_rect()
            text_rect.x = self.list_x
            text_rect.y = y

            item_rect = text_rect.inflate(20, 10)

            self.game_rects.append(
                (item_rect, game)
            )

            if self.selected_game == game:
                game_text = self.menu_font.render(
                    name,
                    True,
                    "Dark green"
                )

            elif item_rect.collidepoint(mouse_pos):
                game_text = self.menu_font.render(
                    name,
                    True,
                    (255, 220, 120)
                )

            self.screen.blit(
                game_text,
                text_rect
            )
            self.screen.blit(
            self.add_button,
            self.add_button_rect
            )

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                for rect, game in self.game_rects:

                    if rect.collidepoint(mouse_pos):
                        self.selected_game = game

                        print("Jogo selecionado:", game)

                        return "game_selected"

                if self.add_button_rect.collidepoint(mouse_pos):

                    if self.selected_game is not None:
                        print("Adicionando jogo:", self.selected_game)

                        return "game_added"