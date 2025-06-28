# Import libraries
import pygame
import sys
import random

# I couldn't figure out how to cleanly import modules so I am just going to import them
#from . import module
from . import window
from . import events
from . import utils
#from . import resource_handler
import config
from . import resource_handler

# Set up window

def start():
    print('Game start!')
    pygame.init()
    pygame.mixer.init()

    screen = window.create_window()
    clock = pygame.time.Clock()
    running = True

    goldfish, catfish, angelfish, bass, trout, anchovy, clownfish, crab, pufferfish, surgeonfish, worm, rusty_can = resource_handler.load_resources()
    player = Player(goldfish)
    player.scale()
    
    while running:
        event = events.handle_events()
        if event == 'quit':
            running = False
        elif event == 'toggle_fullscreen':
            toggle_fullscreen()

        screen.fill(config.BLACK)
        player.draw(screen)
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
    print('Game quit!')
    sys.exit()

def toggle_fullscreen():
    if config.FULLSCREEN:
        config.FULLSCREEN = False
    else:
        config.FULLSCREEN = True
    screen = window.create_window()
    config.screen_width, config.screen_height = screen.get_size()
    return screen,

class Player:
    def __init__(self, goldfish):
        self.image_original = goldfish
        #self.i_width = self.image.get_width()
        #self.i_height = self.image.get_width()
        self.x = config.screen_width/2
        self.y = config.screen_height/2
        self.pos = (self.x, self.y)
        self.image = None
        self.width = None
        self.height = None
    
    def scale(self):
        self.image = pygame.transform.scale_by(self.image_original, config.screen_height*0.3)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, screen):
        self.scale()
        screen.blit(self.image, (self.pos))
