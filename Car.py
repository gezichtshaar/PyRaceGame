from Entity import Entity
import math

#
TAU = math.pi * 2

class Car(Entity):
    def __init__(self, game, sprite_name, coords, rot, keys):
        super().__init__('Car', game, sprite_name, coords, [50, 50], rot, True, True, True)
        self.keys = keys
        self.damage = 0
        self.petrol = 100
        checkpoints = [False, False, False, False]

    def update(self, dt, input_manager):
        self.rot += 3 * dt

        if False: #forward
            self.accel += 100 * dt
            if self.accel > 100:
                self.accel = 100

        if False: #backward
            if self.accel > 0:
                self.accel -= 200 * dt
            elif self.accel <= 0:
                self.accel -= 10 * dt
            if self.accel < -75:
                self.accel = -75

        if False: #left
            self.rot -= 0.01 * self.velocity * dt

        if False: #right
            self.rot += 0.01 * self.velocity * dt

        if not True and not True: #neither forward nor backward
            self.accel = 0

        self.velocity += self.accel * dt # v = a * dt

        self.rot %= TAU # Keep rot lower than 6.28/TAU
        if self.rot < 0:
            self.rot += TAU # Keep rot positive

        if self.velocity > -5 and self.velocity < 5 and self.accel == 0:
            self.velocity = 0 # Set velocity to 0 if it is negligibly low.
        else:
            # This might need to be reworked to account for dt
            self.velocity += 0.99 # Emulate "friction" by reducing the speed of the car.

        self.coords[0] += self.velocity * dt * math.cos(self.rot) # sx = v * dt * cos()
        self.coords[1] += self.velocity * dt * math.sin(self.rot) # sy = v * dt * sin()

    def draw(self, graphics_manager):
        super(Car, self).draw(graphics_manager)
        #~ graphics_manager.draw_sprite(self.sprite_name, self.coords[0], self.coords[1], self.rot)

