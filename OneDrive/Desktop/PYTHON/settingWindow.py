import pygame

def RunSettingWindow():
    pygame.init()
    pygame.display.set_caption("Setting")
    WIDTH = 600
    HEIGHT = 400
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    FPS = pygame.time.Clock()
    RUNNING_SETTING_WINDOW = True

    while RUNNING_SETTING_WINDOW:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING_SETTING_WINDOW = False
        SCREEN.fill((0,0,0))
        pygame.display.flip()
        FPS.tick(60)
    
    pygame.quit()