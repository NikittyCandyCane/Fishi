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
    mouse = Mouse()
    
    while running:
        event = events.handle_events()
        if event == 'quit':
            running = False
        elif event == 'toggle_fullscreen':
            toggle_fullscreen()
        
        screen_update(screen, clock, player, mouse)
    quit()

def toggle_fullscreen():
    if config.FULLSCREEN:
        config.FULLSCREEN = False
    else:
        config.FULLSCREEN = True
    screen = window.create_window()
    config.screen_width, config.screen_height = screen.get_size()
    return screen,

def quit():
    print('Game quit!')
    pygame.quit()
    sys.exit()

def screen_update(screen, clock, player, mouse):
    screen.fill(config.BLACK)
    mouse.update_position()
    draw(screen, player, mouse)
    clock.tick(60)
    pygame.display.flip()

def draw(screen, player, mouse):
    player.update(mouse, screen)

class Player:
    def __init__(self, goldfish):
        self.image_original = goldfish
        #self.i_width = self.image.get_width()
        #self.i_height = self.image.get_width()
        self.image = None
        self.width = None
        self.height = None
        self.rotation = 0
    
    def scale(self, mouse):
        scale_width = int(config.screen_width * 0.1)
        aspect_ratio = self.image_original.get_height() / self.image_original.get_width()
        scale_height = int(scale_width * aspect_ratio)
        self.image = pygame.transform.scale(self.image_original, (scale_width, scale_height))
        
        #self.x = config.screen_width/2
        #self.y = config.screen_height/2
        self.pos = (mouse.x, mouse.y)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def rotate(self, mouse):
        if mouse.x_displace > 0:
            if self.rotation < 0:
                self.rotation += 5
            elif self.rotation > 0:
                self.rotation -= 5
        elif mouse.x_displace < 0:
            if self.rotation < 180:
                self.rotation -= 5
            elif self.rotation > 180:
                self.rotation += 5

        self.image = pygame.transform.rotate(self.image, self.rotation)

    def draw(self, screen):
        screen.blit(self.image, (self.pos))

    def update(self, mouse, screen):
        self.scale(mouse)
        self.rotate(mouse)
        self.draw(screen)


class Mouse:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()

    def update_position(self):
        self.old_x, self.old_y = self.x, self.y
        self.x, self.y = pygame.mouse.get_pos()
        self.x_displace = self.x - self.old_x
        self.y_displace = self.y - self.old_y

        print('x displacement: ', self.x_displace)
        print('y displacement: ', self.y_displace)