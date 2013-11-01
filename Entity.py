from Race_Game import Race_Game

class Entity(object):
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
        self.x = "hello, world!!!!"
