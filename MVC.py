# Model
class Player:
    def __init__(self, sno, name, height, weight, games_played):
        self.sno = sno
        self.name = name
        self.height = height
        self.weight = weight
        self.games_played = games_played

class Marvel_Model:
    def __init__(self):
        self.players = [
            Player(1, "IronMan", 180, 75, 120),
            Player(2, "SpiderMan", 170, 65, 110),
            Player(3, "Hulk", 200, 140, 90),
            Player(4, "Thor", 195, 100, 130),
            Player(5, "Captain America", 188, 90, 105)
        ]

class DC_Model:
    def __init__(self):
        self.players = [
            Player(1, "BatMan", 180, 85, 105),
            Player(2, "SuperMan", 189, 95, 205),
            Player(3, "Harvedent", 181, 75, 55),
            Player(4, "Henery", 176, 87, 25),
            Player(5, "Heralt", 184, 100, 45)
        ]

#view
class Marvel_View:
    @staticmethod
    def display_players(players):
        print("Marvel Players:")
        print(f"{'S.No':<5} {'Name':<16} {'Height':<8} {'Weight':<8} {'Games Played':<12}")
        for p in players:
            print(f"{p.sno:<5} {p.name:<16} {p.height:<8} {p.weight:<8} {p.games_played:<12}")

class DC_View:
    @staticmethod
    def display_players(players):
        print("DC Players:")
        print(f"{'S.No':<5} {'Name':<16} {'Height':<8} {'Weight':<8} {'Games Played':<12}")
        for p in players:
            print(f"{p.sno:<5} {p.name:<16} {p.height:<8} {p.weight:<8} {p.games_played:<12}")

# Controller
class Marvel_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_players(self):
        self.view.display_players(self.model.players)

class DC_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_players(self):
        self.view.display_players(self.model.players)

# Usage Example
if __name__ == "__main__":
    marvel_model = Marvel_Model()
    marvel_view = Marvel_View()
    marvel_controller = Marvel_Controller(marvel_model, marvel_view)
    marvel_controller.show_players()

    print()
    dc_model = DC_Model()
    dc_view = DC_View()
    dc_controller = DC_Controller(dc_model, dc_view)
    dc_controller.show_players()