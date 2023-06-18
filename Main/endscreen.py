import pygame

screen = pygame.display.set_mode((500,500))
endsc = pygame.image.load('end.png')
def end(main):
    pygame.init()
    while True:
        screen.fill((0,255,0))
        key = pygame.key.get_pressed()
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if key[pygame.K_UP]:
                pygame.quit()
                quit()
            if key[pygame.K_SPACE]:
                main = True
                return



