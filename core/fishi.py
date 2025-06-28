# Import libraries
import pygame # type: ignore
import config
import sys
import random

# Initialize pygame and sound mixer
pygame.init()
pygame.mixer.init()

# Set up window
screen = pygame.display.set_mode((1200, 750))
