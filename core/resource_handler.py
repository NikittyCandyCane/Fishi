import pygame
import os
from paths import BASEDIR
from paths import IMAGES_DIR

def load_resources():
    # B - Fresh Water
    goldfish = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/B - Fresh Water/Goldfish.png')).convert_alpha()
    catfish = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/B - Fresh Water/Catfish.png')).convert_alpha()
    angelfish = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/B - Fresh Water/Angelfish.png')).convert_alpha()
    bass = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/B - Fresh Water/Bass.png')).convert_alpha()
    trout = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/B - Fresh Water/Rainbow Trout.png')).convert_alpha()

    # A - Salt Water
    anchovy = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/A - Salt Water/Anchovy.png')).convert_alpha()
    clownfish = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/A - Salt Water/Clownfish.png')).convert_alpha()
    crab = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/A - Salt Water/Crab - Dungeness.png')).convert_alpha()
    pufferfish = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/A - Salt Water/Pufferfish.png')).convert_alpha()
    surgeonfish = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/A - Salt Water/Surgeonfish.png')).convert_alpha()

    #C - Misc
    worm = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/C - Misc/Worm.png')).convert_alpha()
    rusty_can = pygame.image.load(os.path.join(IMAGES_DIR, 'Fish/C - Misc/Rusty Can.png')).convert_alpha()

    print('Resources loaded!')

    return goldfish, catfish, angelfish, bass, trout, anchovy, clownfish, crab, pufferfish, surgeonfish, worm, rusty_can
