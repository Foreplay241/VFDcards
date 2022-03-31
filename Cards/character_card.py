from enum import Enum

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
        self.vitality = 0
        self.finesse = 0
        self.divination = 0
        self.total_score = 0
        self.win_score = 0
        self.loss_score = 0
        self.tie_score = 0
        self.rankStr = "Zero"
        self.RANK_DICT = {
            "Zero": {
                "Vitality": ["Soldier", [5, 0, 0]],
                "Finesse": ["Ranger", [0, 5, 0]],
                "Divination": ["Seer", [0, 0, 5]]
            }
        }
        self.win_score_text = Text(str(self.win_score), (64, 64), color=WHITE, size=16)
        self.loss_score_text = Text(str(self.loss_score), (64, 64), color=WHITE, size=16)
        self.tie_score_text = Text(str(self.tie_score), (64, 64), color=WHITE, size=16)
        self.total_score_text = Text(str(self.total_score), (64, 64), color=WHITE, size=16)
        self.hasBattled = False
        self.isWinner = False
        self.next_class_title = "None"
        self.PRIMARY_VFD = None
        self.chosen_VFD = None
        self.spritesPath = os.path.join(self.spritesPath, "Triblocs")
        self.class_color = pg.Color((int(self.vitality * 28.33),
                                     int(self.finesse * 28.33),
                                     int(self.divination * 28.33),
                                     ))
    
    def update(self):
        super(Character, self).update()
    
    def display_score(self):
        score_text = self.total_score_text
        score_text.render(str([self.win_score, self.loss_score, self.tie_score]))
        if self.card_type.startswith("Enemy"):
            self.image.blit(score_text.img, (46, 64))
        else:
            self.image.blit(score_text.img, (46, 52))
    
    def adjust_VFD(self, VFD_score: list):
        self.vitality = VFD_score[0]
        self.finesse = VFD_score[1]
        self.divination = VFD_score[2]
        self.class_color = (pg.Color(int(VFD_score[0] * 28.33),
                                     int(VFD_score[1] * 28.33),
                                     int(VFD_score[2] * 28.33), ))
    
    def win(self):
        self.isWinner = True
        self.win_score += 1
        self.total_score += 1
        self.hasBattled = True
        self.switch_skill_to(self.chosen_VFD)
        # self.front_image = pg.transform.flip(self.front_image, False, True)
        self.display_score()
    
    def lose(self):
        self.isWinner = False
        self.loss_score += 1
        self.total_score += 1
        self.hasBattled = True
        self.switch_skill_to(self.chosen_VFD)
        # self.front_image = pg.transform.flip(self.front_image, False, True)
        self.display_score()
    
    def tie(self):
        self.tie_score += 1
        self.total_score += 1
        self.hasBattled = True
        self.switch_skill_to(self.chosen_VFD)
        self.front_image = pg.transform.flip(self.front_image, False, True)
        self.display_score()
    
    def switch_skill_to(self, new_VFD: str):
        self.chosen_VFD = new_VFD
        self.update_image(self.generateTriblock(self.chosen_VFD), pg.Surface((0, 0)))
    
    def generateNextRank(self, next_rank: str, vfd_option: str) -> pg.Surface:
        self.adjust_VFD(self.RANK_DICT[next_rank][vfd_option][1])
        self.class_title = self.RANK_DICT[next_rank][vfd_option][0]
        self.switch_skill_to(vfd_option)
        return self.generateTriblock(vfd_option)
    
    def generateTriblock(self, chosenVFD: str):
        newImg = pg.Surface((128, 128))
        newImg.fill(self.class_color)
        if chosenVFD == "Vitality":
            self.addImageLayer(newImg, layerName='botlo', layerNum=self.finesse, color=FINESSE_GREEN)
            self.addImageLayer(newImg, layerName='rigo', layerNum=self.divination, color=DIVINATION_BLUE)
            self.addImageLayer(newImg, layerName='topo', layerNum=self.vitality, color=VITALITY_RED)
        elif chosenVFD == "Finesse":
            self.addImageLayer(newImg, layerName='botlo', layerNum=self.divination, color=DIVINATION_BLUE)
            self.addImageLayer(newImg, layerName='rigo', layerNum=self.vitality, color=VITALITY_RED)
            self.addImageLayer(newImg, layerName='topo', layerNum=self.finesse, color=FINESSE_GREEN)
        elif chosenVFD == "Divination":
            self.addImageLayer(newImg, layerName='botlo', layerNum=self.vitality, color=VITALITY_RED)
            self.addImageLayer(newImg, layerName='rigo', layerNum=self.finesse, color=FINESSE_GREEN)
            self.addImageLayer(newImg, layerName='topo', layerNum=self.divination, color=DIVINATION_BLUE)
        return newImg
