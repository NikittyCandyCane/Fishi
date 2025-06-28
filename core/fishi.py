# Import libraries
import pygame
import sys
import random
import math
import os

# I couldn't figure out how to cleanly import modules so I am just going to import them
#from . import module
from . import window
from . import events
from . import utils
#from . import resource_handler
import config
from . import resource_handler

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ui'))
import menu_ui

# Set up window

def start():
    print('Game start!')
    pygame.init()
    pygame.mixer.init()

    screen = window.create_window()
    clock = pygame.time.Clock()
    running = True

    goldfish, catfish, angelfish, bass, trout, anchovy, clownfish, crab, pufferfish, surgeonfish, worm, rusty_can, menu_bg, ocean_bg_frames, moving_waves_frames, start_button, finish_button = resource_handler.load_resources()
    game, menu, player, mouse, ocean_bg = create_objects(goldfish, ocean_bg_frames, menu_bg, moving_waves_frames, start_button, finish_button)

    while running:
        event = events.handle_events()
        if event == 'quit':
            running = False
        elif event == 'toggle_fullscreen':
            toggle_fullscreen()
        elif event == 'mouse_click':
            mouse.click(game, menu, screen)
        
        game.screen_update(screen, menu, clock, player, mouse, ocean_bg)
    quit()


def create_objects(goldfish, ocean_bg_frames, menu_bg, moving_waves_frames, start_button_img, finish_button_img):
    game = Game()
    player = Player(goldfish)
    mouse = Mouse()
    ocean_bg = utils.Gif(ocean_bg_frames, 30, 0, 0)
    menu = menu_ui.Menu(menu_bg, moving_waves_frames, start_button_img, finish_button_img)
    return game, menu, player, mouse, ocean_bg


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

class Game:
    def __init__(self):
        self.status = 'menu'

    def screen_update(self, screen, menu, clock, player, mouse, ocean_bg):
        if self.status == 'menu':
            self.screen_update_menu(screen, menu)
        if self.status == 'playing':
            self.screen_update_playing(screen, player, mouse, ocean_bg)
        clock.tick(60)
        pygame.display.flip()
    
    def screen_update_menu(self, screen, menu):
        screen.fill(config.BLACK)
        menu.update(screen)

    def screen_update_playing(self, screen, player, mouse, ocean_bg):
        screen.fill(config.BLACK)
        mouse.update_position()
        #draw
        ocean_bg.update(screen)
        player.update(mouse, screen)

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
        
        self.pos = (mouse.x, mouse.y)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update_rotation(self, mouse):
        
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

    def click(self, game, menu, screen):
        if game.status == 'menu':
            action = menu.click(screen)
            if action == 'quit':
                quit()