from Entity import Entity
from Graphics_Manager import Graphics_Manager
from Content import Content
from pygame.locals import *
import pygame, sys

class Race_Game(object):
    def __init__(self):
        self.graphics_manager = Graphics_Manager()
        self.content = Content()
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
            #print(pygame.event.get())
            self.graphics_manager.update_display()

            #~ count += 1
            #~ if count % 2 == 1:
                #~ self.graphics_manager.DISPLAY_SURF.fill(self.graphics_manager.WHITE)
            #~ else:
                #~ self.graphics_manager.DISPLAY_SURF.fill(self.graphics_manager.BLACK)
            #~ if count == 2:
                #~ count = 0
            self.fps_clock.tick(self.FPS)
