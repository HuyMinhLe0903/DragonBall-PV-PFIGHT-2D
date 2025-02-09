import pygame
import multiprocessing
import settingWindow
import chooseCharacterWindow

backgroundList = {
    "1": "image/MenuBG1.png",
    "2": "image/MenuBG2.png",
    "3": "image/MenuBG3.png",
    "4": "image/MenuBG4.png"
}

functionUsing = ""

controller = 1
backgroundImage = backgroundList[str(controller)]

WIDTH = 600
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = pygame.time.Clock()
RUNNING_MAIN_WINDOW = True

SettingWindow = False
ChooseCharacterWindow = False

def UpdateController(direction):
    global controller
    if direction == "Up":
        if controller == 1:
            controller = controller
        else:
            controller -= 1
    elif direction == "Down":
        if controller == 4:
            controller = controller
        else:
            controller += 1

def DrawBackground():
    global controller
    global backgroundImage
    global backgroundList
    global WIDTH
    global HEIGHT
    global SCREEN

    backgroundImage = backgroundList[str(controller)]
    image = pygame.image.load(backgroundImage).convert()
    image = pygame.transform.scale(image,(WIDTH,HEIGHT))
    SCREEN.blit(image,(0,0))
    print(backgroundImage)

def UpdateFunctionUsing():
    global controller
    global functionUsing

    if controller == 1:
        functionUsing = ""
    elif controller == 2:
        functionUsing = "play"
    elif controller == 3:
        functionUsing = "setting"
    elif controller == 4:
        functionUsing = "exit"

def OnPressEnter():
    global functionUsing
    global RUNNING_MAIN_WINDOW
    global SettingWindow
    global ChooseCharacterWindow

    if functionUsing == "exit":
        RUNNING_MAIN_WINDOW = False
    elif functionUsing == "setting":
        windowProcess = multiprocessing.Process(target = settingWindow.RunSettingWindow)
        windowProcess.start()
        windowProcess.join()
    elif functionUsing == "play":
        windowProcess = multiprocessing.Process(target = chooseCharacterWindow.RunWindow)
        windowProcess.start()
        windowProcess.join()

def RunMainWindow():
    pygame.init()

    global controller
    global WIDTH
    global HEIGHT
    global SCREEN
    global FPS
    global RUNNING_MAIN_WINDOW

    pygame.display.set_caption("DragonBall PVP FIGHT 2D")

    while RUNNING_MAIN_WINDOW:
        SCREEN.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING_MAIN_WINDOW = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    UpdateController("Up")
                elif event.key == pygame.K_DOWN:
                    UpdateController("Down")
                elif event.key == pygame.K_RETURN:
                    OnPressEnter()
        
        DrawBackground()
        UpdateFunctionUsing()

        pygame.display.flip()
        FPS.tick(60)
    
    pygame.quit()