from Cards.card import Card
from GUI.text import Text
from settings import *
import os


class Character(Card):
    def __init__(self, card_data_dict: dict, col=0, max_col=0, row=0, max_row=0):
        """
        Character version of a card, contains the base VFD-score
        :param card_data_dict: Dictionary of card data, containing name, VFD-score, class title and whatnot
        :param col: column of the button grid
        :param max_col: max column for the button grid
        :param row: row for the button grid
        :param max_row: max row of the button grid
        """
        super(Character, self).__init__(card_data_dict, col=col, max_col=max_col, row=row, max_row=max_row)
        self.total_score = 0
        self.win_score = 0
        self.loss_score = 0
        self.tie_score = 0
        self.win_score_text = Text(str(self.win_score), (64, 64), color=WHITE, size=16)
        self.loss_score_text = Text(str(self.loss_score), (64, 64), color=WHITE, size=16)
        self.tie_score_text = Text(str(self.tie_score), (64, 64), color=WHITE, size=16)
        self.total_score_text = Text(str(self.total_score), (64, 64), color=WHITE, size=16)
        self.card_data["Total Points"] = self.total_score
        self.card_data["Total Wins"] = self.win_score
        self.card_data["Total Loss"] = self.loss_score
        self.card_data["Total Ties"] = self.tie_score
        self.hasBattled = False
        self.isWinner = False

    def update(self):
        super(Character, self).update()

    def display_score(self, WLT: str):
        score_text = self.total_score_text
        score_text.render(str([self.win_score, self.loss_score, self.tie_score]))
        if self.card_data[""]
        self.image.blit(score_text.img, (46, 64))

    def adjust_VFD(self, VFD: str, new_value: int):
        self.card_data[VFD] = new_value

    def win(self):
        self.isWinner = True
        self.win_score += 1
        self.total_score += 1
        self.hasBattled = True
        self.display_score("win")

    def lose(self):
        self.isWinner = False
        self.loss_score += 1
        self.total_score += 1
        self.hasBattled = True
        self.display_score("loss")
        
    def tie(self):
        self.tie_score += 1
        self.total_score += 1
        self.hasBattled = True
        self.display_score("tie")

    def switch_skill_to(self, new_VFD: str):
        self.chosen_VFD = new_VFD
        self.update_image(self.generateImg(), pg.Surface((0, 0)))

    def flip_card(self):
        super(Character, self).flip_card()
        