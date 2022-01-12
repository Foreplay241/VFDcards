from Gamestates.gamestate import GameState
from settings import *


class Menu(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        pass

    def get_event(self, event):
        super(Menu, self).get_event(event)

    def update(self, dt):
        super(Menu, self).update(dt)

    def draw(self, surface: pg.Surface):
        super(Menu, self).draw(surface)
