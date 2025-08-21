from DC_Model import DC_Model
from DC_View import DC_View

class DC_Controller:
    def __init__(self):
        self.model = DC_Model()
        self.view = DC_View(self.model)

    def input_hero(self):
        try:
            serial_no = int(input("Enter Serial No: "))
            name = input("Enter Name: ")
            height = int(input("Enter Height (cm): "))
            weight = int(input("Enter Weight (kg): "))
            games_played = int(input("Enter Games Played: "))
        except ValueError:
            print("Please enter valid numeric values for serial no, height, weight, and games played.")
            return
        self.model.add_hero(serial_no, name, height, weight, games_played)
        print(f"{name} added to DC team.\n")


    def set_character_details(self, serial_no, name, height, weight, games_played):
        self.model.add_hero(serial_no, name, height, weight, games_played)

    def display_characters(self):
        self.view.display_all_characters()


if __name__ == "__main__":
    controller = DC_Controller()
    controller.input_hero()
    controller.display_characters()
    
    