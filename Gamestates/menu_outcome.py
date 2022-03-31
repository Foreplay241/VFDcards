from Cards.card import Card
from Cards.character_card import Character
from GUI.button import Button
from GUI.text_button import TextButton
from Gamestates.menu import Menu, generate_new_card_data
from settings import *
import pygame as pg


# TODO ADVANCE TO NEXT RANK

class OutcomeMenu(Menu):
    def __init__(self):
        super(OutcomeMenu, self).__init__()
        self.curr_char = None
        self.enemys_party = None
        self.players_party = None
        self.playerWLT = [0, 0, 0]
        self.enemyWLT = [0, 0, 0]
        self.name_buttons = []
        self.first_enemy_name_button = TextButton("OUT0", (0, 0,), (64, 64), (64, 64), "E-name1",
                                                  textcolor=GHOST_WHITE, row=0, max_row=16, col=1, max_col=4,
                                                  maxWidth=100)
        self.second_enemy_name_button = TextButton("OUT1", (0, 0,), (64, 64), (64, 64), "E-name2",
                                                   textcolor=GHOST_WHITE, row=0, max_row=16, col=2, max_col=4,
                                                   maxWidth=100)
        self.third_enemy_name_button = TextButton("OUT2", (0, 0,), (64, 64), (64, 64), "E-name3",
                                                  textcolor=GHOST_WHITE, row=0, max_row=16, col=3, max_col=4,
                                                  maxWidth=100)
        self.first_enemy_character_card = Button("OUT3", (0, 0), (128, 128), (128, 128),
                                                 col=1, max_col=4, row=1, max_row=16)
        self.second_enemy_character_card = Button("OUT4", (0, 0), (128, 128), (128, 128),
                                                  col=2, max_col=4, row=1, max_row=16)
        self.third_enemy_character_card = Button("OUT5", (0, 0), (128, 128), (128, 128),
                                                 col=3, max_col=4, row=1, max_row=16)
        self.enemys_winlosstie_button = TextButton("OUT6", (0, 0), (256, 64), (256, 64), "Win-Loss-Tie",
                                                   textcolor=DARK_TURQUOISE,
                                                   optiontext="Enemy", optioncolor=INDIAN_RED,
                                                   valuetext="W-L-T", valuecolor=DARK_TAN,
                                                   row=5, max_row=16, col=5, max_col=10, maxWidth=620)
        self.first_player_name_button = TextButton("OUT7", (0, 0,), (64, 64), (64, 64), "P-name1",
                                                   textcolor=GHOST_WHITE, row=7, max_row=16, col=1, max_col=4,
                                                   maxWidth=100)
        self.second_player_name_button = TextButton("OUT8", (0, 0,), (64, 64), (64, 64), "P-name2",
                                                    textcolor=GHOST_WHITE, row=7, max_row=16, col=2, max_col=4,
                                                    maxWidth=100)
        self.third_player_name_button = TextButton("OUT9", (0, 0,), (64, 64), (64, 64), "P-name3",
                                                   textcolor=GHOST_WHITE, row=7, max_row=16, col=3, max_col=4,
                                                   maxWidth=100)
        self.first_player_character_card = Button("OUT10", (0, 0), (128, 128), (128, 128),
                                                  col=1, max_col=4, row=8, max_row=16)
        self.second_player_character_card = Button("OUT11", (0, 0), (128, 128), (128, 128),
                                                   col=2, max_col=4, row=8, max_row=16)
        self.third_player_character_card = Button("OUT12", (0, 0), (128, 128), (128, 128),
                                                  col=3, max_col=4, row=8, max_row=16)
        self.first_pc_next_rank = ""
        self.second_pc_next_rank = ""
        self.third_pc_next_rank = ""
        
        self.players_winlosstie_button = TextButton("OUT13", (0, 0), (256, 64), (256, 64), "Win-Loss-Tie",
                                                    textcolor=DARK_TURQUOISE,
                                                    optiontext="Player", optioncolor=LAWN_GREEN,
                                                    valuetext="W-L-T", valuecolor=DARK_TAN,
                                                    row=12, max_row=16, col=5, max_col=10, maxWidth=620)
        self.next_round_button = TextButton("OUT14", (0, 0,), (265, 64), (356, 64), "-next round-",
                                            fontsize=32,
                                            textcolor=GHOST_WHITE, row=14, max_row=16, col=5, max_col=10,
                                            maxWidth=520)
        self.home_menu_button = TextButton("OUT15", (0, 0), (256, 64), (256, 64), "Home menu",
                                           fontsize=32,
                                           textcolor=GHOST_WHITE, row=15, max_row=16, col=1, max_col=3,
                                           maxWidth=155)
        self.exit_button = TextButton("OUT16", (0, 0), (256, 64), (256, 64), "Quit", fontsize=32,
                                      textcolor=GHOST_WHITE, row=15, max_row=16, col=2, max_col=3,
                                      maxWidth=155)
        
        # ADD CARD BUTTONS TO CARD BUTTON LIST
        self.card_buttons.append(self.first_enemy_character_card)
        self.card_buttons.append(self.second_enemy_character_card)
        self.card_buttons.append(self.third_enemy_character_card)
        self.card_buttons.append(self.first_player_character_card)
        self.card_buttons.append(self.second_player_character_card)
        self.card_buttons.append(self.third_player_character_card)
        
        # ADD NAME BUTTONS TO NAME BUTTON LIST
        self.name_buttons.append(self.first_enemy_name_button)
        self.name_buttons.append(self.second_enemy_name_button)
        self.name_buttons.append(self.third_enemy_name_button)
        self.name_buttons.append(self.first_player_name_button)
        self.name_buttons.append(self.second_player_name_button)
        self.name_buttons.append(self.third_player_name_button)
        
        # ADD TEXT BUTTONS
        self.text_buttons.append(self.players_winlosstie_button)
        self.text_buttons.append(self.enemys_winlosstie_button)
        self.text_buttons.append(self.next_round_button)
        self.text_buttons.append(self.home_menu_button)
        self.text_buttons.append(self.exit_button)
        
        # ADD ALL BUTTONS TO ALL BUTTON LIST
        self.add_all_buttons([self.name_buttons, self.card_buttons, self.text_buttons])
    
    def startup(self, persistent):
        if "Player's Party" in persistent:
            self.players_party = persistent["Player's Party"]
            self.first_player_name_button.update_button_text(self.players_party[0].name)
            self.second_player_name_button.update_button_text(self.players_party[1].name)
            self.third_player_name_button.update_button_text(self.players_party[2].name)
        if "Enemy's Party" in persistent:
            self.enemys_party = persistent["Enemy's Party"]
            self.first_enemy_name_button.update_button_text(self.enemys_party[0].name)
            self.second_enemy_name_button.update_button_text(self.enemys_party[1].name)
            self.third_enemy_name_button.update_button_text(self.enemys_party[2].name)
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
            for cb in self.card_buttons:
                cb.selected = False
                if cb.rect.collidepoint(self.mouse_pos):
                    cb.selected = True
            if self.first_player_name_button.rect.collidepoint(self.mouse_pos):
                self.curr_char = self.players_party[0]
                self.first_player_name_button.active = True
                self.second_player_name_button.active = False
                self.third_player_name_button.active = False
                self.update_next_rank_buttons("One", self.curr_char)
            if self.second_player_name_button.rect.collidepoint(self.mouse_pos):
                self.curr_char = self.players_party[1]
                self.first_player_name_button.active = False
                self.second_player_name_button.active = True
                self.third_player_name_button.active = False
                self.update_next_rank_buttons("One", self.curr_char)
            if self.third_player_name_button.rect.collidepoint(self.mouse_pos):
                self.curr_char = self.players_party[2]
                self.first_player_name_button.active = False
                self.second_player_name_button.active = False
                self.third_player_name_button.active = True
                self.update_next_rank_buttons("One", self.curr_char)
            if self.first_player_character_card.rect.collidepoint(self.mouse_pos) and self.curr_char:
                self.curr_char.next_class_title = self.first_pc_next_rank
                self.first_player_character_card.selected = True
                self.second_player_character_card.selected = False
                self.third_player_character_card.selected = False
                for nameBTN in self.name_buttons:
                    if nameBTN.active:
                        nameBTN.set_button_option(WHITE, self.curr_char.name)
                        nameBTN.set_button_value(self.curr_char.class_color,
                                                 self.curr_char.next_class_title)
                        nameBTN.update_button_text("")
            if self.second_player_character_card.rect.collidepoint(self.mouse_pos) and self.curr_char:
                self.curr_char.next_class_title = self.second_pc_next_rank
                self.first_player_character_card.selected = False
                self.second_player_character_card.selected = True
                self.third_player_character_card.selected = False
                for nameBTN in self.name_buttons:
                    if nameBTN.active:
                        nameBTN.set_button_option(WHITE, self.curr_char.name)
                        nameBTN.set_button_value(self.curr_char.class_color,
                                                 self.curr_char.next_class_title)
                        nameBTN.update_button_text("")
            if self.third_player_character_card.rect.collidepoint(self.mouse_pos) and self.curr_char:
                self.curr_char.next_class_title = self.third_pc_next_rank
                self.first_player_character_card.selected = False
                self.second_player_character_card.selected = False
                self.third_player_character_card.selected = True
                for nameBTN in self.name_buttons:
                    if nameBTN.active:
                        nameBTN.set_button_option(WHITE, self.curr_char.name)
                        nameBTN.set_button_value(self.curr_char.class_color,
                                                 self.curr_char.next_class_title)
                        nameBTN.update_button_text("")
            if self.next_round_button.rect.collidepoint(self.mouse_pos):
                self.persist = {
                    "Player's Party": self.players_party,
                    "Enemy's Party": self.enemys_party
                }
                print(self.persist)
                self.next_state_name = "GAME"
                self.done = True
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
    
    def upgrade_character(self, new_rank: str) -> Character:
        pass
    
    def update_next_rank_buttons(self, rank: str, current_character: Character):
        self.first_player_character_card.update_image(current_character.generateNextRank(rank, "Vitality"),
                                                      pg.Surface((0, 0)))
        self.first_pc_next_rank = current_character.RANK_DICT[rank]["Vitality"][0]
        self.second_player_character_card.update_image(current_character.generateNextRank(rank, "Finesse"),
                                                       pg.Surface((0, 0)))
        self.second_pc_next_rank = current_character.RANK_DICT[rank]["Finesse"][0]
        self.third_player_character_card.update_image(current_character.generateNextRank(rank, "Divination"),
                                                      pg.Surface((0, 0)))
        self.third_pc_next_rank = current_character.RANK_DICT[rank]["Divination"][0]
        # pg.display.flip()
