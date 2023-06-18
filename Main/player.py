import pygame
from pipe import *

class player:
    def __init__(self,screen):
        self.screen = screen
        self.jump1 = False
        self.gravity = 2
        self.birdx = 200
        self.birdy = 250
        self.y_change = 50
        self.image = pygame.image.load('bird.png')
        self.image = pygame.transform.scale(self.image,(80,80))
        pygame.display.update()
        
    def update(self):
        self.screen.blit(self.image,(self.birdx,self.birdy))
        if self.jump1:
            self.birdy = self.birdy - self.y_change
            self.jump1= False
        else:
            self.birdy = self.birdy + self.gravity
            
        if self.birdy <= 10:
            self.birdy = 10
        if self.birdy >= 420:
            self.birdy = 420
    def jump(self):
        self.jump1= True

    def iscollide(self, pipe:pipe):
        if (self.birdx + 80 >= pipe.pipex and self.birdx + 80 <= pipe.pipex + 100) and (self.birdy <= pipe.pipey - pipe.offset + 500 or self.birdy + 80 >= pipe.pipey):
            return True
        return False

    def score(self,pipe:pipe):
        if pipe.pipex <= 200:
            return True