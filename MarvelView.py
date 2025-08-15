class MarvelView:
    def __init__(self, marvel):
        self.marvel = marvel

    def show_marvel(self):
        print("Marvel details")
        print(f"s no: {self.marvel.s_no}")
        print(f"name: {self.marvel.name}")
        print(f"height: {self.marvel.height}")
        print(f"weight: {self.marvel.weight}")
        print(f"games_played: {self.marvel.games_played}")


