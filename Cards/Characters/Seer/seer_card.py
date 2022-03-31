from enum import Enum
import pygame as pg
from Cards.character_card import Character


class Seer(Character):
    def __init__(self, card_data_dict: dict, col=0, max_col=0, row=0, max_row=0):
        super(Seer, self).__init__(card_data_dict, col=col, max_col=max_col, row=row, max_row=max_row)
        self.RANK_DICT = {
            "Zero": {
                "Divination": ["Seer", [0, 0, 5]]
            },
            "One": {
                "Vitality": ["Cleric", [2, 1, 5]],
                "Finesse": ["Mage", [0, 3, 5]],
                "Divination": ["Priest", [1, 1, 6]]
            },
            "Two": {
                "Vitality": ["Battle-mage", [4, 1, 6]],
                "Finesse": ["Druid", [0, 5, 6]],
                "Divination": ["Elementalist", [3, 1, 7]]
            },
            "Three": {
                "Vitality": ["Monk", [5, 3, 6]],
                "Finesse": ["Shaman", [1, 6, 7]],
                "Divination": ["Bishop", [3, 3, 8]]
            },
            "Four": {
                "Vitality": ["Warlock", [7, 4, 6]],
                "Finesse": ["Bard", [2, 8, 7]],
                "Divination": ["Wizard", [4, 4, 9]]
            }
        }
        self.PRIMARY_VFD = "Divination"
        self.chosen_VFD = self.PRIMARY_VFD
        self.vitality = 0
        self.finesse = 0
        self.divination = 5
        self.class_color = pg.Color((int(self.vitality * 28.33),
                                     int(self.finesse * 28.33),
                                     int(self.divination * 28.33),
                                     ))
        self.front_image = self.generateTriblock(self.PRIMARY_VFD)
        self.back_image.fill(self.class_color)

    def win(self):
        super(Seer, self).win()
        
    def lose(self):
        super(Seer, self).lose()
        
    def tie(self):
        super(Seer, self).tie()
        