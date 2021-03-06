import pygame, math

class GraphicsManager(object):
    def __init__(self):
        self.DISPLAY_SURF = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("PyRaceGame")
        self.BLACK = (  0,  0,  0)
        self.WHITE = (255,255,255)
        self.RED   = (255,  0,  0)
        self.GREEN = (0  ,255,  0)
        self.BLUE  = (0  ,  0,255)

    def load_content(self, content):
        self.content = content

    def draw_map(self):
        self.DISPLAY_SURF.blit(self.content.map, (0, 0))

    def draw_sprite(self, name, x, y, rot):
        """Blits a rotated sprite onto DISPLAY_SURF with a
        negative offset equal to half the height and
        length of the sprite.
        """

        #~ print("degrees: {}".format(math.degrees(rot)))
        rotated_sprite = pygame.transform.rotate(self.content.SPRITES[name], 360-math.degrees(rot))
        rect = rotated_sprite.get_rect()
        rect.center = (x, y)
        self.DISPLAY_SURF.blit(rotated_sprite, rect)

    def update_display(self):
        pygame.display.update()
