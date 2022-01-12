from Gamestates.menu import Menu
from settings import *
import pygame as pg


class OutcomeMenu(Menu):
    def __init__(self):
        super(OutcomeMenu, self).__init__()
        self.enemys_party = None
        self.players_party = None

    def startup(self, persistent):
        if "Player's Party" in persistent:
            self.players_party = persistent["Player's Party"]
            self.enemys_party = persistent["Enemy's Party"]

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_n:
                self.persist = {}
                self.next_state_name = "HOME_MENU"
                self.done = True
        if event.type == pg.MOUSEBUTTONDOWN:
            pass
        super(OutcomeMenu, self).get_event(event)

    def update(self, dt):
        super(OutcomeMenu, self).update(dt)

    def draw(self, surface: pg.Surface):
        surface.fill(GREY75)
        super(OutcomeMenu, self).draw(surface)
