from Cards.card import Card
from settings import *
import os


class Character(Card):
    def __init__(self, card_data_dict: dict,
                 col=0, max_col=0, row=0, max_row=0):
        super(Character, self).__init__(card_data_dict, col=col, max_col=max_col, row=row, max_row=max_row)
        print("+================+")
        print(self.card_data)
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
        self.hasBattled = False
        self.isWinner = False

    def update(self):
        super(Character, self).update()

    def switch_to(self, new_VFD: str):
        self.chosen_VFD = new_VFD
        self.update_image(self.generateImg(), pg.Surface((0, 0)))
