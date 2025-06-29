import pygame
import config

class Gif:
    def __init__(self, frames, delay, x, y, size=None):
        self.frames = frames
        self.delay = delay
        self.last_update = 0
        self.index = 0
        self.x = x
        self.y = y
        self.size = size
        if self.size == None:
            self.is_bg = True
        else:
            self.is_bg = False

    def update_animation(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >= self.delay:
            self.last_update = current_time
            self.index = (self.index + 1) % len(self.frames)
    
    def scale(self):
        if self.is_bg:
            self.frames[self.index] = pygame.transform.scale(self.frames[self.index], (config.screen_width, config.screen_height))
        else:
            scale_width = int(config.screen_width * self.size)
            aspect_ratio = self.frames[self.index].get_height() / self.frames[self.index].get_width()
            scale_height = int(scale_width * aspect_ratio)
            self.frames[self.index] = pygame.transform.scale(self.frames[self.index], (scale_width, scale_height))

    def draw(self, screen):
        screen.blit(self.frames[self.index], (self.x, self.y))

    def update(self, screen):
        self.update_animation()
        self.scale()
        self.draw(screen)
    
def fade_out(screen, delay, last_update, speed=5):
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((config.BLACK))
    current_time = pygame.time.get_ticks()

    if current_time - last_update >= delay:
            last_update = current_time
            alpha -= 1
            fade_surface.set_alpha(alpha)

    screen.blit(fade_surface, (0,0))

class Fade:
    def __init__(self, screen, mode='both_1'):
        self.fade_surface = pygame.Surface(screen.get_size())
        self.fade_surface.fill((config.BLACK))
        self.delay = 1
        self.last_update = 0
        self.mode = mode
        if mode == 'both_1' or mode == 'out':
            self.alpha = 0
        else:
            self.alpha = 255

    def fade_handle(self, screen):
        if self.mode == 'both_1':
            self.fade_out(screen)
            if self.alpha >= 255:
                    self.mode = 'both_2'
                    return 'finished both_1'
        elif self.mode == 'both_2':
             self.fade_in(screen)
             if self.alpha <= 0:
                return 'finished fading'
        elif self.mode == 'out':
            self.fade_out(screen)
        else:
            self.fade_in(screen)

    def fade_out(self, screen):
        self.fade_surface = pygame.Surface(screen.get_size())
        self.fade_surface.fill((config.BLACK))
        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >= self.delay:
                self.last_update = current_time
                self.alpha += 20
                self.fade_surface.set_alpha(self.alpha)

        self.draw(screen)

    def fade_in(self, screen):
        self.fade_surface = pygame.Surface(screen.get_size())
        self.fade_surface.fill((config.BLACK))
        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >= self.delay:
                self.last_update = current_time
                self.alpha -= 20
                self.fade_surface.set_alpha(self.alpha)
        self.draw(screen)

    def draw(self, screen):    
        screen.blit(self.fade_surface, (0,0))