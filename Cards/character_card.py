from Cards.card import Card
from settings import *
import os


class Character(Card):
    def __init__(self, name: str, creation_number: int, class_group: str, card_type: str,
                 col=0, max_col=0, row=0, max_row=0):
        super(Character, self).__init__(name, creation_number, class_group, card_type,
                                        col=col, max_col=max_col, row=row, max_row=max_row)
        self.hasBattled = False
        self.isWinner = False

    def switch_to(self, new_VFD: str):
        self.chosen_VFD = new_VFD
        self.update_image(self.generateImg(), pg.Surface((0, 0)))

    def update_VFD_score(self, VFDscore):
        self.card_data["Vitality"] = VFDscore[0]
        self.card_data["Finesse"] = VFDscore[1]
        self.card_data["Divination"] = VFDscore[2]

    def lost_battle(self):
        self.kill()
