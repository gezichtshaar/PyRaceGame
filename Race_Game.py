from Entity import Entity
from Graphics_Manager import Graphics_Manager
from pygame.locals import *
import pygame, sys

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (0  ,255,  0)
BLUE  = (0  ,  0,255)

class Race_Game(object):
    def __init__(self):
        self.graphics_manager = Graphics_Manager()
        self.running = False
        self.paused = False
        self.entities = []

    def run(self):
        #count = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            #print(pygame.event.get())
            self.graphics_manager.update_display()

            #~ count += 1
            #~ if count % 2 == 1:
                #~ self.graphics_manager.DISPLAY_SURF.fill(WHITE)
            #~ else:
                #~ self.graphics_manager.DISPLAY_SURF.fill(BLACK)
            #~ if count == 2:
                #~ count = 0
