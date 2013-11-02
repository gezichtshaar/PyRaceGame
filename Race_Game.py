from Entity import Entity
from Car import Car
from Graphics_Manager import Graphics_Manager
from Content import Content
from pygame.locals import *
import pygame, sys, math

class Race_Game(object):
    def __init__(self):
        self.content = Content()
        self.graphics_manager = Graphics_Manager()
        self.running = False
        self.paused = False
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.entities = {}

    def init_entities(self):
        self.entities['car1'] = Car(self, 'car1', [625, 575], math.pi, 0)
        self.entities['car2'] = Car(self, 'car1', [625, 625], math.pi, 0)

    def run(self):
        running = True
        self.graphics_manager.load_content(self.content)
        self.init_entities()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.graphics_manager.draw_map()

            for entity in self.entities:
                self.entities[entity].update(self.clock.get_time()/1000, 0)
                self.entities[entity].draw(self.graphics_manager)

            #~ self.entities['car1'].update(0, 0)
            #~ self.entities['car1'].draw(self.graphics_manager)

            self.graphics_manager.update_display()
            self.clock.tick(self.FPS)
