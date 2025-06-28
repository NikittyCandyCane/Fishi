# Import libraries
import pygame
import sys
import random

# I couldn't figure out how to cleanly import modules so I am just going to import them
from . import module
from . import window
from . import events
from . import utils
import config

# Set up window

def start():
    print('Game start!')
    pygame.init()
    pygame.mixer.init()
    #module.import_modules()

    screen = window.create_window()
    clock = pygame.time.Clock()
    running = True

    from . import resource_handler

    while running:
        event = events.handle_events()
        if event == 'quit':
            running = False
        elif event == 'toggle_fullscreen':
            toggle_fullscreen
        
        clock.tick(60)


    pygame.quit()
    print('Game quit!')
    sys.exit()

def toggle_fullscreen():
    if config.FULLSCREEN:
        config.FULLSCREEN = False
    else:
        config.FULLSCREEN = True
    window.create_window()