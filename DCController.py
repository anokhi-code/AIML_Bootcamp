from DCModel import DC
from DCView import DCView

class DCController:
    def __init__(self):
        self.dc = DC()
        self.dc_view = DCView(self.dc)

    def set_dc_data(self):
        number_of_dc_team_members = int(input("Enter the number of DC team members: "))
        dc_teams = []
        for i in range(number_of_dc_team_members):
            dc_team = {}
            s_no = input("Enter the serial number: ")
            self.dc.set_s_no(s_no)
            name = input("Enter the name: ")
            self.dc.set_name(name)
            height = input("Enter the height: ")
            self.dc.set_height(height)
            weight = input("Enter the weight: ")
            self.dc.set_weight(weight)
            games_played = input("Enter the games played: ")
            self.dc.set_games_played(games_played)
            dc_team.update({"s_no": s_no})
            dc_team.update({"name": name})
            dc_team.update({"height": height})
            dc_team.update({"weight": weight})
            dc_team.update({"games_played": games_played})
            print(dc_team)
            dc_teams.append(dc_team)
        print(dc_teams)

    def display(self):
        self.dc_view.show_dc()


controller = DCController()
controller.set_dc_data()
controller.display()

