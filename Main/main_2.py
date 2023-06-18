import pygame
import random
import sys
from pygame.locals import *


FPS = 32
SCREEENWIDTH = 400
SCREEENHEIGHT = 512
screen = pygame.display.set_mode((SCREEENWIDTH,SCREEENHEIGHT))
GROUNDY = SCREEENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
BG = 'bg.jpeg'
pipe = 'pipe1.jpeg'

#Image Processing
PLAYER = pygame.image.load('bird.png')
PLAYER = pygame.transform.scale(PLAYER,(70,70))
BASE = pygame.image.load('base.png')
BASE = pygame.transform.scale(BASE,(500,250))
#Score Image Processing
ZERO = pygame.image.load('0.png')
ZERO = pygame.transform.scale(ZERO,(40,60))
ONE = pygame.image.load('1.png')
ONE = pygame.transform.scale(ONE,(40,60))
TWO = pygame.image.load('2.png')
TWO = pygame.transform.scale(TWO,(40,60))
THREE = pygame.image.load('3.png')
THREE = pygame.transform.scale(THREE,(40,60))
FOUR = pygame.image.load('4.png')
FOUR = pygame.transform.scale(FOUR,(40,60))
FIVE = pygame.image.load('5.png')
FIVE = pygame.transform.scale(FIVE,(40,60))
SIX = pygame.image.load('6.png')
SIX = pygame.transform.scale(SIX,(40,60))
SEVEN = pygame.image.load('7.png')
SEVEN = pygame.transform.scale(SEVEN,(40,60))
EIGHT = pygame.image.load('8.png')
EIGHT = pygame.transform.scale(EIGHT,(40,60))
NINE = pygame.image.load('9.png')
NINE = pygame.transform.scale(NINE,(40,60))

def message(size, mess, x_pos, y_pos, color):
    font = pygame.font.SysFont(None, size)
    render = font.render(mess , True, color)
    screen.blit(render, (x_pos, y_pos))


def WelcomeScreen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return

            else:
                message(50,"Welcome to Flappy Bird",10,30,(0,0,0))
                screen.blit(GAME_SPRITES['background'],(0,0))
                screen.blit(GAME_SPRITES['player'],(150,200))
                screen.blit(GAME_SPRITES['base'],(-30,365))
                pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    #Sprites
    GAME_SPRITES['pipe'] = (
    pygame.transform.rotate( pygame.image.load(pipe).convert_alpha(),180),
                            pygame.image.load(pipe).convert_alpha()   )

    GAME_SPRITES['background'] = pygame.image.load(BG).convert()
    GAME_SPRITES['player'] = PLAYER.convert_alpha()
    GAME_SPRITES['base'] = BASE.convert_alpha()

    #Sounds
    # GAME_SOUNDS[''] = pygame.mixer.Sound()

    while True:
        WelcomeScreen()
        maingame()

