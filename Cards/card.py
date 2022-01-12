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
        self.chosen_VFD = "Vitality"

        self.front_image = self.generateImg()
        self.back_image = pg.Surface((128, 128))
        self.back_image.fill(RANDOM_BLUE)
        self.image = self.back_image
        self.rect = self.image.get_rect()

        self.isFaceUp = False
        self.selected = False

    def rotate_center(self, surf, image, pos, originPos, angle):
        img_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset_center_to_pivot = pg.math.Vector2(pos) - img_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-angle)
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
        rotated_image = pg.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
        surf.blit(rotated_image, rotated_image_rect)

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

    def addBetaPart(self, baseImg: pg.Surface, beta_digit: int, class_color: pg.Color):
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
        beta_img = pg.image.load(os.path.join('Cards/Characters/Triblocks', f"beta{beta_digit}.png")).convert_alpha()
        beta_color = pg.Surface((128, 128))
        beta_color.fill(class_color)
        beta_img.blit(beta_color, (0, 0), special_flags=pg.BLEND_RGB_MULT)
        baseImg.blit(beta_img, (0, 0))

    def addGammaPart(self, baseImg: pg.Surface, gamma_digit: int, class_color: pg.Color):
        x = 0
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
        gamma_img = pg.image.load(os.path.join('Cards/Characters/Triblocks', f"gamma{gamma_digit}.png")).convert_alpha()
        gamma_color = pg.Surface((128, 128))
        gamma_color.fill(class_color)
        gamma_img.blit(gamma_color, (0, 0), special_flags=pg.BLEND_RGB_MULT)
        baseImg.blit(gamma_img, (0, 0))

    def addDeltaPart(self, baseImg: pg.Surface, delta_digit: int, class_color: pg.Color):
        x = 0
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
        delta_img = pg.image.load(os.path.join('Cards/Characters/Triblocks', f"delta{delta_digit}.png")).convert_alpha()
        delta_color = pg.Surface((128, 128))
        delta_color.fill(class_color)
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
        epsilon_text = pg.font.Font(None, 22).render(self.card_data["Name"], True,
                                                     COLOR_DICT[random.choice(CLASS_GROUPS)][self.card_data["Class Digit"]])
        if self.card_data["Card Type"].startswith("Enemy"):
            epsilon_text = pg.transform.flip(epsilon_text, False, True)
        epsilon_color.fill(pg.Color(r, g, b))
        epsilon_img.blit(epsilon_color, (0, 0), special_flags=pg.BLEND_RGB_MULT)
        epsilon_img.blit(epsilon_text, (10, 108))
        baseImg.blit(epsilon_img, (0, 0))

    def generateImg(self) -> pg.Surface:
        newImg = pg.Surface((128, 128))
        self.addAlphaPart(newImg)
        if self.chosen_VFD == "Vitality":
            self.addBetaPart(newImg, self.card_data["Vitality"], VITALITY_RED)
            self.addGammaPart(newImg, self.card_data["Finesse"], FINESSE_GREEN)
            self.addDeltaPart(newImg, self.card_data["Divination"], DIVINATION_BLUE)
        elif self.chosen_VFD == "Finesse":
            self.addBetaPart(newImg, self.card_data["Finesse"], FINESSE_GREEN)
            self.addGammaPart(newImg, self.card_data["Divination"], DIVINATION_BLUE)
            self.addDeltaPart(newImg, self.card_data["Vitality"], VITALITY_RED)
        elif self.chosen_VFD == "Divination":
            self.addBetaPart(newImg, self.card_data["Divination"], DIVINATION_BLUE)
            self.addGammaPart(newImg, self.card_data["Vitality"], VITALITY_RED)
            self.addDeltaPart(newImg, self.card_data["Finesse"], FINESSE_GREEN)
        self.addEpsilonPart(newImg)
        return newImg

    # def generateImg(self) -> pg.Surface:
    #     newImg = pg.Surface((128, 128))
    #     self.addAlphaPart(newImg)
    #     if self.chosen_VFD == "Vitality":
    #         self.addBetaPart(newImg, self.card_data["Vitality"], COLOR_DICT["Melee"][self.card_data["Class Digit"]])
    #         self.addGammaPart(newImg, self.card_data["Finesse"], COLOR_DICT["Ranged"][self.card_data["Class Digit"]])
    #         self.addDeltaPart(newImg, self.card_data["Divination"], COLOR_DICT["Magic"][self.card_data["Class Digit"]])
    #     elif self.chosen_VFD == "Finesse":
    #         self.addBetaPart(newImg, self.card_data["Finesse"], COLOR_DICT["Ranged"][self.card_data["Class Digit"]])
    #         self.addGammaPart(newImg, self.card_data["Divination"], COLOR_DICT["Magic"][self.card_data["Class Digit"]])
    #         self.addDeltaPart(newImg, self.card_data["Vitality"], COLOR_DICT["Melee"][self.card_data["Class Digit"]])
    #     elif self.chosen_VFD == "Divination":
    #         self.addBetaPart(newImg, self.card_data["Divination"], COLOR_DICT["Magic"][self.card_data["Class Digit"]])
    #         self.addGammaPart(newImg, self.card_data["Vitality"], COLOR_DICT["Melee"][self.card_data["Class Digit"]])
    #         self.addDeltaPart(newImg, self.card_data["Finesse"], COLOR_DICT["Ranged"][self.card_data["Class Digit"]])
    #     self.addEpsilonPart(newImg)
    #     return newImg

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
        if self.selected:
            pg.draw.rect(window, GREY25, self.rect, 4)
