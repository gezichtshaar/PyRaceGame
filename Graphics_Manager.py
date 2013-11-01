import pygame

class Graphics_Manager(object):
    def __init__(self):
        self.DISPLAY_SURF = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("PyRaceGame")
        self.BLACK = (  0,  0,  0)
        self.WHITE = (255,255,255)
        self.RED   = (255,  0,  0)
        self.GREEN = (0  ,255,  0)
        self.BLUE  = (0  ,  0,255)

    def update_display(self):
        pygame.display.update()

