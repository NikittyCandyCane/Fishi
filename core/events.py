import pygame
import config
from . import window

def handle_events():
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                          return 'quit'
                    if event.key == pygame.K_TAB:
                                return 'toggle_fullscreen'
                    # other keydowns
    return False