from enum import Enum

from Cards.character_card import Character


class Seer(Character):
    class RANK1(Enum):
        CLERIC = [3, 0, 5]
        MAGE = [0, 3, 5]
        PRIEST = [2, 0, 6]

    class RANK2(Enum):
        BATTLEMAGE = [4, 1, 6]
        DRUID = [0, 5, 6]
        ELEMENTALIST = [3, 1, 7]

    class RANK3(Enum):
        MONK = [5, 3, 6]
        SHAMAN = [1, 6, 7]
        BISHOP = [3, 3, 8]

    class RANK4(Enum):
        WARLOCK = [7, 4, 6]
        BARD = [2, 8, 7]
        WIZARD = [4, 4, 9]

    def __init__(self, card_data_dict: dict, col=0, max_col=0, row=0, max_row=0):
        super(Seer, self).__init__(card_data_dict, col=col, max_col=max_col, row=row, max_row=max_row)
        self.PRIMARY_VFD = "Divination"
        self.chosen_VFD = self.PRIMARY_VFD
        self.card_data["Vitality"] = 0
        self.card_data["Finesse"] = 0
        self.card_data["Divination"] = 5

    def win(self):
        super(Seer, self).win()
        
    def lose(self):
        super(Seer, self).lose()
        
    def tie(self):
        super(Seer, self).tie()
        