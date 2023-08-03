from GameFrame import Level, RoomObject
from GameFrame import RoomObject, Globals
from Objects.Laser import Laser
import pygame

class Ship(RoomObject):

    def __init__(self,room,x,y):
        RoomObject.__init__(self,room,x,y)
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
        self.handle_key_events = True
    def key_pressed(self, key):
        if key[pygame.K_w]:
            self.y -= 30
        elif key[pygame.K_s]:
            self.y += 30
        if key[pygame.K_a]:
            self.x -= 30
        if key[pygame.K_d]:
            self.x += 30 
        if key[pygame.K_SPACE]:
            self.shoot_laser()
        if key[pygame.K_e]:
            self.rotate(30)
        if key[pygame.K_q]:
            self.rotate(-30)
    def keep_in_room(self):
        if self.y < 0: 
            self.y = 0 
        elif self.y + self.height > Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
        elif self.x < 0: 
            self.x = 0 
        elif self.x + self.width > Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width
    def step(self):
        self.keep_in_room()
    def shoot_laser(self):
        new_laser = Laser(self.room, 
                          self.x + self.width,
                          self.y +self.height/2-4)
        self.room.add_room_object(new_laser)
       