class DCView:
    def __init__(self, dc):
        self.dc = dc

    def show_dc(self):
        print("DC Team details")
        print(f"s no: {self.dc.s_no}")
        print(f"name: {self.dc.name}")
        print(f"height: {self.dc.height}")
        print(f"weight: {self.dc.weight}")
        print(f"games_played: {self.dc.games_played}")


