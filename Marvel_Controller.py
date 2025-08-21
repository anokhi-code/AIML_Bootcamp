from Marvel_Model import Marvel_Model
from Marvel_View import Marvel_View

class Marvel_Controller:
    def __init__(self):
        self.model = Marvel_Model()
        self.view = Marvel_View(self.model)

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
        print(f"{name} added to Marvel team.\n")

    def display_characters(self):
        self.view.display_all_characters()

if __name__ == "__main__":
    controller = Marvel_Controller()
    controller.input_hero()
    controller.display_characters()
