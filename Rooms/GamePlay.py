from GameFrame import Level, Globals
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Hud import Score, Lives

class GamePlay(Level):
    def __init__ (self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("Background.png")
        
        self.add_room_object(Ship(self,25,50))
        self.add_room_object(Zork(self,1120,50))

        self.score = Score(self,
                           Globals.SCREEN_WIDTH/2-20,20,
                           str(Globals.SCORE))
        self.add_room_object(self.score)
        self.lives = Lives(self, Globals.SCREEN_HEIGHT- 150,29)
        self.add_room_object(self.lives)
        self.laser_shoot = self.load_sound("Laser_shot.ogg")
        self.asteroid_shot = self.load_sound("Asteroid_shot.wav")
        self.astronaut_hit = self.load_sound("Astronaut_hit.ogg")
        self.astronaut_saved = self.load_sound("Astronaut_saved.ogg")
        self.ship_damage = self.load_sound("Ship_damage.ogg")

