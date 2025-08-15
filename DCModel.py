class DC :
    def __init__(self):
        self.s_no = ""
        self.name = ""
        self.height = ""
        self.weight = ""
        self.games_played = ""

    def set_s_no(self, s_no):
        self.s_no = s_no
    def get_s_no(self):
        return self.s_no

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def set_height(self, height):
        self.height = height
    def get_height(self):
        return self.height

    def set_weight(self, weight):
        self.weight = weight
    def get_weight(self):
        return self.weight

    def set_games_played(self, games_played):
        self.games_played = games_played
    def get_games_played(self):
        return self.games_played