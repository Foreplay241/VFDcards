import os.path
from datetime import datetime

from GUI.button import Button
from settings import *


class Card(Button):
    def __init__(self, name: str, creation_number: int, class_group: str, card_type: str,
                 col=0, max_col=0, row=0, max_row=0):
        super(Card, self).__init__(name, (0, 0), (128, 128), (128, 128),
                                   col=col, max_col=max_col, row=row, max_row=max_row)
        self.card_data = {
            "Name": name,
            "Creation Number": creation_number,
            "Class Group": class_group,
            "Card Type": card_type
        }
        x = 0
        for c in map(int, str(creation_number)):
            if x == 0:
                self.card_data["Vitality"] = c
            if x == 1:
                self.card_data["Finesse"] = c
            if x == 2:
                self.card_data["Divination"] = c
            if x == 3:
                self.card_data["Class Title"] = CLASS_DICT[class_group][c]
                self.card_data["Class Digit"] = c
            x += 1

        self.front_image = self.generateImg()
        self.back_image = pg.Surface((128, 128))
        self.back_image.fill(RANDOM_BLUE)
        self.image = self.back_image
        self.rect = self.image.get_rect()

        self.isFaceUp = False

    def addAlphaPart(self, baseImg: pg.Surface):
        x = 0
        a = 0
        r, g, b, = 0, 0, 0
        for c in map(int, str(self.card_data["Creation Number"])):
            if x == 0:
                a = c
                r = c * 11
            if x == 1:
                g = c * 15
            if x == 2:
                b = c * 19
            if x == 3:
                pass
            if x == 4:
                pass
            if x == 5:
                pass
            x += 1

        alpha_img = pg.image.load(os.path.join('Cards/Characters/Triblocks', f"alpha{a}.png")).convert_alpha()
        alpha_color = pg.Surface((128, 128))
        alpha_color.fill(COLOR_DICT[self.card_data["Class Group"]][self.card_data["Class Digit"]])
        alpha_img.blit(alpha_color, (0, 0), special_flags=pg.BLEND_RGB_MULT)
        baseImg.blit(alpha_img, (0, 0))

    def addBetaPart(self, baseImg: pg.Surface):
        x = 0
        a = 0
        r, g, b, = 0, 0, 0
        for c in map(int, str(self.card_data["Creation Number"])):
            if x == 0:
                r += c
            if x == 1:
                a = c
                g += c
            if x == 2:
                b += c
            if x == 3:
                b += c
            if x == 4:
                g += c
            if x == 5:
                r += c
            x += 1
        beta_img = pg.image.load(os.path.join('Cards/Characters/Triblocks', f"beta{a}.png")).convert_alpha()
        beta_color = pg.Surface((128, 128))
        beta_color.fill(PALE_VIOLET_RED)
        beta_img.blit(beta_color, (0, 0), special_flags=pg.BLEND_RGB_MULT)
        baseImg.blit(beta_img, (0, 0))

    def addGammaPart(self, baseImg: pg.Surface):
        x = 0
        a = 0
        r, g, b, = 0, 0, 0
        for c in map(int, str(self.card_data["Creation Number"])):
            if x == 0:
                r += c
            if x == 1:
                g += c
            if x == 2:
                a = c
                b += c
            if x == 3:
                b += c
            if x == 4:
                g += c
            if x == 5:
                r += c
            x += 1
        gamma_img = pg.image.load(os.path.join('Cards/Characters/Triblocks', f"gamma{a}.png")).convert_alpha()
        gamma_color = pg.Surface((128, 128))
        gamma_color.fill(SAGE_GREEN)
        gamma_img.blit(gamma_color, (0, 0), special_flags=pg.BLEND_RGB_MULT)
        baseImg.blit(gamma_img, (0, 0))

    def addDeltaPart(self, baseImg: pg.Surface):
        x = 0
        a = 0
        r, g, b, = 0, 0, 0
        for c in map(int, str(self.card_data["Creation Number"])):
            if x == 0:
                r += c
            if x == 1:
                g += c
            if x == 2:
                b += c
            if x == 3:
                a = c
                b += c
            if x == 4:
                g += c
            if x == 5:
                r += c
            x += 1
        delta_img = pg.image.load(os.path.join('Cards/Characters/Triblocks', f"delta{a}.png")).convert_alpha()
        delta_color = pg.Surface((128, 128))
        delta_color.fill(DARK_SLATE_BLUE)
        delta_img.blit(delta_color, (0, 0), special_flags=pg.BLEND_RGB_MULT)
        baseImg.blit(delta_img, (0, 0))

    def addEpsilonPart(self, baseImg: pg.Surface):
        x = 0
        a = 0
        r, g, b, = 0, 0, 0
        for c in map(int, str(self.card_data["Creation Number"])):
            if x == 0:
                r += c
            if x == 1:
                g += c
            if x == 2:
                b += c
            if x == 3:
                b += c
            if x == 4:
                a = c
                g += c
            if x == 5:
                r += c
            x += 1
        epsilon_img = pg.image.load(os.path.join('Cards/Characters/Triblocks', f"epsilon{a}.png")).convert_alpha()
        epsilon_color = pg.Surface((128, 128))
        epsilon_color.fill(pg.Color(r, g, b))
        epsilon_img.blit(epsilon_color, (0, 0), special_flags=pg.BLEND_RGB_MULT)
        baseImg.blit(epsilon_img, (0, 0))

    def update_triblocks(self):
        self.front_image = self.generateImg()

    def generateImg(self) -> pg.Surface:
        newImg = pg.Surface((128, 128))
        self.addAlphaPart(newImg)
        self.addBetaPart(newImg)
        self.addGammaPart(newImg)
        self.addDeltaPart(newImg)
        self.addEpsilonPart(newImg)
        return newImg

    def flip_card(self):
        self.isFaceUp = not self.isFaceUp
        if self.isFaceUp:
            self.image = self.front_image
        else:
            self.image = self.back_image

    def update(self):
        super(Card, self).update()

    def draw(self, window):
        super(Card, self).draw(window)
