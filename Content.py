import pygame

class Content(object):
    def __init__(self):
        self.load_sprites()
        self.load_sound()
        self.load_map()

    def load_sprites(self):
        """Load all sprites"""

        car1 = pygame.image.load('Content/car1.png')
        car1 = pygame.transform.scale(car1, (80, 48))
        self.SPRITES = {'car1': car1}

    def load_sound(self):
        """Load all sound files"""

        foo = "bar"

    def load_map(self):
        """Load the map"""

        self.map = pygame.image.load('Content/map.png')
