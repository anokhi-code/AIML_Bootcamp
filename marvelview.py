class Marvel_view:
    def __init__(self, model):
        self.model = model

    def display_character(self):
        print(f"Serial No: {self.model.get_serial_no()}")
        print(f"Name: {self.model.get_name()}")
        print(f"Height: {self.model.get_height()} cm")
        print(f"Weight: {self.model.get_weight()} kg")
        print(f"Games Played: {self.model.get_games_played()}")
    
    