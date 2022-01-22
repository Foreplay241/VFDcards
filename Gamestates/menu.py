from Gamestates.gamestate import GameState
from settings import *


def generate_new_card_data(name="Elira Jinmop", creation_time=420069,
                           class_group="Melee", card_type="ACE?") -> dict:
    new_card_data = {"Name": name, "Creation Number": creation_time,
                     "Class Group": class_group, "Card Type": card_type}
    creation_num_list = []
    for i in map(int, str(creation_time)):
        creation_num_list.append(i)
    creation_num_list.sort()
    new_card_data["Number List"] = creation_num_list
    new_card_data["Class Digit"] = creation_num_list[0]
    new_card_data["Class Title"] = CLASS_DICT[class_group][creation_num_list[0]]
    new_card_data["Class Color"] = COLOR_DICT[class_group][creation_num_list[0]]
    return new_card_data


class Menu(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        super(Menu, self).startup(persistent)

    def get_event(self, event):
        super(Menu, self).get_event(event)

    def update(self, dt):
        super(Menu, self).update(dt)

    def draw(self, surface: pg.Surface):
        super(Menu, self).draw(surface)
