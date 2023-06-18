import pygame
import random


class pipe:
    def __init__(self, display):
        self.display = display
        self.pipex = 580
        self.offset = 650
        self.pipey = random.randrange(200,400)
        self.image =  pygame.image.load('pipe1.jpeg')
        self.image = pygame.transform.scale(self.image,(100,500))
        self.image2 = pygame.image.load('pipe1.jpeg')
        self.image2 = pygame.transform.scale(self.image2,(100,500))
        self.image2 = pygame.transform.rotate(self.image2,180)
        self.hasSpawned = False
        # display.blit(self.image,(self.pipex,self.pipey))
        # display.blit(self.image2,(self.pipex,self.pipey - self.offset))
    
    def update(self):
        self.pipex -= 3
        # if self.pipex <= 50:
            # self.pipex = 50
        # self.pipe -= 10
        self.display.blit(self.image,(self.pipex,self.pipey))
        self.display.blit(self.image2,(self.pipex,self.pipey - self.offset))
        