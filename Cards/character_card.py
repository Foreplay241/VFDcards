from Cards.card import Card
from settings import *
import os


class Character(Card):
    def __init__(self, name: str, creation_number: int, class_group: str, card_type: str,
                 col=0, max_col=0, row=0, max_row=0):
        super(Character, self).__init__(name, creation_number, class_group, card_type,
                                        col=col, max_col=max_col, row=row, max_row=max_row)

    def rotate_center(self, surf, image, pos, originPos, angle):
        img_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset_center_to_pivot = pg.math.Vector2(pos) - img_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-angle)
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
        rotated_image = pg.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
        surf.blit(rotated_image, rotated_image_rect)

    def update_VFD_score(self, VFDscore):
        self.card_data["Vitality"] = VFDscore[0]
        self.card_data["Finesse"] = VFDscore[1]
        self.card_data["Divination"] = VFDscore[2]
