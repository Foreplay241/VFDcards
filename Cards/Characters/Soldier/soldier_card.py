from enum import Enum
import pygame as pg

from Cards.character_card import Character


class Soldier(Character):
    def __init__(self, card_data_dict: dict, col=0, max_col=0, row=0, max_row=0):
        super(Soldier, self).__init__(card_data_dict, col=col, max_col=max_col, row=row, max_row=max_row)
        self.RANK_DICT = {
            "Zero": {
                "Vitality": ["Soldier", [5, 0, 0]]
            },
            "One": {
                "Vitality": ["Warrior", [6, 2, 0]],
                "Finesse": ["Brawler", [5, 3, 0]],
                "Divination": ["Spell-sword", [5, 1, 2]]
            },
            "Two": {
                "Vitality": ["Gladiator", [7, 4, 0]],
                "Finesse": ["Rogue", [6, 4, 1]],
                "Divination": ["Templar", [6, 2, 3]]
            },
            "Three": {
                "Vitality": ["Knight", [8, 6, 0]],
                "Finesse": ["Samurai", [6, 7, 1]],
                "Divination": ["Paladin", [7, 3, 4]]
            },
            "Four": {
                "Vitality": ["Berserker", [9, 8, 0]],
                "Finesse": ["Dragoon", [8, 8, 1]],
                "Divination": ["Rune-master", [8, 4, 5]]
            }
        }
        self.PRIMARY_VFD = "Vitality"
        self.chosen_VFD = self.PRIMARY_VFD
        self.vitality = 5
        self.finesse = 0
        self.divination = 0
        self.class_color = pg.Color((int(self.vitality * 28.33),
                                     int(self.finesse * 28.33),
                                     int(self.divination * 28.33),
                                     ))
        self.front_image = self.generateTriblock(self.PRIMARY_VFD)
        self.back_image.fill(self.class_color)

    def win(self):
        super(Soldier, self).win()

    def lose(self):
        super(Soldier, self).lose()

    def tie(self):
        super(Soldier, self).tie()
