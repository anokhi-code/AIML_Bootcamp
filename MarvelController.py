from MarvelModel import Marvel
from MarvelView import MarvelView

class MarvelController:
    def __init__(self):
        self.marvel = Marvel()
        self.marvel_view = MarvelView(self.marvel)

    def set_marvel_data(self):
        number_of_marvel_team_members= int(input("Enter the number of teams members: "))
        marvel_teams = []
        for i in range(number_of_marvel_team_members):
            marvel_team = {}
            s_no = input("Enter the serial number: ")
            self.marvel.set_s_no(s_no)
            name = input("Enter the name: ")
            self.marvel.set_name(name)
            height = input("Enter the height: ")
            self.marvel.set_height(height)
            weight = input("Enter the weight: ")
            self.marvel.set_weight(weight)
            games_played = input("Enter the games played: ")
            self.marvel.set_games_played(games_played)
            marvel_team.update({"s_no" : s_no})
            marvel_team.update({"name": name})
            marvel_team.update({"height": height})
            marvel_team.update({"weight": weight})
            marvel_team.update({"games_played": games_played})
            print(marvel_team)
            marvel_teams.append(marvel_team)
        print(marvel_teams)

    def display(self):
        self.marvel_view.show_marvel()





controller = MarvelController()
controller.set_marvel_data()
controller.display()

