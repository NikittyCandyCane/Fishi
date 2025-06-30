import pygame
import os
from paths import BASEDIR
from paths import IMAGES_DIR, SOUNDS_DIR

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

    #UI
    menu_bg = pygame.image.load(os.path.join(IMAGES_DIR, 'ui/menu_bg.jpg')).convert_alpha()
    start_button = pygame.image.load(os.path.join(IMAGES_DIR, 'ui/start_button.png')).convert_alpha()
    finish_button = pygame.image.load(os.path.join(IMAGES_DIR, 'ui/finish_button.png')).convert_alpha()
    moving_waves = []
    for i in range(0,9):
        i = f"{i:03}"
        img = pygame.transform.scale_by(pygame.image.load(os.path.join(IMAGES_DIR, f'ui/moving_waves/tile{i}.png')).convert_alpha(), 1)
        moving_waves.append(img)

    ocean_bg = []
    for i in range(0,100):
        i = f"{i:03}"
        img = pygame.transform.scale_by(pygame.image.load(os.path.join(IMAGES_DIR, f'ocean_bg/tile{i}.png')).convert_alpha(), 1)
        ocean_bg.append(img)

    title_music = os.path.join(SOUNDS_DIR, 'title.mp3')

    print('Resources loaded!')

    return goldfish, catfish, angelfish, bass, trout, anchovy, clownfish, crab, pufferfish, surgeonfish, worm, rusty_can, menu_bg, ocean_bg, moving_waves, start_button, finish_button, title_music