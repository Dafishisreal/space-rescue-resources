from Objects.Title import Title

from GameFrame import Level


class WelcomeScreen(Level):
    def  __init__ (self, screen, joysticks):
        Level.__init__(self, screen , joysticks)


        self.set_background_image("Background.png")
        self.add_room_object(Title(self,240,200))