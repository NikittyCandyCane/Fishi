import config
import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core')))
import utils

class Menu:
    def __init__(self, menu_bg, moving_waves_frames, start_button_img, finish_button_img):
        self.menu_bg = menu_bg
        self.menu_bg_pos = (0,0)
        self.moving_waves = utils.Gif(moving_waves_frames, 300, -5, 100, 1.07)
        self.start_button = Button('start', start_button_img, 0.3)
        self.finish_button = Button('finish', finish_button_img, 0.3)
        self.trans_last_update = 0
        self.is_trans = False
        self.start_clicked_yet = False

    def update(self, screen):
        self.scale()
        return self.draw(screen)

    def scale(self):
        self.menu_bg = pygame.transform.scale(self.menu_bg, (config.screen_width, config.screen_height))

    def draw(self, screen):
        screen.blit(self.menu_bg, (self.menu_bg_pos))
        self.moving_waves.update(screen)
        self.start_button.update(screen)
        self.finish_button.update(screen)
        self.fade_mode = None
        if self.is_trans:
            return self.wave_transition(screen)

    def wave_transition(self, screen):
        state = self.fade.fade_handle(screen)
        if state == 'finished fading':
            self.is_trans = False
        elif state == 'finished both_1':
            return 'playing'
        

    def click(self, screen):
        if self.start_clicked_yet == False:
            if self.start_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.start_clicked_yet = True
                self.is_trans = True
                self.fade = utils.Fade(screen)
        if self.finish_button.rect.collidepoint(pygame.mouse.get_pos()):
            return 'quit'
        

class Button:
    def __init__(self, name, image, size):
        self.name = name
        self.image = image
        self.size = size

    def update(self, screen):
        self.find_pos()
        self.scale()
        self.draw(screen)

    def scale(self):
        scale_width = int(config.screen_width * self.size)
        aspect_ratio = self.image.get_height() / self.image.get_width()
        scale_height = int(scale_width * aspect_ratio)
        self.image = pygame.transform.scale(self.image, (scale_width, scale_height))

    def draw(self, screen):
        screen.blit(self.image, (self.pos))

    def find_pos(self):
        if self.name == 'start':
            self.rect = self.image.get_rect(center=(config.screen_width/2, config.screen_height/4))
        if self.name == 'finish':
            self.rect = self.image.get_rect(center=(config.screen_width/2, (config.screen_height/5)*3))
        self.pos = self.rect.topleft