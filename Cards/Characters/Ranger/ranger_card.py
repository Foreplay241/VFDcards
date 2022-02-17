from Cards.character_card import Character
from enum import Enum


class Ranger(Character):
    class RANK1(Enum):
        SLINGER = [3, 5, 0]
        ARCHER = [1, 6, 1]
        WITCH = [1, 5, 2]

    class RANK2(Enum):
        ASSASSIN = [5, 6, 0]
        HUNTER = [2, 7, 2]
        NECROMANCER = [2, 6, 3]

    class RANK3(Enum):
        NINJA = [7, 7, 0]
        BEASTMASTER = [3, 8, 3]
        SPELLBOW = [3, 6, 5]

    class RANK4(Enum):
        AXTHROWER = [8, 9, 0]
        EAGLEEYE = [4, 9, 4]
        ARCHMAGE = [3, 7, 7]

    def __init__(self, card_data_dict: dict, col=0, max_col=0, row=0, max_row=0):
        super(Ranger, self).__init__(card_data_dict, col=col, max_col=max_col, row=row, max_row=max_row)
        self.PRIMARY_VFD = "Finesse"
        self.chosen_VFD = self.PRIMARY_VFD
        self.card_data["Vitality"] = 0
        self.card_data["Finesse"] = 5
        self.card_data["Divination"] = 0

    def win(self):
        super(Ranger, self).win()

    def lose(self):
        super(Ranger, self).lose()

    def tie(self):
        super(Ranger, self).tie()
