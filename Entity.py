import abc

class Entity(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, game, sprite_name, coords, hitbox, rot, is_visible, is_collidable, is_actor):
        self.name = name
        self.game = game
        self.sprite_name = sprite_name
        self.coords = coords
        self.velocity = 0
        self.accel = 0
        self.negative_accel = 0
        self.hitbox = hitbox
        self.rot = rot
        self.is_visible = is_visible
        self.is_collidable = is_collidable
        self.is_actor = is_actor
        self.is_alive = True

    @abc.abstractmethod
    def update():
        """Updates"""

    @abc.abstractmethod
    def draw(self, graphics_manager):
        """Draws sprite in Graphics_Manager"""
        graphics_manager.draw_sprite(self.sprite_name, self.coords[0], self.coords[1], self.rot)

