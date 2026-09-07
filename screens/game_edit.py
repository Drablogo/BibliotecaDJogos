import pygame

from database.database import update_game


class GameEditScreen:

    def __init__(self, screen, config, game):

        self.screen = screen
        self.config = config

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
        # PAINEL
        # ==========================================

        self.panel_img = config.skin.ADD_PANEL

        self.panel_width = 500
        self.panel_height = 850

        self.panel_x = 710
        self.panel_y = 60

        # ==========================================
        # FONTES
        # ==========================================

        self.title_font = config.font.LOGO
        self.menu_font = config.font.SEARCH

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
            "EDIT GAME",
            True,
            "Dark green"
        )

        self.title_x = 960
        self.title_y = 95

        # ==========================================
        # CAMPOS
        # ==========================================

        self.fields = [

            {
                "label": "Name",
                "value": self.name or ""
            },

            {
                "label": "Platform",
                "value": self.platform or ""
            },

            {
                "label": "Year",
                "value": str(self.year or "")
            },

            {
                "label": "Genre",
                "value": self.genre or ""
            },

            {
                "label": "Developer",
                "value": self.developer or ""
            },

            {
                "label": "Cover",
                "value": self.cover or ""
            },

            {
                "label": "Description",
                "value": self.description or ""
            }

        ]

        self.active_field = 0

        self.field_rects = []

        self.description_field = 6

        # ==========================================
        # BOTÕES
        # ==========================================

        self.save_rect = pygame.Rect(
            875,
            820,
            80,
            35
        )

        self.cancel_rect = pygame.Rect(
            975,
            820,
            100,
            35
        )

        # ==========================================
        # CURSOR
        # ==========================================

        pygame.key.start_text_input()

    # =================================================
    # DRAW FIELD
    # =================================================

    def draw_field(
        self,
        label,
        value,
        index,
        x,
        y,
        width,
        height
    ):

        # ==========================================
        # LABEL
        # ==========================================

        label_text = self.menu_font.render(
            label,
            True,
            "gray"
        )

        self.screen.blit(
            label_text,
            (
                x,
                y
            )
        )

        # ==========================================
        # CAMPO
        # ==========================================

        field_rect = pygame.Rect(
            x,
            y + 22,
            width,
            height
        )

        self.field_rects.append(
            field_rect
        )

        if index == self.active_field:

            border_color = (
                255,
                220,
                120
            )

            text_color = "Dark green"

        else:

            border_color = "gray"

            text_color = "gray"

        pygame.draw.rect(
            self.screen,
            border_color,
            field_rect,
            2
        )

        # ==========================================
        # TEXTO
        # ==========================================

        text = self.menu_font.render(
            value,
            True,
            text_color
        )

        text_rect = text.get_rect()

        text_rect.x = field_rect.x + 8
        text_rect.centery = field_rect.centery

        self.screen.blit(
            text,
            text_rect
        )

    # =================================================
    # DRAW
    # =================================================

    def draw(self):

        self.field_rects = []

        # ==========================================
        # PAINEL
        # ==========================================

        panel = pygame.transform.scale(
            self.panel_img,
            (
                self.panel_width,
                self.panel_height
            )
        )

        self.screen.blit(
            panel,
            (
                self.panel_x,
                self.panel_y
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
        # CAMPOS
        # ==========================================

        x = 780
        width = 360

        self.draw_field(
            "Name",
            self.fields[0]["value"],
            0,
            x,
            160,
            width,
            35
        )

        self.draw_field(
            "Platform",
            self.fields[1]["value"],
            1,
            x,
            245,
            width,
            35
        )

        self.draw_field(
            "Year",
            self.fields[2]["value"],
            2,
            x,
            330,
            width,
            35
        )

        self.draw_field(
            "Genre",
            self.fields[3]["value"],
            3,
            x,
            415,
            width,
            35
        )

        self.draw_field(
            "Developer",
            self.fields[4]["value"],
            4,
            x,
            500,
            width,
            35
        )

        self.draw_field(
            "Cover",
            self.fields[5]["value"],
            5,
            x,
            585,
            width,
            35
        )

        self.draw_field(
            "Description",
            self.fields[6]["value"],
            6,
            x,
            670,
            width,
            55
        )

        # ==========================================
        # BOTÃO SAVE
        # ==========================================

        self.draw_button(
            "SAVE",
            self.save_rect
        )

        # ==========================================
        # BOTÃO CANCEL
        # ==========================================

        self.draw_button(
            "CANCEL",
            self.cancel_rect
        )

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
    # SALVAR
    # =================================================

    def save_game(self):

        name = self.fields[0]["value"].strip()
        platform = self.fields[1]["value"].strip()
        year_text = self.fields[2]["value"].strip()
        genre = self.fields[3]["value"].strip()
        developer = self.fields[4]["value"].strip()
        cover = self.fields[5]["value"].strip()
        description = self.fields[6]["value"].strip()

        # ==========================================
        # ANO
        # ==========================================

        if year_text:

            try:
                year = int(year_text)

            except ValueError:

                print(
                    "Ano inválido."
                )

                return None

        else:

            year = None

        # ==========================================
        # VALIDAÇÃO
        # ==========================================

        if not name:

            print(
                "O nome do jogo não pode ficar vazio."
            )

            return None

        if not platform:

            print(
                "A plataforma não pode ficar vazia."
            )

            return None

        # ==========================================
        # ATUALIZAR BANCO
        # ==========================================

        update_game(
            self.game_id,
            name,
            platform,
            year,
            cover,
            genre,
            developer,
            description
        )

        print(
            "Jogo atualizado:",
            name
        )

        return "game_updated"

    # =================================================
    # EVENTOS
    # =================================================

    def handle_event(self, event):

        # ==========================================
        # MOUSE
        # ==========================================

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                # ==================================
                # CAMPOS
                # ==================================

                for index, rect in enumerate(
                    self.field_rects
                ):

                    if rect.collidepoint(
                        mouse_pos
                    ):

                        self.active_field = index

                        return None

                # ==================================
                # SAVE
                # ==================================

                if self.save_rect.collidepoint(
                    mouse_pos
                ):

                    return self.save_game()

                # ==================================
                # CANCEL
                # ==================================

                if self.cancel_rect.collidepoint(
                    mouse_pos
                ):

                    return "cancel_edit"

        # ==========================================
        # TECLADO
        # ==========================================

        if event.type == pygame.KEYDOWN:

            field = self.fields[
                self.active_field
            ]

            # ======================================
            # BACKSPACE
            # ======================================

            if event.key == pygame.K_BACKSPACE:

                field["value"] = field[
                    "value"
                ][:-1]

            # ======================================
            # TAB
            # ======================================

            elif event.key == pygame.K_TAB:

                self.active_field = (
                    self.active_field + 1
                ) % len(self.fields)

            # ======================================
            # ENTER
            # ======================================

            elif event.key == pygame.K_RETURN:

                if (
                    self.active_field
                    == self.description_field
                ):

                    field["value"] += " "

            # ======================================
            # TEXTO
            # ======================================

            else:

                if event.unicode:

                    field["value"] += (
                        event.unicode
                    )

        return None