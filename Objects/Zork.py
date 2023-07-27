from GameFrame import Level, RoomObject
from GameFrame import RoomObject, Globals
import random

class Zork(RoomObject):
    def __init__(self,room,x,y):
        RoomObject.__init__(self,room,x,y)
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)
        self.y_speed = random.choice([-10,10])
    def keep_in_room(self): 
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
    def step(self):
        self.keep_in_room()