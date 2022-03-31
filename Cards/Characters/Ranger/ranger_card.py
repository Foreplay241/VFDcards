from Cards.character_card import Character
from enum import Enum
import pygame as pg


class Ranger(Character):
        
    def __init__(self, card_data_dict: dict, col=0, max_col=0, row=0, max_row=0):
        super(Ranger, self).__init__(card_data_dict, col=col, max_col=max_col, row=row, max_row=max_row)
        self.RANK_DICT = {
            "Zero": {
                "Finesse": ["Ranger", [0, 5, 0]]
            },
            "One": {
                "Vitality": ["Slinger", [3, 5, 0]],
                "Finesse": ["Archer", [1, 6, 1]],
                "Divination": ["Witch", [1, 5, 2]]
            },
            "Two": {
                "Vitality": ["Assassin", [5, 6, 0]],
                "Finesse": ["Hunter", [2, 7, 2]],
                "Divination": ["Necromancer", [2, 6, 3]]
            },
            "Three": {
                "Vitality": ["Ninja", [7, 7, 0]],
                "Finesse": ["Beast-master", [3, 8, 3]],
                "Divination": ["Spellbow", [3, 6, 5]]
            },
            "Four": {
                "Vitality": ["Ax-thrower", [8, 9, 0]],
                "Finesse": ["Eagle-eye", [4, 9, 4]],
                "Divination": ["Arch-Mage", [3, 7, 7]]
            }
        }
        self.PRIMARY_VFD = "Finesse"
        self.chosen_VFD = self.PRIMARY_VFD
        self.vitality = 0
        self.finesse = 5
        self.divination = 0
        self.class_color = pg.Color((int(self.vitality * 28.33),
                                     int(self.finesse * 28.33),
                                     int(self.divination * 28.33)))
        self.front_image = self.generateTriblock(self.PRIMARY_VFD)
        self.back_image.fill(self.class_color)
    
    def win(self):
        super(Ranger, self).win()
    
    def lose(self):
        super(Ranger, self).lose()
    
    def tie(self):
        super(Ranger, self).tie()
        
        