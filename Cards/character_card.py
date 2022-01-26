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
        self.total_score_text = Text(str(self.total_score), (64, 64), color=WHITE, size=16)
        # print("+================+")
        if self.card_data["Class Group"] == "Melee":
            self.chosen_VFD = "Vitality"
            self.card_data["Vitality"] = self.card_data["Number List"][5]
            self.card_data["Finesse"] = self.card_data["Number List"][4]
            self.card_data["Divination"] = self.card_data["Number List"][3]
        if self.card_data["Class Group"] == "Ranged":
            self.chosen_VFD = "Finesse"
            self.card_data["Vitality"] = self.card_data["Number List"][3]
            self.card_data["Finesse"] = self.card_data["Number List"][5]
            self.card_data["Divination"] = self.card_data["Number List"][4]
        if self.card_data["Class Group"] == "Magic":
            self.chosen_VFD = "Divination"
            self.card_data["Vitality"] = self.card_data["Number List"][4]
            self.card_data["Finesse"] = self.card_data["Number List"][3]
            self.card_data["Divination"] = self.card_data["Number List"][5]
        self.card_data["Total Points"] = 0
        self.hasBattled = False
        self.isWinner = False

    def update(self):
        super(Character, self).update()

    def display_total_score(self):
        self.image.blit(self.total_score_text.img, (64, 64))

    def win(self, gain_points: int):
        self.hasBattled = True
        self.isWinner = True
        self.card_data["Total Points"] += gain_points
        self.update_image(self.generateImg(), self.generateImg())
        self.total_score_text.text = str(self.card_data["Total Points"])
        self.total_score_text.render()
        self.display_total_score()

    def lose(self):
        self.hasBattled = True
        self.isWinner = False
        self.flip_card()

    def switch_to(self, new_VFD: str):
        self.chosen_VFD = new_VFD
        self.update_image(self.generateImg(), pg.Surface((0, 0)))
