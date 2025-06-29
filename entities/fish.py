import pygame
import random
import os
import sys
import config
import math
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
            if fish.is_off_screen():
                self.fishes.remove(fish)

    def spawn_wait(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.start_time > self.SPAWN_WAIT:
            self.spawn_fish()

    def scale_fishes(self):
        for fish in self.fishes:
            fish.scale()

    def spawn_fish(self):
        current_time = pygame.time.get_ticks()

        if len(self.fishes) <= 5:
            if current_time - self.last_spawn > self.spawn_delay:
                self.last_spawn = current_time
                self.spawn_delay = random.randint(0,1)
                fish = Fish(self.fish_images)
                self.fishes.append(fish)

    def get_screen(self, screen):
       self.screen = screen
       

class Fish:
    def __init__(self, fish_images):
        self.fish_images = fish_images
        self.image = self.random_image()
        self.size = self.random_size()
        self.scale()
        random_side = self.random_position()
        self.random_velocity(random_side)
        self.random_wobble()

    def random_image(self):
        image = random.choice(self.fish_images)
        return image
    
    def random_size(self):
        size = round(random.uniform(0.01, 0.18), 1)
        return size

    def random_position(self):
        random_side = random.choice(['random_x', 'random_y'])
        if random_side == 'random_x':
            self.x = random.randint((-self.width), (config.screen_width + self.width))
            self.y = random.choice([(self.height + config.screen_height), (0-self.height)])
        else:
            self.x = random.choice([(self.width + config.screen_width), (0-self.width)])
            self.y = random.randint((-self.height), (config.screen_height + self.height))
        print('x: ', self.x, '  y: ', self.y)
        return random_side

    def random_velocity(self, random_side):
        if random_side == 'random_x':
            angle = random.uniform(-math.pi/6, math.pi/6)  # -30 to 30 degrees
            speed = random.uniform(2, 4)
            self.dx = speed * math.sin(angle)
            self.dy = -speed if self.y > config.screen_height // 2 else speed
        else:
            angle = random.uniform(-math.pi/6, math.pi/6)
            speed = random.uniform(2, 4)
            self.dy = speed * math.sin(angle)
            self.dx = -speed if self.x > config.screen_width // 2 else speed

    def random_wobble(self):
        self.base_angle = math.atan2(self.dy, self.dx)

        self.wobble_timer = 0  # track time to animate
        self.wobble_speed = random.uniform(0.1, 1)  # how fast to wiggle
        self.wobble_amplitude = math.radians(10)

    def scale(self):
        scale_width = int(config.screen_width * self.size)
        aspect_ratio = self.image.get_height() / self.image.get_width()
        scale_height = int(scale_width * aspect_ratio)
        self.image = pygame.transform.scale(self.image, (scale_width, scale_height))

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update_pos(self):
        self.x += self.dx
        self.y += self.dy

    def update_wobble(self):
        self.x += self.dx
        self.y += self.dy
        self.wobble_timer += self.wobble_speed

        # Wobble angle (oscillates with time)
        self.wobble_angle = math.sin(self.wobble_timer) * self.wobble_amplitude
        self.total_angle = self.base_angle + self.wobble_angle

        self.wobble_image = pygame.transform.rotate(self.image, -math.degrees(self.total_angle))
        self.wobble_rect = self.wobble_image.get_rect(center=(self.x, self.y))

    def is_off_screen(self):
        return (
            self.x < -self.width or
            self.x > config.screen_width + self.width or
            self.y < -self.height or
            self.y > config.screen_height + self.height
        )

    def update(self, screen):
        self.update_pos()
        self.update_wobble()
        self.draw(screen)

    def draw(self, screen):
        #screen.blit(self.image, (self.x, self.y))
        screen.blit(self.wobble_image, self.wobble_rect)