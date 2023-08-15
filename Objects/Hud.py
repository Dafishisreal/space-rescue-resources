from GameFrame import Level, TextObject,Globals
class Score(TextObject):
    def __init__(self, room: Level, x: int, y: int, text= None):

        TextObject.__init__(self,room, x, y, text)
        self.size=60
        Globals.SCORE = 0
        self.font='Comic Sans MS' 
        self.colour= (255,255,255)
        self.bold=False
        self.update_text()
    def update_score(self,change):
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()