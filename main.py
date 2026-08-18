import pygame
import sys

import config
from config import font

from screens.home import HomeScreen

pygame.init()

screen = pygame.display.set_mode([config.window.WIDTH, config.window.HEIGHT])

home_screem = HomeScreen(screen, config)

pygame.display.set_caption(config.window.TITLE)

pygame.display.set_icon(config.window.ICON)


config.sound.BGM.play(loops=-1, fade_ms=500)

clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(config.skin.BG,(0, 0))

    home_screem.draw()

    pygame.display.update()

    clock.tick(60)

pygame.quit()