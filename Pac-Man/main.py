import sys
import pygame
from pygame.locals import *
import time

pygame.init()

screen = pygame.display.set_mode((600, 600))
background = pygame.image.load("./image/mainScreen.jpg")
pygame.display.set_caption("PAC-MAN")

# Starting position
x, y = 435, 555
pacNow_Pos = [x, y]
pacNext_Pos = [x, y]
pacNext_Pos2rP = [0, 0]  # rP is roadPosition
pacOld_Move = [0, -10]
pacOld_Pos = [x, y]
pacOld_Pos2rP = [0, 0]  # rP is roadPosition
pacOld_Dir = 'le'

imgCount = 0
imgList = ['1', '2', '3', '1', '2']

# Red
redNow_pod = [445, 345]
redCheck_pod = [445, 345]
redCheck_pod2rP = [0, 0]  # rP is roadPosition

# bring data
with open('./data/roadPosition', 'r') as f:
    roadPosition = f.read()


# Manipulation
def pos(pacNext_XY, pacNext_Value, size_L, getDir):
    global pac_image
    global red_image
    global imgCount
    global pacOld_Dir

    while True:

        # -----------------------------pacman-------------------------------
        pacNext_Pos[pacNext_XY] = pacNow_Pos[pacNext_XY] + pacNext_Value
        pacNext_Pos[0] = pacNext_Pos[0] % size_L[2]
        pacNext_Pos[1] = pacNext_Pos[1] % size_L[3]

        pacNext_Pos2rP[0] = int((pacNext_Pos[0] - size_L[0]) / size_L[1])
        pacNext_Pos2rP[1] = int((pacNext_Pos[1] - size_L[0]) / size_L[1])

        pacOld_Pos[pacOld_Move[0]] = pacNow_Pos[pacOld_Move[0]] + pacOld_Move[1]
        pacOld_Pos[0] = pacOld_Pos[0] % size_L[2]
        pacOld_Pos[1] = pacOld_Pos[1] % size_L[3]
        pacOld_Pos2rP[0] = int((pacOld_Pos[0] - size_L[0]) / size_L[1])
        pacOld_Pos2rP[1] = int((pacOld_Pos[1] - size_L[0]) / size_L[1])

        time.sleep(0.08)

        if str(pacOld_Pos2rP) in roadPosition and str(pacNext_Pos2rP) not in roadPosition:

            screen.blit(background, (0, 0))
            pacNow_Pos[pacOld_Move[0]] = pacNow_Pos[pacOld_Move[0]] + pacOld_Move[1]

            pac_image = pygame.image.load("./image/pac_man" + size_L[4] + imgList[imgCount] + pacOld_Dir + ".png")
            if imgCount == 4:
                imgCount = 0
            else:
                imgCount += 1

            pacNext_Pos[0] = pacNow_Pos[0]
            pacNext_Pos[1] = pacNow_Pos[1]

        elif str(pacNext_Pos2rP) in roadPosition:

            screen.blit(background, (0, 0))
            pacNow_Pos[pacNext_XY] = pacNow_Pos[pacNext_XY] + pacNext_Value

            pacNow_Pos[0] = pacNow_Pos[0] % size_L[2]
            pacNow_Pos[1] = pacNow_Pos[1] % size_L[3]

            pac_image = pygame.image.load("./image/pac_man" + size_L[4] + imgList[imgCount] + getDir + ".png")
            pacOld_Dir = getDir
            if imgCount == 4:
                imgCount = 0
            else:
                imgCount += 1

            pacOld_Move[0] = pacNext_XY
            pacOld_Move[1] = pacNext_Value

            pacOld_Pos[0] = pacNow_Pos[0]
            pacOld_Pos[1] = pacNow_Pos[1]

        else:
            screen.blit(background, (0, 0))

            pacNext_Pos[0] = pacNow_Pos[0]
            pacNext_Pos[1] = pacNow_Pos[1]

            pacOld_Pos[0] = pacNow_Pos[0]
            pacOld_Pos[1] = pacNow_Pos[1]
        # -----------------------------pacman-----------------------------
        # -----------------------------red--------------------------------
        redCheck_pod2rP[0] = int((redNow_pod[0] - size_L[0]) / size_L[1])
        redCheck_pod2rP[1] = int((redNow_pod[1] - size_L[0]) / size_L[1])
        # -----------------------------red--------------------------------
        pac_rect = pac_image.get_rect()
        pac_rect.center = pacNow_Pos

        red_rect = red_image.get_rect()
        red_rect.center = redNow_pod

        screen.blit(red_image, red_rect)

        screen.blit(pac_image, pac_rect)
        pygame.display.update()

        for event2 in pygame.event.get():
            if event2.type == QUIT:
                pygame.quit()
                sys.exit
            if event2.type == KEYDOWN:
                if event2.key == K_LEFT:
                    pos(0, -size_L[1], size_L, 'le')
                elif event2.key == K_RIGHT:
                    pos(0, size_L[1], size_L, 'ri')
                elif event2.key == K_UP:
                    pos(1, -size_L[1], size_L, 'up')
                elif event2.key == K_DOWN:
                    pos(1, size_L[1], size_L, 'dw')


def main():
    global screen
    global background
    global pacNow_Pos
    global pac_image
    global pacNext_Pos
    global pacOld_Move
    global pacOld_Pos
    global red_image
    global redNow_pod
    global redCheck_pod

    # PAC-MAN画像の描画位置
    # 画像の描画を更新
    while True:
        pygame.display.update()
        screen.blit(background, (0, 0))

        for event2 in pygame.event.get():
            if event2.type == QUIT:
                pygame.quit()
                sys.exit
            if event2.type == KEYUP:
                if event2.key == ord('a'):

                    screen = pygame.display.set_mode((900, 990))  # ウィンドウの大きさ
                    background = pygame.image.load("./image/playScreen900.jpg")
                    pac_image = pygame.image.load("./image/pac_man900.png")  # 画像を読み込む
                    red_image = pygame.image.load("./image/Red900.png")

                    pac_rect = pac_image.get_rect()
                    pac_rect.center = pacNow_Pos

                    red_rect = red_image.get_rect()
                    red_rect.center = redNow_pod

                    screen.blit(background, (0, 0))
                    screen.blit(pac_image, pac_rect)
                    screen.blit(red_image, red_rect)
                    pygame.display.update()

                    sizeList = [5, 10, 900, 990, "900"]
                    time.sleep(2)
                    pos(pacOld_Move[0], pacOld_Move[1], sizeList, pacOld_Dir)

                elif event2.key == ord('b'):

                    screen = pygame.display.set_mode((540, 594))  # ウィンドウの大きさ
                    background = pygame.image.load("./image/playScreen600.jpg")
                    pac_image = pygame.image.load("./image/pac_man600.png")  # 画像を読み込む
                    red_image = pygame.image.load("./image/Red600.png")

                    pacNow_Pos = [261, 333]
                    pacNext_Pos = [261, 333]
                    pacOld_Move = [0, -6]
                    pacOld_Pos = [261, 333]
                    redNow_pod = [267, 207]
                    redCheck_pod = [267, 207]

                    pac_rect = pac_image.get_rect()
                    pac_rect.center = pacNow_Pos

                    red_rect = red_image.get_rect()
                    red_rect.center = redNow_pod

                    screen.blit(background, (0, 0))
                    screen.blit(pac_image, pac_rect)
                    screen.blit(red_image, red_rect)
                    pygame.display.update()

                    sizeList = [3, 6, 540, 594, "600"]
                    time.sleep(2)
                    pos(pacOld_Move[0], pacOld_Move[1], sizeList, pacOld_Dir)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()
