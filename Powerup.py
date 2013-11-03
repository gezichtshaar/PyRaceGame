from Entity import Entity

class Powerup(Entity):
    def __init__(self, game, sprite_name, coords, category):
        super().__init__('Powerup', game, sprite_name, coords, [30, 30], 0, True, True, False)
        self.category = category
        self.is_active = True
        self.timer = 0

    def reset_car_damage(self, car):
        """Sets car damage to 0."""
        car.damage = 0

    def reset_car_petrol(self, car):
        """Sets car petrol to 100."""
        car.petrol = 100

    def update(self, dt, input_manager):
        if self.timer > 0:
            self.timer -= dt
        else:
            self.timer = 0
            self.is_active = True
            self.is_visible = True
            self.is_collidable = True

    def draw(self, graphics_manager):
        super(Powerup, self).draw(graphics_manager)
