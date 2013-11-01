from Entity import Entity
from Car import Car
from Graphics_Manager import Graphics_Manager
from Content import Content
from pygame.locals import *
import pygame, sys

class Race_Game(object):
    def __init__(self):
        self.content = Content()
        self.graphics_manager = Graphics_Manager(self.content)
        self.running = False
        self.paused = False
        self.FPS = 60
        self.fps_clock = pygame.time.Clock()
        self.entities = []

    def run(self):
        #~ count = 0
        running = True
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.graphics_manager.draw_map()


            #~ self.entities.append(Car(self, 'car1', [50, 50], 0, 0))
            #~ self.entities[0].render(self.graphics_manager)


            self.graphics_manager.update_display()
            self.fps_clock.tick(self.FPS)
