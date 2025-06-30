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
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'entities'))
import fish

# Set up window

def start():
    print('Game start!')
    pygame.init()
    pygame.mixer.init()

    screen = window.create_window()
    clock = pygame.time.Clock()
    running = True

    goldfish, catfish, angelfish, bass, trout, anchovy, clownfish, crab, pufferfish, surgeonfish, worm, rusty_can, menu_bg, ocean_bg_frames, moving_waves_frames, start_button, finish_button, title_music, ambience = resource_handler.load_resources()
    game, menu, player, mouse, ocean_bg = create_objects(goldfish, ocean_bg_frames, menu_bg, moving_waves_frames, start_button, finish_button)

    while running:
        event = events.handle_events()
        if event == 'quit':
            running = False
        elif event == 'toggle_fullscreen':
            toggle_fullscreen(game)
        elif event == 'mouse_click':
            mouse.click(game, menu, screen)

        game.screen_update(screen, menu, clock, player, mouse, ocean_bg, title_music, ambience)
    quit()


def create_objects(goldfish, ocean_bg_frames, menu_bg, moving_waves_frames, start_button_img, finish_button_img):
    game = Game()
    player = Player(goldfish)
    mouse = Mouse()
    ocean_bg = utils.Gif(ocean_bg_frames, 30, 0, 0)
    menu = menu_ui.Menu(menu_bg, moving_waves_frames, start_button_img, finish_button_img)
    return game, menu, player, mouse, ocean_bg


def toggle_fullscreen(game):
    if config.FULLSCREEN:
        config.FULLSCREEN = False
    else:
        config.FULLSCREEN = True
    screen = window.create_window()
    pygame.display.flip()
    config.screen_width, config.screen_height = screen.get_size()
    game.fish_handler.scale_fishes()
    return screen

def quit():
    print('Game quit!')
    pygame.quit()
    sys.exit()

class Game:
    def __init__(self):
        self.status = 'menu'
        self.is_first_menu_loop = True
        self.music_manager = Music_Manager()

    def screen_update(self, screen, menu, clock, player, mouse, ocean_bg, title_music, ambience):
        if self.status == 'menu':
            if self.screen_update_menu(screen, menu, title_music) is not None:
                self.status = 'playing'
        if self.status == 'playing':
            self.screen_update_playing(screen, player, mouse, ocean_bg, ambience)
        clock.tick(60)
        pygame.display.flip()
    
    def screen_update_menu(self, screen, menu, title_music):
        if self.is_first_menu_loop:
            self.music_manager.play(title_music)
            self.is_first_menu_loop = False

        self.is_first_play_loop = False
        screen.fill(config.BLACK)
        return menu.update(screen)

    def screen_update_playing(self, screen, player, mouse, ocean_bg, ambience):
        self.is_first_menu_loop = True
        if self.is_first_play_loop == False:
            self.music_manager.fadeout(100)
            self.music_manager.loop_sound(ambience)
            self.fish_handler = fish.Fish_Handler(screen)
            self.is_first_play_loop = True

        mouse.update_position()
        #draw
        ocean_bg.update(screen)
        self.fish_handler.get_screen(screen)
        self.fish_handler.run()
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

class Music_Manager:
    def __init__(self):
        self.current_track = None
        self.looping_channel = None

    def play(self, path, loop=-1):
        if self.current_track != path:
            pygame.mixer.music.load(path)
            self.current_track = path
            pygame.mixer.music.play(loop)

    def stop(self):
        pygame.mixer.music.stop()

    def fadeout(self, ms):
        pygame.mixer.music.fadeout(ms)

    def loop_sound(self, sound):
        if self.looping_channel is None or not self.looping_channel.get_busy():
            self.looping_channel = sound.play(loops=-1)

    def fadeout_sound(self, ms):
        if self.looping_channel and self.looping_channel.get_busy():
            self.looping_channel.fadeout(ms)
            self.looping_channel = None

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