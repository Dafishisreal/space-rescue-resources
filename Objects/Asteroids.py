from GameFrame import RoomObject, Globals
import random

class Asteroid(RoomObject):
    """
    A class for Zorks danerous obstacles
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Asteroid object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set image
        image = self.load_image("asteroid.png")
        self.set_image(image,50,49)
        
        # set travel direction
        angle = random.randint(135,225)
        self.set_direction(angle, 10)

        # register events 
        self.register_collision_object("Ship")
        self.register_collision_object("Laser")
        
    def step(self):
        """
        Determines what happens to the asteroid on each tick of the game clock
        """
        self.keep_in_room()
        self.outside_of_room()
        
    def keep_in_room(self):
        """
        Keeps the asteroid inside the top and bottom room limits
        """
        if self.y < 0:
            self.y = 0
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT*2 - self.height:
            self.y = Globals.SCREEN_HEIGHT*2 - self.height
            self.y_speed *= -1
        elif self.x < 0:
            self.x = 0
            self.x_speed *= -1
        elif self.x > Globals.SCREEN_WIDTH*2 - self.width:
            self.x = Globals.SCREEN_WIDTH*2 - self.width
            self.x_speed *= -1
        
            
    def outside_of_room(self):
        """
        removes asteroid that have exited the room
        """
        if self.x + self.width < 0:
            print("asteroid deleted")
            self.room.delete_object(self)
    def handle_collision(self, other, other_type):
        if other_type == "Ship":
            self.room.running = False
    def handle_collision(self, other, other_type):
        if other_type == "Laser":
            self.delete_object(self)
    