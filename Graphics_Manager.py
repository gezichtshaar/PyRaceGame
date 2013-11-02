import pygame, math

class Graphics_Manager(object):
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

        rotated_sprite = pygame.transform.rotate(self.content.SPRITES[name], math.degrees(rot))
        rect = rotated_sprite.get_rect()
        self.DISPLAY_SURF.blit(rotated_sprite, (x-(rect.width/2), y-(rect.height/2)))

    def update_display(self):
        pygame.display.update()
