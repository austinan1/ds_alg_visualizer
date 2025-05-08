import pygame
from sys import exit





def drawStart():
    pass

def drawArray():
    pass


def main():
    pygame.init()
    pygame.display.set_caption("Data Structure & Algorithm Visualizer")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))

    #initializer
    screen_width = 800
    screen_height = 800
    screen1 = pygame.Surface((800,800))
    screen1.fill((255, 255, 255))

    #start buttons and shi
    
    
    

    mode = 'Start'
    #possible modes = start,array, every data type etc...

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(screen1,(0,0))
        if mode == 'Start':
            drawStart()
        if mode == 'Array':
            drawArray()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()