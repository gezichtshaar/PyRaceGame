from Entity import Entity
from Car import Car
from GraphicsManager import GraphicsManager
from InputManager import InputManager
from Content import Content
from Powerup import Powerup
import pygame, math

class RaceGame(object):
    def __init__(self):
        self.content = Content()
        self.graphics_manager = GraphicsManager()
        self.input_manager = InputManager()
        self.running = False
        self.paused = False
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.entities = {}

    def init_entities(self):
        self.entities['car1'] = Car(self, 'car1', [625, 575], math.pi, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
        self.entities['car2'] = Car(self, 'car1', [625, 625], math.pi, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.entities['powerup1'] = Powerup(self, 'petrol', [50, 50], 'petrol')

    def run(self):
        running = True
        self.graphics_manager.load_content(self.content)
        self.init_entities()
        while True:
            self.input_manager.handle_input(self)
            self.graphics_manager.draw_map()

            # This is yet to be made a separate method.
            for entity in self.entities:
                self.entities[entity].update(self.clock.get_time()/1000, self.input_manager)
                self.entities[entity].draw(self.graphics_manager)

            self.graphics_manager.update_display()
            self.clock.tick(self.FPS)
