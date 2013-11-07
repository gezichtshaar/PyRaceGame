from Entity import Entity
from Car import Car
from GraphicsManager import GraphicsManager
from InputManager import InputManager
from Content import Content
from Powerup import Powerup
import pygame, math

class RaceGame(object):
    def __init__(self): #todo, add settingsmanager for framerate and keybinding
        self.content = Content()
        self.graphics_manager = GraphicsManager()
        self.input_manager = InputManager()
        self.time = pygame.time # Clock object won't be as precise as custom timing
        self.running = False
        self.paused = False
        self.FPS = 30
        self.last_update = 0
        self.next_update = 0
        self.entities = {} # sould probebly not be an associative list, no need for it

    def init_entities(self):
        self.entities['car1'] = Car(self, 'car1', [625, 575], math.pi, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
        self.entities['car2'] = Car(self, 'car1', [625, 625], math.pi, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.entities['powerup1'] = Powerup(self, 'petrol', [50, 50], 'petrol')
        
    def tick(self):
        dt = 0
        while self.time.get_ticks() < (self.next_update + dt) || dt == 0:
            dt = (self.time.get_ticks()-self.last_update)/1000
            self.update(dt)
        self.render()
        self.last_update = self.next_update
        self.next_update += self.FPS/1000
        
    def update(self, dt):
        self.input_manager.handle_input(self)
        if !self.paused:
            for entity in self.entities:
                self.entities[entity].update(dt, self.input_manager)
        
    def render(self):
        self.graphics_manager.draw_map() #souldn't be handled by graphics_manager
        for entity in self.entities:
            self.entities[entity].draw(self.graphics_manager)
        self.graphics_manager.update_display() # also shouldn't be handled by graphics_manager
        

    def run(self):
        if !self.running: #don't run while running
            self.graphics_manager.load_content(self.content)
            self.init_entities()
            self.last_update = self.time.get_ticks()
            self.next_update = self.last_update + self.FPS/1000
            self.running = True
            while self.running:
                self.tick()
                self.time.wait(10) #make sure the program doesn't explode
