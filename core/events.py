import pygame

def handle_events():
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.keyp == pygame.K_ESCAPE:
                          return False
                    # other keydowns

    return True