import pygame
import config

class Gif:
    def __init__(self, frames, delay, pos, size=None):
        self.frames = frames
        self.delay = delay
        self.last_update = 0
        self.index = 0
        self.pos = pos
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
        screen.blit(self.frames[self.index], self.pos)

    def update(self, screen):
        self.update_animation()
        self.scale()
        self.draw(screen)