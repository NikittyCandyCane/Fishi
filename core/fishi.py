# Import libraries
import pygame
import sys
import random
import math

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

    goldfish, catfish, angelfish, bass, trout, anchovy, clownfish, crab, pufferfish, surgeonfish, worm, rusty_can, menu_bg, ocean_bg_frames = resource_handler.load_resources()
    player, mouse, ocean_bg = create_objects(goldfish, ocean_bg_frames)

    while running:
        event = events.handle_events()
        if event == 'quit':
            running = False
        elif event == 'toggle_fullscreen':
            toggle_fullscreen()
        
        screen_update(screen, clock, player, mouse, ocean_bg)
    quit()

def create_objects(goldfish, ocean_bg_frames):
    player = Player(goldfish)
    mouse = Mouse()
    ocean_bg = Gif(ocean_bg_frames, 30, (0,0))
    return player, mouse, ocean_bg


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

def screen_update(screen, clock, player, mouse, ocean_bg):
    screen.fill(config.BLACK)
    mouse.update_position()
    draw(screen, player, mouse, ocean_bg)
    clock.tick(60)
    pygame.display.flip()

def draw(screen, player, mouse, ocean_bg):
    ocean_bg.update(screen)
    player.update(mouse, screen)

class Gif:
    def __init__(self, frames, delay, pos):
        self.frames = frames
        self.delay = delay
        self.last_update = 0
        self.index = 0
        self.pos = pos

    def update_animation(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >= self.delay:
            self.last_update = current_time
            self.index = (self.index + 1) % len(self.frames)
    
    def scale(self):
        scale_width = int(config.screen_width * 1.2)
        aspect_ratio = self.frames[self.index].get_height() / self.frames[self.index].get_width()
        scale_height = int(scale_width * aspect_ratio)
        self.frames[self.index] = pygame.transform.scale(self.frames[self.index], (scale_width, scale_height))

    def draw(self, screen):
        screen.blit(self.frames[self.index], self.pos)

    def update(self, screen):
        self.update_animation()
        self.scale()
        self.draw(screen)

class Player:
    def __init__(self, goldfish):
        self.image_original = goldfish
        #self.i_width = self.image.get_width()
        #self.i_height = self.image.get_width()
        self.image = None
        self.width = None
        self.height = None
        self.angle = 0
    
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

    def update_rotation(self, mouse):
        
        # if mouse.x_displace > 0:
        #     if self.rotation < 0:
        #         self.rotation += 5
        #     elif self.rotation > 0:
        #         self.rotation -= 5
        # elif mouse.x_displace < 0:
        #     if self.rotation < 180:
        #         self.rotation -= 5
        #     elif self.rotation > 180:
        #         self.rotation += 5

        if mouse.x_displace**2 + mouse.y_displace**2 > 1:
            self.angle = -math.degrees(math.atan2(mouse.y_displace, mouse.x_displace))
        self.image = pygame.transform.rotozoom(self.image, self.angle, 1)
        rotated_rect = self.image.get_rect(center=(mouse.x, mouse.y))
        self.pos = rotated_rect.topleft

        #self.image = pygame.transform.rotate(self.image, self.rotation)

    def draw(self, screen):
        screen.blit(self.image, (self.pos))

    def update(self, mouse, screen):
        self.scale(mouse)
        self.update_rotation(mouse)
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