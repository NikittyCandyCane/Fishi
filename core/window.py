import pygame
import config

def create_window():
    if config.FULLSCREEN:
        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))

    screen_width, screen_height = screen.get_size()

    pygame.display.set_caption(config.TITLE)
    return screen