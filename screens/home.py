import pygame
from config import *
from config import skin, font


class HomeScreen:
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config

        self.logo = config.skin.LOGO
        self.panel_img = config.skin.PANEL
        self.font = config.font.RETRO

        self.logo_text = config.font.LOGO.render("Game Library", True, "white")

        self.search_text = config.font.SEARCH.render("Search...", True, "white")

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

        self.logo_text_x = 173
        self.logo_text_y = 127

        panel_width = 306
        panel_height = 516

        panel_x = 810

        panel_y = 130

        self.panel = pygame.Rect(panel_x, panel_y, panel_width, panel_height)

        self.menu_x = self.panel.centerx
        self.menu_y = 250
        self.menu_spacing = 115

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()

        self.screen.blit(self.panel_img, self.panel) #desenhar painel

        self.screen.blit(self.logo,(self.logo_x, self.logo_y)) #desenhar logo

        self.screen.blit(self.logo_text,(self.logo_text_x, self.logo_text_y)) #desenhar texto da logo

        for index, item in enumerate(self.menu_items):
            y = self.menu_y + index * self.menu_spacing

            icon_rect = item["icon"].get_rect()

            icon_rect.centerx = self.menu_x
            icon_rect.y = y

            self.screen.blit(item["icon"], icon_rect)

            menu_text = self.menu_font.render(
                item["text"],
                True,
                "white"
            )

            text_rect = menu_text.get_rect()

            text_rect.centerx = self.menu_x
            text_rect.y = y + 55

            item_rect = icon_rect.union(text_rect)
            item_rect.inflate_ip(30, 15)

            item["rect"] = item_rect

            is_hovered = item["rect"].collidepoint(mouse_pos)

            if is_hovered:
                menu_text = self.menu_font.render(
                    item["text"],
                    True,
                    (255, 220, 120)
                )


            self.screen.blit(item["icon"], icon_rect)

            self.screen.blit(menu_text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                for item in self.menu_items:
                    if item["rect"].collidepoint(mouse_pos):

                        if item["text"] == "Add":
                            return "add"

