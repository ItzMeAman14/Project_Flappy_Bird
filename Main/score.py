import pygame
from player import *

class score:
    def __init__(self):
        self.score = 0


    def message(size, mess, x_pos, y_pos, color,display):
        font = pygame.font.SysFont(None, size)
        render = font.render(mess , True, color)
        display.blit(render, (x_pos, y_pos))

    def score_count(self):
        if player.iscollide is False:
            self.score += 1
            
            

    