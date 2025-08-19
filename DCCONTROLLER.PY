from DCMODLE import DC_Model
from DCVIEW import DC_view

class MarvelController:
    def __init__(self):
        self.model = DC_Model()
        self.view = DC_view(self.model)

    def set_character_details(self, serial_no, name, height, weight, games_played):
        self.model.set_serial_no(serial_no)
        self.model.set_name(name)
        self.model.set_height(height)
        self.model.set_weight(weight)
        self.model.set_games_played(games_played)

    def display_character(self):
        self.view.display_character()