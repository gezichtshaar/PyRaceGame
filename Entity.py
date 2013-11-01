import abc

class Entity(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, game, coords, hitbox, rot, is_visible, is_collidable, is_actor):
        self.name = name
        self.game = game
        self.coords = coords
        self.velocity = 0
        self.accel = 0
        self.hitbox = hitbox
        self.rot = rot
        self.is_visible = is_visible
        self.is_collidable = is_collidable
        self.is_actor = is_actor
        self.is_alive = True

    @abc.abstractmethod
    def render(self):
        """Renders"""
