import pygame
import config

def create_window():
    if config.FULLSCREEN:
        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))

    pygame.display.set_caption(config.TITLE)
    return screen