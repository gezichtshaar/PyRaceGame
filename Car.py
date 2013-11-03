from Entity import Entity
import math

TAU = math.pi * 2

class Car(Entity):
    def __init__(self, game, sprite_name, coords, rot, keys):
        super().__init__('Car', game, sprite_name, coords, [50, 50], rot, True, True, True)
        self.keys = keys
        self.damage = 0
        self.petrol = 100
        checkpoints = [False, False, False, False]

    def update(self, dt, input_manager):
        print("accel: {}".format(self.accel))
        print("velocity: {}".format(self.velocity))
        print("rot: {}".format(self.rot))
        print("dt: {}".format(dt))

        self.negative_accel = 0.3 * -self.velocity

        if input_manager.keyboard_state[self.keys[0]]: #forward
            self.accel += 100 * dt
            if self.accel > 75:
                self.accel = 75

        if input_manager.keyboard_state[self.keys[1]]: #backward
            if self.accel > 0:
                self.accel -= 200 * dt
            elif self.accel <= 0:
                self.accel -= 10 * dt
            if self.accel < -50:
                self.accel = -50

        if input_manager.keyboard_state[self.keys[2]]: #left
            self.rot -= 0.01 * self.velocity * dt

        if input_manager.keyboard_state[self.keys[3]]: #right
            self.rot += 0.01 * self.velocity * dt

        if not input_manager.keyboard_state[self.keys[0]] and not input_manager.keyboard_state[self.keys[1]]: #neither forward nor backward
            self.accel = 0

        self.velocity += (self.accel + self.negative_accel) * dt # v = a * dt

        self.rot %= TAU # Keep rot lower than 6.28/TAU
        if self.rot < 0:
            self.rot += TAU # Keep rot positive

        if self.velocity > -5 and self.velocity < 5 and self.accel == 0:
            self.velocity = 0 # Set velocity to 0 if it is negligibly low.
        else:
            # This might need to be reworked to account for dt
            pass

        self.coords[0] += self.velocity * dt * math.cos(self.rot) # sx = v * dt * cos()
        self.coords[1] += self.velocity * dt * math.sin(self.rot) # sy = v * dt * sin()

    def draw(self, graphics_manager):
        super(Car, self).draw(graphics_manager)
        #~ graphics_manager.draw_sprite(self.sprite_name, self.coords[0], self.coords[1], self.rot)

