import pygame

class Graphics_Manager(object):
    def __init__(self):
        DISPLAYSURF = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("PyRaceGame")

    def update_display(self):
        pygame.display.update()

