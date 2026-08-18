import pygame

pygame.init()
pygame.mixer.init()

class window:
    TITLE = "Game Library"
    WIDTH = 1920
    HEIGHT = 1080
    ICON = pygame.image.load("assets/icons/Logo.png")

class font:
    RETRO = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 14)
    MENU = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 14)
    LOGO = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 17)
    SEARCH = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 18)

class skin:
    BG = pygame.image.load("assets/background/background.png")
    PANEL = pygame.image.load("assets/ui/Panel.png")
    LOGO = pygame.image.load("assets/ui/Logo.png")
    SEARCHBAR = pygame.image.load("assets/ui/Searchbar.png")

    HOME_ICON = pygame.image.load("assets/icons/Home.png")
    ADD_ICON = pygame.image.load("assets/icons/Add.png")
    GAMES_ICON = pygame.image.load("assets/icons/Games.png")

class sound:
    BGM = pygame.mixer.Sound("sounds/Synth BGM.mp3")
    BGM.set_volume(0.1)