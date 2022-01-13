from GUI.text_button import TextButton
from Gamestates.menu import Menu
from settings import *
import pygame as pg


class OutcomeMenu(Menu):
    def __init__(self):
        super(OutcomeMenu, self).__init__()
        self.enemys_party = None
        self.players_party = None
        self.players_num_winners = 0
        self.winner_text_button = TextButton("TUT0", (0, 0), (256, 64), (256, 64), "Player is winner.", fontsize=32,
                                             textcolor=GHOST_WHITE, row=15, max_row=16, col=5, max_col=10,
                                             maxWidth=620)
        self.all_buttons.append(self.winner_text_button)

    def startup(self, persistent):
        if "Player's Party" in persistent:
            self.players_party = persistent["Player's Party"]
            self.enemys_party = persistent["Enemy's Party"]
        for pc in self.players_party:
            if pc.isWinner:
                self.players_num_winners += 1
        if self.players_num_winners <= 1:
            self.winner_text_button.update_button_text("Player is the loser.")
        super(OutcomeMenu, self).startup(persistent)

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
