from Gamestates.menu import Menu
import pygame as pg
from settings import *


class PauseMenu(Menu):
    def __init__(self):
        super(PauseMenu, self).__init__()
        self.paused_player_party = []
        self.paused_enemy_party = []

    def startup(self, persistent):
        self.paused_player_party = persistent["Player's Party"]
        self.paused_enemy_party = persistent["Enemy's Party"]

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                self.persist = {
                    "Player's Party": self.paused_player_party,
                    "Enemy's Party": self.paused_enemy_party
                }
                self.next_state_name = "GAME"
                self.done = True

    def update(self, dt):
        super(PauseMenu, self).update(dt)

    def draw(self, surface: pg.Surface):
        surface.fill(BAKERS_CHOCOLATE)
        super(PauseMenu, self).draw(surface)
