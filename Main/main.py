import pygame
import random
import sys
import pygame.locals 

pygame.init()

FPS = 32
SCREEENWIDTH = 800
SCREEENHEIGHT = 500
GAME_SPRITES = {}
GAME_SOUNDS = {}
screen = pygame.display.set_mode((SCREEENWIDTH,SCREEENHEIGHT))
pygame.display.set_caption('Flappy Bird')
white = (255,255,255)
black = (0,0,0)
x = 150
y = 250
jump = False
y_change = 30
Gravity = 0.2
fall = False
bg = pygame.image.load('bg.jpeg')
bird1 = pygame.image.load('bird.png')
pipe1 = pygame.image.load('pipe1.jpeg')
pipe2 = pygame.image.load('pipe1.jpeg')

bg = pygame.transform.scale(bg,(800,500))
pipe1 = pygame.transform.scale(pipe1,(100,500))
pipe2 = pygame.transform.scale(pipe2,(100,500))
pipe2 = pygame.transform.rotate(pipe2,180)
bird1 = pygame.transform.scale(bird1,(80,70))
bg_x = 0
bg_y = 0
pipe_x = 300
pipe_y = random.randrange(150,400)
velocity = 2

main = True
while main:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            main = False
            sys.exit()

        if key[pygame.K_SPACE] and y>30:
            jump = True
        if jump:
            jump = False
            y = y - y_change

    if y<312:
        y = y + Gravity*2  
    if y<=30:
        y = y + Gravity*10
            
    bg_x = bg_x - velocity
    pipe_x = pipe_x - velocity
    if bg_x == 0 and pipe_x == 0:
        bg_x = 0
        pipe_x = 0
            
    screen.blit(bg,(bg_x+800,bg_y))
    screen.blit(bg,(bg_x,bg_y))

    screen.blit(bird1,(x,y))
    screen.blit(pipe1,(pipe_x + 800,pipe_y))
    screen.blit(pipe1,(pipe_x,pipe_y))
    screen.blit(pipe2,(pipe_x + 800,pipe_y - 650))
    pygame.time.delay(5)
    pygame.display.update()