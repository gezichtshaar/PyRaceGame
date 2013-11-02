import pygame

class Powerup(Entity):
    def __init__(self, game, sprite_name, category, coords)
        super().__init__('Powerup', game, sprite_name, coords, [30, 30], 0, True, True, False)
        self.category = self.category
        self.is_active = True
        self.timer = -1

    def reset_car_damage(self, car):
        """Sets car damage to 0."""
        car.damage = 0

    def reset_car_petrol(self, car):
        """Sets car petrol to 100."""
        car.petrol = 100

    def update(self, dt, input_manager):

