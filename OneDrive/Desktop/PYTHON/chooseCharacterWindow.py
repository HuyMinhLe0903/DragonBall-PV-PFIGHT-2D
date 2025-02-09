import pygame

def RunWindow():
    pygame.init()
    pygame.display.set_caption("Choose Character")
    WIDTH = 600
    HEIGHT = 400
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    FPS = pygame.time.Clock()
    RUNNING_WINDOW = True

    while RUNNING_WINDOW:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING_WINDOW = False
        SCREEN.fill((0,0,0))
        pygame.display.flip()
        FPS.tick(60)
    
    pygame.quit()
