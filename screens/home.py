import pygame
from config import *
from config import skin, font


class HomeScreen:
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config

        self.logo = config.skin.LOGO
        self.panel_img = config.skin.PANEL
        self.search_bar = config.skin.SEARCHBAR
        self.font = config.font.RETRO

        self.logo_text = config.font.LOGO.render(
            "Game Library",
            True,
            "white"
        )
        self.search_text = config.font.SEARCH.render(
            "Search...",
            True,
            "white"
        )

        self.menu_font = config.font.MENU

        self.menu_items = [
            {
                "icon": config.skin.HOME_ICON,
                "text": "Home",
            },

            {
                "icon": config.skin.ADD_ICON,
                "text": "Add",
            },

            {
                "icon": config.skin.GAMES_ICON,
                "text": "Games",
            },
        ]

        self.logo_x = 84
        self.logo_y = 86

        self.search_bar_x = 1484
        self.search_bar_y = 86

        self.logo_text_x = 173
        self.logo_text_y = 127

        self.search_text_x = 1564
        self.search_text_y = 122

        panel_width = 306
        panel_height = 516

        panel_x = 810

        panel_y = 130

        self.panel = pygame.Rect(panel_x, panel_y, panel_width, panel_height)

        self.menu_x = self.panel.centerx
        self.menu_y = 250
        self.menu_spacing = 115

        """
        self.panel_img = pygame.transform.scale(
            self.panel_img,
            (panel_width, panel_height)
        )
        """

    def draw(self):
        self.screen.blit(
            self.panel_img,
            self.panel
        )

        self.screen.blit(
            self.logo,
            (self.logo_x, self.logo_y)
        )

        self.screen.blit(
            self.search_bar,
            (self.search_bar_x, self.search_bar_y)
        )

        self.screen.blit(
            self.logo_text,
            (self.logo_text_x, self.logo_text_y)
        )

        self.screen.blit(
            self.search_text,
            (self.search_text_x, self.search_text_y)
        )

        for index, item in enumerate(self.menu_items):
            y = self.menu_y + index * self.menu_spacing

            icon_rect = item["icon"].get_rect()

            icon_rect.centerx = self.menu_x
            icon_rect.y = y

            self.screen.blit(
                item["icon"],
                icon_rect
            )

            menu_text = self.menu_font.render(
                item["text"],
                True,
                "white"
            )

            text_rect = menu_text.get_rect()
            text_rect.centerx = self.menu_x
            text_rect.y = y + 55

            self.screen.blit(
                menu_text,
                text_rect
            )