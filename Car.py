from Entity import Entity
from Race_Game import Race_Game

class Car(Entity):
    def __init__(self, game, coords, rot, keys):
        super().__init__("Car", game, coords, [50, 50], rot, True, True, True)


#~ game = Race_Game()
#~ car = Car(game, [0, 0], 0, 0)
