import pygame

# pygame setup
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
FPS = pygame.time.Clock()

#COLOR
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (21, 255, 0)
CYAN = (0, 255, 205)
BLUE = (0, 75, 255)
PURPLE = (100, 0, 255)
PINK = (255, 0, 255)

running = True

#run project
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    SCREEN.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    FPS.tick(60)  # limits FPS to 60

pygame.quit()