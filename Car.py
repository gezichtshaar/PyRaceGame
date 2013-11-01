from Entity import Entity
import math

TAU = math.pi * 2

class Car(Entity):
    def __init__(self, game, coords, rot, keys):
        super().__init__("Car", game, coords, [50, 50], rot, True, True, True)
        self.keys = keys
        self.damage = 0
        self.petrol = 100
        checkpoints = [False, False, False, False]

    def update(self, dt, input_manager):
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

        self.rot %= TAU
        if self.rot < 0:
            self.rot += TAU

        if self.velocity > -5 and self.velocity < 5 and self.accel == 0:
            self.velocity = 0
        else:
            self.velocity += 0.99

        self.coords[0] += self.velocity * math.cos(rot) * dt
        self.coords[1] += self.velocity * math.sin(rot) * dt

