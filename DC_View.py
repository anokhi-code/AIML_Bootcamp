class DC_View:
    def __init__(self, model):
        self.model = model

    def display_all_characters(self):
        heroes = self.model.get_heroes()
        print(f"{'S No':<6} {'Name':<20} {'Height (cm)':<12} {'Weight (kg)':<12} {'Games Played':<12}")
        for hero in heroes:
            print(f"{hero['serial_no']:<6} {hero['name']:<20} {hero['height']:<12} {hero['weight']:<12} {hero['games_played']:<12}")
