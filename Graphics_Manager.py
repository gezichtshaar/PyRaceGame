import pygame

class Graphics_Manager(object):
    def __init__(self, content):
        self.content = content
        self.DISPLAY_SURF = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("PyRaceGame")
        self.BLACK = (  0,  0,  0)
        self.WHITE = (255,255,255)
        self.RED   = (255,  0,  0)
        self.GREEN = (0  ,255,  0)
        self.BLUE  = (0  ,  0,255)


    def draw_map(self):
        self.DISPLAY_SURF.blit(self.content.map, (0, 0))

    def draw_sprite(self, name, x, y, rot):
        self.DISPLAY_SURF.blit(self.content.SPRITES[name], (x, y))

    def update_display(self):
        pygame.display.update()
