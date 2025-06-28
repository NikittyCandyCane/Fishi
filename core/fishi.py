# Import libraries
import pygame
import config
import sys
import random

# I couldn't figure out how to cleanly import modules so I am just going to import them
from . import module
from . import window
from . import events
from . import utils

# Set up window

def start():
    print('Game start!')
    pygame.init()
    pygame.mixer.init()
    #module.import_modules()

    screen = window.create_window()
    clock = pygame.time.Clock()
    running = True

    while running:
        running = events.handle_events()

    pygame.quit()
    sys.exit()

        