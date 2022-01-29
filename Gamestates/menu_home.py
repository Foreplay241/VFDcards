import os
import random
from datetime import datetime

from Cards import card
from GUI.button import Button
from GUI.text import Text
from GUI.text_button import TextButton
from Gamestates.menu import Menu
from settings import *


def add_character_to_party(character_card_data: dict, party: list):
    party.append(character_card_data)


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


def generate_tutorial_team(team_size=3) -> []:
    character_list = [
        generate_new_card_data(name="GorKil", creation_time=234567, card_type="Character", class_group="Melee"),
        generate_new_card_data(name="RaGuh", creation_time=543210, card_type="Character", class_group="Ranged"),
        generate_new_card_data(name="MerRoni", creation_time=987654, card_type="Character", class_group="Magic")
    ]
    return character_list


def generate_random_team(team_size=3) -> []:
    character_list = []
    for i in range(team_size):
        new_character_data = generate_new_card_data(name=random.choice(EXAMPLE_NAMES),
                                                    creation_time=random.randint(100000, 999999),
                                                    card_type="Character",
                                                    class_group=random.choice(CLASS_GROUPS))
        character_list.append(new_character_data)
    return character_list


class HomeMenu(Menu):
    def __init__(self):
        super(HomeMenu, self).__init__()

        self.player_character_list = []
        self.enemy_character_list = []
        self.card_buttons = []
        self.max_party_size = 3
        self.generate_random_team_button = TextButton("H8", (0, 0), (128, 128), (128, 128), text="Generate Random Team",
                                                      textcolor=CORN_FLOWER_BLUE, bgColor=SPACE_GREY,
                                                      optiontext="", optioncolor=LIGHT_SLATE_BLUE, fontsize=22,
                                                      col=1, max_col=2, row=2, max_row=12, maxWidth=210)
        self.first_character_card = Button("H4", (0, 0), (128, 128), (128, 128),
                                           col=1, max_col=4, row=4, max_row=12)
        self.second_character_card = Button("H5", (0, 0), (128, 128), (128, 128),
                                            col=2, max_col=4, row=4, max_row=12)
        self.third_character_card = Button("H6", (0, 0), (128, 128), (128, 128),
                                           col=3, max_col=4, row=4, max_row=12)
        self.enter_battle_button = TextButton("H7", (0, 0), (0, 0), (0, 0),
                                              text=f"Enter game",
                                              textcolor=WHITE_SMOKE, bgColor=SPACE_GREY,
                                              optiontext="", optioncolor=LIGHT_SLATE_BLUE, fontsize=22,
                                              col=1, max_col=2, row=7, max_row=12, maxWidth=420)
        self.enter_tutorial_button = TextButton("H7", (0, 0), (0, 0), (0, 0),
                                                text=f"Tutorial",
                                                textcolor=MUSTARD_YELLOW, bgColor=SPACE_GREY,
                                                optiontext="", optioncolor=LIGHT_SLATE_BLUE, fontsize=22,
                                                col=1, max_col=2, row=8, max_row=12, maxWidth=420)
        self.text_buttons.append(self.generate_random_team_button)
        self.all_buttons.append(self.enter_battle_button)
        self.all_buttons.append(self.enter_tutorial_button)
        self.all_buttons.append(self.generate_random_team_button)

        self.card_buttons.append(self.first_character_card)
        self.card_buttons.append(self.second_character_card)
        self.card_buttons.append(self.third_character_card)
        self.all_buttons.append(self.first_character_card)
        self.all_buttons.append(self.second_character_card)
        self.all_buttons.append(self.third_character_card)

    def startup(self, persistent):
        self.player_character_list = generate_random_team(self.max_party_size)
        self.enemy_character_list = generate_random_team(self.max_party_size)
        self.update_character_previews()
        super(HomeMenu, self).startup(persistent)

    def get_event(self, event):
        super(HomeMenu, self).get_event(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            for cb in self.card_buttons:
                if cb.rect.collidepoint(self.mouse_pos):
                    self.player_character_list[self.card_buttons.index(cb)] = generate_new_card_data(
                        creation_time=random.randint(420000, 420999),
                        card_type="Character",
                        class_group=random.choice(CLASS_GROUPS))
                    self.update_character_previews()
            for ab in self.all_buttons:
                ab.active = False
                if ab.rect.collidepoint(self.mouse_pos):
                    ab.active = True
            if self.generate_random_team_button.rect.collidepoint(self.mouse_pos):
                self.player_character_list = generate_random_team(self.max_party_size)
                self.enemy_character_list = generate_random_team(self.max_party_size)
                self.update_character_previews()

            if self.enter_battle_button.rect.collidepoint(self.mouse_pos):
                if len(self.player_character_list) == self.max_party_size:
                    self.persist = {
                        "Player's new Party": self.player_character_list,
                        "Enemy's new Party": self.enemy_character_list
                    }
                    self.next_state_name = "GAME"
                    self.done = True

            if self.enter_tutorial_button.rect.collidepoint(self.mouse_pos):
                self.player_character_list = generate_tutorial_team(self.max_party_size)
                self.enemy_character_list = generate_tutorial_team(self.max_party_size)
                if len(self.player_character_list) == self.max_party_size:
                    self.persist = {
                        "Player's new Party": self.player_character_list,
                        "Enemy's new Party": self.enemy_character_list
                    }
                    self.next_state_name = "TUTORIAL"
                    self.done = True

        if event.type == pg.KEYDOWN:
            for tb in self.text_buttons:
                if tb.active and tb.canEdit:
                    if event.key == pg.K_BACKSPACE:
                        if len(tb.text) > 0:
                            tb.text = tb.text[:-1]
                            tb.update_button_text(tb.text)

    def generate_card_preview(self, card_data: dict) -> pg.Surface:
        info_img = pg.Surface((128, 128))
        info_img.fill(BLACK)
        name_img = self.font.render(card_data["Name"], True, card_data["Class Color"])
        number_img = self.font.render(str(card_data["Creation Number"]), True, card_data["Class Color"])
        class_img = self.font.render(str(card_data["Class Title"]), True, card_data["Class Color"])
        info_img.blit(name_img, (0, 0))
        info_img.blit(number_img, (0, 26))
        info_img.blit(class_img, (0, 52))
        return info_img

    def update_character_previews(self):
        self.first_character_card.update_image(pg.Surface((128, 128)),
                                               self.generate_card_preview(self.player_character_list[0]))
        self.second_character_card.update_image(pg.Surface((128, 128)),
                                                self.generate_card_preview(self.player_character_list[1]))
        self.third_character_card.update_image(pg.Surface((128, 128)),
                                               self.generate_card_preview(self.player_character_list[2]))

    def update(self, dt):
        super(HomeMenu, self).update(dt)

    def draw(self, surface: pg.Surface):
        surface.fill(BLACK)
        super(HomeMenu, self).draw(surface)
