import pygame

from database.database import remove_game_from_library


class GameDetailsScreen:

    def __init__(self, screen, config, game):

        self.screen = screen
        self.config = config
        self.game = game

        self.panel_img = config.skin.ADD_PANEL

        self.title_font = config.font.LOGO
        self.menu_font = config.font.SEARCH

        # ==========================================
        # DADOS DO JOGO
        # ==========================================

        (
            self.game_id,
            self.name,
            self.platform,
            self.year,
            self.cover,
            self.genre,
            self.developer,
            self.description
        ) = game

        # ==========================================
        # LOGO
        # ==========================================

        self.logo = config.skin.LOGO

        self.logo_x = 84
        self.logo_y = 86

        self.logo_text = config.font.LOGO.render(
            "Game Library",
            True,
            "white"
        )

        self.logo_text_x = 173
        self.logo_text_y = 127

        # ==========================================
        # TÍTULO
        # ==========================================

        self.title = self.title_font.render(
            "GAME DETAILS",
            True,
            "Dark green"
        )

        self.title_x = 960
        self.title_y = 125

        # ==========================================
        # CAPA
        # ==========================================

        self.cover_image = None

        self.cover_max_width = 160
        self.cover_max_height = 190

        self.cover_y = 175

        self.load_cover()

        # ==========================================
        # BOTÕES
        # ==========================================

        self.edit_rect = pygame.Rect(
            875,
            610,
            70,
            30
        )

        self.remove_rect = pygame.Rect(
            975,
            610,
            90,
            30
        )

        self.back_rect = pygame.Rect(
            925,
            635,
            70,
            30
        )

    # =================================================
    # CARREGAR CAPA
    # =================================================

    def load_cover(self):

        if not self.cover:
            return

        try:

            image = pygame.image.load(
                self.cover
            ).convert_alpha()

            original_width, original_height = (
                image.get_size()
            )

            scale = min(
                self.cover_max_width / original_width,
                self.cover_max_height / original_height
            )

            new_width = int(
                original_width * scale
            )

            new_height = int(
                original_height * scale
            )

            self.cover_image = pygame.transform.scale(
                image,
                (
                    new_width,
                    new_height
                )
            )

        except pygame.error as error:

            print(
                "Erro ao carregar capa:",
                error
            )

    # =================================================
    # QUEBRA DE TEXTO
    # =================================================

    def wrap_text(self, text, max_width):

        if not text:
            return []

        words = text.split()

        lines = []
        current_line = ""

        for word in words:

            test_line = current_line

            if test_line:
                test_line += " "

            test_line += word

            text_width = self.menu_font.size(
                test_line
            )[0]

            if text_width <= max_width:

                current_line = test_line

            else:

                if current_line:
                    lines.append(
                        current_line
                    )

                current_line = word

        if current_line:
            lines.append(
                current_line
            )

        return lines

    # =================================================
    # BOTÃO
    # =================================================

    def draw_button(self, text, rect):

        mouse_pos = pygame.mouse.get_pos()

        if rect.collidepoint(mouse_pos):

            color = (
                255,
                220,
                120
            )

        else:

            color = "gray"

        button_text = self.menu_font.render(
            text,
            True,
            color
        )

        button_rect = button_text.get_rect()

        button_rect.center = rect.center

        self.screen.blit(
            button_text,
            button_rect
        )

    # =================================================
    # DRAW
    # =================================================

    def draw(self):

        # ==========================================
        # PAINEL
        # ==========================================

        panel = pygame.transform.scale(
            self.panel_img,
            (
                360,
                600
            )
        )

        self.screen.blit(
            panel,
            (
                780,
                90
            )
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
        # CAPA
        # ==========================================

        if self.cover_image:

            cover_rect = self.cover_image.get_rect()

            cover_rect.centerx = 960
            cover_rect.y = self.cover_y

            self.screen.blit(
                self.cover_image,
                cover_rect
            )

        # ==========================================
        # NOME
        # ==========================================

        name_text = self.menu_font.render(
            self.name,
            True,
            "Dark green"
        )

        name_rect = name_text.get_rect()

        name_rect.centerx = 960
        name_rect.y = 380

        self.screen.blit(
            name_text,
            name_rect
        )

        # ==========================================
        # PLATAFORMA
        # ==========================================

        platform_text = self.menu_font.render(
            f"Platform: {self.platform}",
            True,
            "gray"
        )

        platform_rect = platform_text.get_rect()

        platform_rect.centerx = 960
        platform_rect.y = 415

        self.screen.blit(
            platform_text,
            platform_rect
        )

        # ==========================================
        # ANO
        # ==========================================

        year_text = self.menu_font.render(
            f"Year: {self.year}",
            True,
            "gray"
        )

        year_rect = year_text.get_rect()

        year_rect.centerx = 960
        year_rect.y = 440

        self.screen.blit(
            year_text,
            year_rect
        )

        # ==========================================
        # GÊNERO
        # ==========================================

        if self.genre:

            genre_text = self.menu_font.render(
                f"Genre: {self.genre}",
                True,
                "gray"
            )

            genre_rect = genre_text.get_rect()

            genre_rect.centerx = 960
            genre_rect.y = 465

            self.screen.blit(
                genre_text,
                genre_rect
            )

        # ==========================================
        # DESENVOLVEDORA
        # ==========================================

        if self.developer:

            developer_text = self.menu_font.render(
                f"Developer: {self.developer}",
                True,
                "gray"
            )

            developer_rect = developer_text.get_rect()

            developer_rect.centerx = 960
            developer_rect.y = 490

            self.screen.blit(
                developer_text,
                developer_rect
            )

        # ==========================================
        # DESCRIÇÃO
        # ==========================================

        if self.description:

            description_lines = self.wrap_text(
                self.description,
                300
            )

            description_y = 520

            for line in description_lines:

                description_text = self.menu_font.render(
                    line,
                    True,
                    "gray"
                )

                description_rect = (
                    description_text.get_rect()
                )

                description_rect.centerx = 960
                description_rect.y = description_y

                self.screen.blit(
                    description_text,
                    description_rect
                )

                description_y += 20

        # ==========================================
        # EDIT
        # ==========================================

        self.draw_button(
            "EDIT",
            self.edit_rect
        )

        # ==========================================
        # REMOVE
        # ==========================================

        self.draw_button(
            "REMOVE",
            self.remove_rect
        )

        # ==========================================
        # BACK
        # ==========================================

        self.draw_button(
            "BACK",
            self.back_rect
        )

    # =================================================
    # EVENTOS
    # =================================================

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                # ==================================
                # EDIT
                # ==================================

                if self.edit_rect.collidepoint(
                    mouse_pos
                ):

                    return (
                        "edit_game",
                        self.game
                    )

                # ==================================
                # REMOVE
                # ==================================

                if self.remove_rect.collidepoint(
                    mouse_pos
                ):

                    remove_game_from_library(
                        self.game_id
                    )

                    print(
                        "Jogo removido da biblioteca:",
                        self.name
                    )

                    return "game_removed"

                # ==================================
                # BACK
                # ==================================

                if self.back_rect.collidepoint(
                    mouse_pos
                ):

                    return "back"

        return None