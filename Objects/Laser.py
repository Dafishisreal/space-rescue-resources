from GameFrame import RoomObject, Globals
from Objects import Ship

class Laser(RoomObject):
    def __init__(self, room, x , y,angle):
        RoomObject.__init__(self, room, x ,y)
        self.angle = angle 
        image = self.load_image("Laser.png")
        self.set_image(image,33,9)
        self.set_direction(self.angle,20)
        self.register_collision_object("Astronaut")
        self.register_collision_object("Asteroid")
    def step(self): 
        self.outside_of_room()
    def outside_of_room(self):
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)      
    def spawn_laser(self): 
        new_laser = Laser(self.room, 
                          self.x + self.width,
                          self.y +self.height/2-4)
        self.room.add_room_object(new_laser)
        self.set_timer(10, self.spawn_laser)

    def handle_collision(self, other, other_type):
        if other_type == "Asteroid":
            self.delete_object(self)
            self.delete_object(other)
            self.room.score.update_score(5)
            self.room.asteroid_shot.play()
        if other_type == "Astronaut":
            self.room.delete_object(other)
            self.room.score.update_score(-10)
            self.room.astronaut_hit.play()
            
