from marvelmodel import Marvel_Model
from marvelview import Marvel_view

class MarvelController:
    def __init__(self):
        self.model = Marvel_Model()
        self.view = Marvel_view(self.model)

    def set_character_details(self, serial_no, name, height, weight, games_played):
        self.model.set_serial_no(serial_no)
        self.model.set_name(name)
        self.model.set_height(height)
        self.model.set_weight(weight)
        self.model.set_games_played(games_played)

    def display_character(self):
        self.view.display_character()

if __name__ == "__main__":   # correct way to check
    controller = MarvelController()   # create controller
    controller.set_character_details()
    controller.display_character()
