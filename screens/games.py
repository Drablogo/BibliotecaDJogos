import pygame

from database.database import get_library_games


class GamesScreen:

    def __init__(self, screen, config):

        self.screen = screen
        self.config = config

        # ==========================================
        # LOGO
        # ==========================================

        self.logo = config.skin.LOGO

        self.logo_text = config.font.LOGO.render(
            "Game Library",
            True,
            "white"
        )

        # ==========================================
        # FONTES
        # ==========================================

        self.title_font = config.font.LOGO
        self.menu_font = config.font.SEARCH

        # ==========================================
        # TÍTULO
        # ==========================================

        self.title = self.title_font.render(
            "GAMES",
            True,
            "Dark green"
        )

        # ==========================================
        # POSIÇÃO DO LOGO
        # ==========================================

        self.logo_x = 84
        self.logo_y = 86

        self.logo_text_x = 173
        self.logo_text_y = 127

        # ==========================================
        # POSIÇÃO DO TÍTULO
        # ==========================================

        self.title_x = 960
        self.title_y = 165

        # ==========================================
        # LISTA
        # ==========================================

        self.list_x = 855
        self.list_y = 210
        self.list_spacing = 45

        # ==========================================
        # JOGOS DA BIBLIOTECA
        # ==========================================

        self.games = get_library_games()

        self.game_rects = []

        self.selected_game = None

        # ==========================================
        # BOTÃO BACK
        # ==========================================

        self.back_button = self.menu_font.render(
            "BACK",
            True,
            "gray"
        )

        self.back_button_rect = self.back_button.get_rect()

        self.back_button_rect.centerx = 960
        self.back_button_rect.y = 600

    # =================================================
    # DRAW
    # =================================================

    def draw(self):

        # ==========================================
        # PAINEL
        # ==========================================

        self.screen.blit(
            self.config.skin.ADD_PANEL,
            (810, 130)
        )

        # ==========================================
        # LOGO
        # ==========================================

        self.screen.blit(
            self.logo,
            (
                self.logo_x,
                self.logo_y
            )
        )

        self.screen.blit(
            self.logo_text,
            (
                self.logo_text_x,
                self.logo_text_y
            )
        )

        # ==========================================
        # TÍTULO
        # ==========================================

        title_rect = self.title.get_rect()

        title_rect.centerx = self.title_x
        title_rect.y = self.title_y

        self.screen.blit(
            self.title,
            title_rect
        )

        # ==========================================
        # LIMPA OS RETÂNGULOS
        # ==========================================

        self.game_rects = []

        mouse_pos = pygame.mouse.get_pos()

        # ==========================================
        # LISTA DE JOGOS
        # ==========================================

        for index, game in enumerate(self.games):

            (
                game_id,
                name,
                platform,
                year,
                cover,
                genre,
                developer,
                description
            ) = game

            y = (
                self.list_y
                + index * self.list_spacing
            )

            # ======================================
            # TEXTO
            # ======================================

            game_text = self.menu_font.render(
                name,
                True,
                "gray"
            )

            text_rect = game_text.get_rect()

            text_rect.x = self.list_x
            text_rect.y = y

            # ======================================
            # ÁREA CLICÁVEL
            # ======================================

            item_rect = text_rect.inflate(
                20,
                10
            )

            self.game_rects.append(
                (
                    item_rect,
                    game
                )
            )

            # ======================================
            # HOVER
            # ======================================

            if item_rect.collidepoint(
                mouse_pos
            ):

                game_text = self.menu_font.render(
                    name,
                    True,
                    (255, 220, 120)
                )

            # ======================================
            # DESENHA
            # ======================================

            self.screen.blit(
                game_text,
                text_rect
            )

        # ==========================================
        # BOTÃO BACK
        # ==========================================

        if self.back_button_rect.collidepoint(
            mouse_pos
        ):

            back_button = self.menu_font.render(
                "BACK",
                True,
                (255, 220, 120)
            )

        else:

            back_button = self.menu_font.render(
                "BACK",
                True,
                "gray"
            )

        self.screen.blit(
            back_button,
            self.back_button_rect
        )

    # =================================================
    # EVENTOS
    # =================================================

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                # ==================================
                # BACK
                # ==================================

                if self.back_button_rect.collidepoint(
                    mouse_pos
                ):

                    return "home"

                # ==================================
                # JOGOS
                # ==================================

                for rect, game in self.game_rects:

                    if rect.collidepoint(
                        mouse_pos
                    ):

                        self.selected_game = game

                        print(
                            "Jogo selecionado:",
                            game
                        )

                        return (
                            "game_details",
                            game
                        )

        return None