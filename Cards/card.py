import os.path

from GUI.button import Button
from settings import *


class Card(Button):
    def __init__(self, card_data_dict: dict, col=0, max_col=0, row=0, max_row=0):
        """
        Represents an Action, Character, or Equipment.
        :param card_data_dict: Dictionary of card data, containing name, VFD-score, class title and whatnot
        :param col: column of the button grid
        :param max_col: max column for the button grid
        :param row: row for the button grid
        :param max_row: max row of the button grid
        """
        super(Card, self).__init__(card_data_dict["Name"], (0, 0), (128, 128), (128, 128),
                                   col=col, max_col=max_col, row=row, max_row=max_row)
        
        self.name = "Elira"
        self.creation_number = 420069
        self.number_list = list(str(self.creation_number))
        self.card_type = "ACE"
        self.class_group = "Melee"
        self.class_title = "Soldier"
        self.class_color = VITALITY_RED
        self.sourceFileDir = os.path.dirname(os.path.abspath(__file__))
        self.spritesPath = os.path.join(self.sourceFileDir, "assets/sprites")
        
        self.isFaceUp = True
        self.front_image = pg.Surface((128, 128))
        self.back_image = pg.Surface((128, 128))
        self.selectable = True
        self.selected = False
        
    def addImageLayer(self, baseImg: pg.Surface, layerName="", layerNum=0, color=BLANCHED_ALMOND) -> pg.Surface:
        layerImg = pg.image.load(os.path.join(self.spritesPath, f'{layerName}{layerNum}.png')).convert_alpha()
        layerColor = pg.Surface((128, 128))
        layerColor.fill(color)
        layerImg.blit(layerColor, (0, 0), special_flags=pg.BLEND_RGB_MULT)
        baseImg.blit(layerImg, (0, 0))
        return baseImg
    
    def update(self):
        super(Card, self).update()

    def draw(self, window):
        super(Card, self).draw(window)
        if self.selected:
            pg.draw.rect(window, GREY25, self.rect, 4)
            
    def flip_card(self):
        self.isFaceUp = not self.isFaceUp
        if self.isFaceUp:
            self.image = self.front_image
        else:
            self.image = self.back_image
            