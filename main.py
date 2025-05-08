import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Data Structure & Algorithm Visualizer")
clock = pygame.time.Clock()

font1 = pygame.font.Font(None, 30)

test_surface = pygame.Surface((100,100))
test_surface.fill('Blue')

surface2 = pygame.image.load('assets/1.png')

txtsurface = font1.render('yay', True, 'Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(100,100))
    screen.blit(surface2,(400,400))
    screen.blit(txtsurface, (400,50))

    pygame.display.update()
    clock.tick(60)