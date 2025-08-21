class DC_Model:
    def __init__(self):
        self.heroes = []

    def add_hero(self, serial_no, name, height, weight, games_played):
        hero = {
            "serial_no": serial_no,
            "name": name,
            "height": height,
            "weight": weight,
            "games_played": games_played
        }
        self.heroes.append(hero)

    def get_heroes(self):
        return self.heroes
