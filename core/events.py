import pygame

def handle_events(app):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if app.button.is_clicked(event.pos):
                app.step_sort()


