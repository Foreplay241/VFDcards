from Cards.character_card import Character
from GUI.text_button import TextButton
from Gamestates.menu import Menu, generate_new_card_data
from settings import *
import pygame as pg


class OutcomeMenu(Menu):
    def __init__(self):
        super(OutcomeMenu, self).__init__()
        self.enemys_party = None
        self.players_party = None
        self.player_num_wins = 0
        self.winner_text_button = TextButton("OUT0", (0, 0), (256, 64), (256, 64),
                                             "winorloss. Click here for next screen.", fontsize=32,
                                             textcolor=GHOST_WHITE, row=5, max_row=16, col=5, max_col=10,
                                             maxWidth=620)
        self.home_menu_button = TextButton("OUT1", (0, 0), (256, 64), (256, 64), "Home menu for a new game.",
                                           fontsize=32,
                                           textcolor=GHOST_WHITE, row=7, max_row=16, col=5, max_col=10,
                                           maxWidth=620)
        self.exit_button = TextButton("OUT2", (0, 0), (256, 64), (256, 64), "Quit", fontsize=32,
                                      textcolor=GHOST_WHITE, row=9, max_row=16, col=5, max_col=10,
                                      maxWidth=620)
        self.all_buttons.append(self.winner_text_button)
        self.all_buttons.append(self.home_menu_button)
        self.all_buttons.append(self.exit_button)

    def startup(self, persistent):
        self.player_num_wins = 0
        if "Player's Party" in persistent:
            self.players_party = persistent["Player's Party"]
        if "Enemy's Party" in persistent:
            self.enemys_party = persistent["Enemy's Party"]
        for pc in self.players_party:
            pc.hasBattled = False
            if pc.isWinner:
                self.player_num_wins += 1
        if self.player_num_wins <= 1:
            self.winner_text_button.update_button_text("Loser!! Click here for home menu.")
        else:
            self.winner_text_button.update_button_text("Winner!! Click here for next round.")
        super(OutcomeMenu, self).startup(persistent)

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            pass
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.winner_text_button.rect.collidepoint(self.mouse_pos):
                if self.winner_text_button.text.startswith("Loser!!"):
                    self.persist = {}
                    self.next_state_name = "HOME_MENU"
                    self.done = True
                if self.winner_text_button.text.startswith("Winner!!"):
                    self.enemys_party = []
                    for i in range(3):
                        new_enemy_data = generate_new_card_data(name=random.choice(EXAMPLE_NAMES),
                                                                creation_time=random.randint(100000, 999999),
                                                                card_type="Enemy Character",
                                                                class_group=random.choice(CLASS_GROUPS))
                        self.enemys_party.append(new_enemy_data)
                    self.persist = {
                        "Player's Party": self.players_party,
                        "Enemy's new Party": self.enemys_party,
                    }
                    self.next_state_name = "GAME"
                    self.done = True

        super(OutcomeMenu, self).get_event(event)

    def update(self, dt):
        super(OutcomeMenu, self).update(dt)

    def draw(self, surface: pg.Surface):
        surface.fill(WHITE_SMOKE)
        super(OutcomeMenu, self).draw(surface)
