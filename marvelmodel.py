class Marvel_Model:
    def __init__(self):
       self.serial_no = 0
       self.name = ""
       self.height = 0
       self.weight = 0
       self.games_played = 0

# setters
    def set_serial_no(self, S_no):
        self.serial_no = S_no
    def set_name(self, name):
        self.name = name
    def set_height(self, height):
        self.height = height
    def set_weight(self, weight):
        self.weight = weight
    def set_games_played(self, game):
        self.games_played = game

# getters
    def get_serial_no(self):
        return self.serial_no
    def get_name(self):
        return self.name
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_games_played(self):
        return self.games_played
    
