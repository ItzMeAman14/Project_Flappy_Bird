import pygame
from pipe import *
from player import *
from endscreen import *

screen = pygame.display.set_mode((500,500))
bird = player(screen)
pipes = [pipe(screen)]
bg = pygame.image.load('bg.jpeg')
FPS = 32
score1 = 1
main = True

def message(size, mess, x_pos, y_pos, color,display):
        font = pygame.font.SysFont(None, size)
        render = font.render(mess,True, color)
        display.blit(render, (x_pos, y_pos))

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    while main:
        screen.blit(bg,(0,0))
        bird.update()
        key = pygame.key.get_pressed()
        for p in pipes:
            p.update()
            if bird.iscollide(p):
                message(80,"Game Over",100,250,(0,0,0),screen)
                main = False
                end(main)
            if bird.score(p):
                score1 += 1
                message(50,str(score1//100),250,50,(0,0,0),screen)
            if p.pipex <= 300 and not p.hasSpawned:
                pipes.append(pipe(screen))
                p.hasSpawned = True
            elif p.pipex <= -150:
                pipes.remove(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if key[pygame.K_SPACE]:
                bird.jump() 
        clock.tick(FPS)
        pygame.display.update()
