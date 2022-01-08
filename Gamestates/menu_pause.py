from Gamestates.menu import Menu


class PauseMenu(Menu):
    def __init__(self):
        super(PauseMenu, self).__init__()
        self.paused_player_party = []
        self.paused_enemy_party = []

    def startup(self, persistent):
        self.paused_player_party = persistent["Player's Party"]
        self.paused_enemy_party = persistent["Enemy's Party"]