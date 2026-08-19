import pygame
import sys
import config

from screens.home import HomeScreen
from screens.add import AddScreen

pygame.init()

screen = pygame.display.set_mode([config.window.WIDTH, config.window.HEIGHT])

home_screen = HomeScreen(screen, config)

add_screen = AddScreen(screen, config)

current_screen = home_screen

pygame.display.set_caption(config.window.TITLE)

pygame.display.set_icon(config.window.ICON)


config.sound.BGM.play(loops=-1, fade_ms=500)

clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        action = current_screen.handle_event(event)

        if action == "add":
            current_screen = add_screen

    screen.blit(config.skin.BG,(0, 0))

    current_screen.draw()

    pygame.display.update()

    clock.tick(60)

pygame.quit()