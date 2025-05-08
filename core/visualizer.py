import pygame
from core.ui import Button
from core.events import handle_events
from algorithms.sorting.bubble_sort import bubble_sort


class Visualizer:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("DS & Algo Visualizer")
        self.clock = pygame.time.Clock()
        self.running = True

        screen1 = pygame.Surface((800,800))
        screen1.fill((255, 255, 255))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            pygame.display.update()
            self.screen.blit(screen1,(0,0)) 