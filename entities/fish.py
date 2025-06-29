import pygame
import random
import os
import sys
import config
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
import resource_handler

class Fish_Handler:
    def __init__(self, screen):
       current_time = pygame.time.get_ticks()
       self.start_time = current_time
       self.SPAWN_WAIT = 5000
       self.spawn_delay = random.randint(0,1)
       self.last_spawn = current_time
       self.load_resources()
       self.fishes = []

    def load_resources(self):
        none, catfish, angelfish, bass, trout, anchovy, clownfish, crab, pufferfish, surgeonfish, worm, rusty_can, none, none, none, none, none = resource_handler.load_resources()
        self.fish_images = [catfish, angelfish, bass, trout, anchovy, clownfish, crab, pufferfish, surgeonfish]

    def run(self):
        self.spawn_wait()
        for fish in self.fishes:
            fish.update(self.screen)

    def spawn_wait(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.start_time > self.SPAWN_WAIT:
            self.spawn_fish()

    def spawn_fish(self):
        current_time = pygame.time.get_ticks()

        self.fish = []
        if len(self.fish) < 5:
            if current_time - self.last_spawn > self.spawn_delay:
                self.last_spawn = current_time
                self.spawn_delay = random.randint(0,1)
                self.fishes.append(Fish(self.fish_images))
                print(self.fishes)

    def get_screen(self, screen):
       self.screen = screen
       

class Fish:
    def __init__(self, fish_images):
        self.fish_images = fish_images
        self.image = self.random_image()
        self.size = self.random_size()

    def random_image(self):
        image = random.choice(self.fish_images)
        return image
    
    def random_size(self):
        size = round(random.uniform(0.1, 0.5), 1)
        return size

    def scale(self):
        scale_width = int(config.screen_width * self.size)
        aspect_ratio = self.image.get_height() / self.image.get_width()
        scale_height = int(scale_width * aspect_ratio)
        self.image = pygame.transform.scale(self.image, (scale_width, scale_height))
        
        self.x = 100
        self.y = 100

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update_rotation(self):
        pass
        # self.angle = -math.degrees(math.atan2(mouse.y_displace, mouse.x_displace))
        # self.image = pygame.transform.rotozoom(self.image, self.angle, 1)
        # rotated_rect = self.image.get_rect(center=(mouse.x, mouse.y))
        # self.pos = rotated_rect.topleft

    def update(self, screen):
        self.scale()
        self.update_rotation()
        self.draw(screen)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))