import pygame

WIDTH = 800
HEIGHT = 500
SCREEN = None
FPS = pygame.time.Clock()
RUNNING_WINDOW = True

images = {
    "GokuBlueHair": "image/Characters/GokuBlueHair.png",
    "GokuRedHair": "image/Characters/GokuRedHair.png",
    "Background": "image/FightBG.png"
}

class GokuBlueHair:
    def __init__(self):
        self.gokuBlueHair = pygame.image.load(images["GokuBlueHair"])
        self.gokuBlueHair = pygame.transform.scale(self.gokuBlueHair,(80,100))
        self.x = 0
        self.y = 0
    def Draw(self):
        SCREEN.blit(self.gokuBlueHair,(self.x,self.y))
    def MoveRight(self):
        self.x += 5
    def MoveLeft(self):
        self.x -= 5
    def MoveUp(self):
        self.y -= 5
    def MoveDown(self):
        self.y += 5

class GokuRedHair:
    def __init__(self):
        self.gokuRedHair = pygame.image.load(images["GokuRedHair"])
        self.gokuRedHair = pygame.transform.scale(self.gokuRedHair,(100,100))
        self.x = 700
        self.y = 0
    def Draw(self):
        SCREEN.blit(self.gokuRedHair,(self.x,self.y))
    def MoveRight(self):
        self.x += 5
    def MoveLeft(self):
        self.x -= 5
    def MoveUp(self):
        self.y -= 5
    def MoveDown(self):
        self.y += 5

GOKU_BLUE_HAIR = GokuBlueHair()
GOKU_RED_HAIR = GokuRedHair()

background = pygame.image.load(images["Background"])
background = pygame.transform.scale(background,(800,500))

def RunWindow():
    global gokuBlueHair
    global gokuRedHair
    global background
    global WIDTH
    global HEIGHT
    global SCREEN
    global FPS
    global RUNNING_WINDOW

    pygame.init()
    pygame.display.set_caption("Fight")

    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

    while RUNNING_WINDOW:
        SCREEN.fill((0,0,0))
        SCREEN.blit(background,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING_WINDOW = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            GOKU_BLUE_HAIR.MoveRight()
        elif keys[pygame.K_a]:
            GOKU_BLUE_HAIR.MoveLeft()
        elif keys[pygame.K_w]:
            GOKU_BLUE_HAIR.MoveUp()
        elif keys[pygame.K_s]:
            GOKU_BLUE_HAIR.MoveDown()

        if keys[pygame.K_RIGHT]:
            GOKU_RED_HAIR.MoveRight()
        elif keys[pygame.K_LEFT]:
            GOKU_RED_HAIR.MoveLeft()
        elif keys[pygame.K_UP]:
            GOKU_RED_HAIR.MoveUp()
        elif keys[pygame.K_DOWN]:
            GOKU_RED_HAIR.MoveDown()

        GOKU_BLUE_HAIR.Draw()
        GOKU_RED_HAIR.Draw()

        pygame.display.flip()
        FPS.tick(60)
    
    pygame.quit()
