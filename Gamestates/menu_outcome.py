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
        self.playerWLT = [0, 0, 0]
        self.enemyWLT = [0, 0, 0]
        self.enemys_winlosstie_button = TextButton("OUT0", (0, 0), (256, 64), (256, 64), "Win-Loss-Tie",
                                                   textcolor=DARK_TURQUOISE,
                                                   optiontext="Enemy", optioncolor=INDIAN_RED,
                                                   valuetext="W-L-T", valuecolor=DARK_TAN,
                                                   row=5, max_row=16, col=5, max_col=10, maxWidth=620)
        self.players_winlosstie_button = TextButton("OUT0", (0, 0), (256, 64), (256, 64), "Win-Loss-Tie",
                                                    textcolor=DARK_TURQUOISE,
                                                    optiontext="Player", optioncolor=LAWN_GREEN,
                                                    valuetext="W-L-T", valuecolor=DARK_TAN,
                                                    row=11, max_row=16, col=5, max_col=10, maxWidth=620)
        self.next_round_button = TextButton("OUT3", (0, 0,), (265, 64), (356, 64), "-next round-",
                                            fontsize=32,
                                            textcolor=GHOST_WHITE, row=13, max_row=16, col=5, max_col=10,
                                            maxWidth=620)
        self.home_menu_button = TextButton("OUT1", (0, 0), (256, 64), (256, 64), "Home menu for a new game.",
                                           fontsize=32,
                                           textcolor=GHOST_WHITE, row=14, max_row=16, col=5, max_col=10,
                                           maxWidth=620)
        self.exit_button = TextButton("OUT2", (0, 0), (256, 64), (256, 64), "Quit", fontsize=32,
                                      textcolor=GHOST_WHITE, row=15, max_row=16, col=5, max_col=10,
                                      maxWidth=620)
        self.all_buttons.append(self.players_winlosstie_button)
        self.all_buttons.append(self.enemys_winlosstie_button)
        self.all_buttons.append(self.next_round_button)
        self.all_buttons.append(self.home_menu_button)
        self.all_buttons.append(self.exit_button)
    
    def startup(self, persistent):
        if "Player's Party" in persistent:
            self.players_party = persistent["Player's Party"]
        if "Enemy's Party" in persistent:
            self.enemys_party = persistent["Enemy's Party"]
        for pc in self.players_party:
            pc.hasBattled = False
            self.playerWLT[0] += pc.win_score
            self.playerWLT[1] += pc.loss_score
            self.playerWLT[2] += pc.tie_score
        for ec in self.enemys_party:
            ec.hasBattled = False
            self.enemyWLT[0] += ec.win_score
            self.enemyWLT[1] += ec.loss_score
            self.enemyWLT[2] += ec.tie_score
        self.players_winlosstie_button.update_button_text(self.playerWLT)
        self.enemys_winlosstie_button.update_button_text(self.enemyWLT)
        super(OutcomeMenu, self).startup(persistent)
    
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            pass
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.home_menu_button.rect.collidepoint(self.mouse_pos):
                self.persist = {
                
                }
                self.next_state_name = "HOME_MENU"
                self.done = True
            if self.exit_button.rect.collidepoint(self.mouse_pos):
                self.quit = True
        
        super(OutcomeMenu, self).get_event(event)
    
    def update(self, dt):
        super(OutcomeMenu, self).update(dt)
    
    def draw(self, surface: pg.Surface):
        surface.fill(DARK_GREEN)
        super(OutcomeMenu, self).draw(surface)
