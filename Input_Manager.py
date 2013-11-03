import pygame, sys
from pygame.locals import *

class Input_Manager(object):
    def __init__(self):
        self.keyboad_state = pygame.key.get_pressed()

    def handle_input(self, game):
        self.keyboard_state = pygame.key.get_pressed()

        if self.keyboard_state[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
