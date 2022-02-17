from enum import Enum

from Cards.character_card import Character


class Soldier(Character):
    class RANK1(Enum):
        WARRIOR = ["Warrior", [6, 2, 0]]
        BRAWLER = ["Brawler", [5, 3, 0]]
        SPELLSWORD = ["Spellsword", [5, 1, 2]]

    class RANK2(Enum):
        GLADIATOR = [7, 4, 0]
        ROGUE = [6, 4, 1]
        TEMPLAR = [6, 2, 3]

    class RANK3(Enum):
        KNIGHT = [8, 6, 0]
        SAMURAI = [6, 7, 1]
        PALADIN = [7, 3, 4]

    class RANK4(Enum):
        BERSERKER = [9, 8, 0]
        DRAGOON = [8, 8, 1]
        RUNEMASTER = [8, 4, 3]

    def __init__(self, card_data_dict: dict, col=0, max_col=0, row=0, max_row=0):
        super(Soldier, self).__init__(card_data_dict, col=col, max_col=max_col, row=row, max_row=max_row)
        self.PRIMARY_VFD = "Vitality"
        self.chosen_VFD = self.PRIMARY_VFD
        self.card_data["Vitality"] = 5
        self.card_data["Finesse"] = 0
        self.card_data["Divination"] = 0

    def win(self):
        super(Soldier, self).win()

    def lose(self):
        super(Soldier, self).lose()

    def tie(self):
        super(Soldier, self).tie()
