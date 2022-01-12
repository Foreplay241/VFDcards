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


def generate_card_preview(card_data: dict) -> pg.Surface:
    info_img = pg.Surface((128, 128))
    info_img.fill(BLACK)
    name_img = pg.font.Font(None, 24).render(card_data["Name"], True, GREEN)
    number_img = pg.font.Font(None, 24).render(str(card_data["Creation Number"]), True, GREEN)
    class_img = pg.font.Font(None, 24).render(str(card_data["Class Title"]), True, GREEN)
    info_img.blit(name_img, (0, 0))
    info_img.blit(number_img, (0, 26))
    info_img.blit(class_img, (0, 52))
    return info_img


def generate_new_card_data(name="Elira Jinmop", creation_time=420069,
                           class_group="Melee", card_type="ACE?") -> dict:
    new_card_data = {"Name": name, "Creation Number": creation_time,
                     "Class Group": class_group, "Card Type": card_type}
    x = 0
    for c in map(int, str(creation_time)):
        if x == 0:
            new_card_data["Vitality"] = c
        if x == 1:
            new_card_data["Finesse"] = c
        if x == 2:
            new_card_data["Divination"] = c
        if x == 3:
            new_card_data["Class Title"] = CLASS_DICT[class_group][c]
            new_card_data["Class Digit"] = c
        x += 1
    return new_card_data


class HomeMenu(Menu):
    def __init__(self):
        super(HomeMenu, self).__init__()
        self.new_card_data = {
            "Name": "Knoh Naym",
            "Card Type": "Action, Character, Equipment",
            "Class Title": "Default Class",
            "Creation Number": 123456
        }

        self.player_character_list = []
        self.enemy_character_list = []
        self.character_name_list = []
        self.card_buttons = []
        self.max_party_size = 3
        self.prev_name = None
        self.next_name = None
        self.name_character_button = TextButton("H0", (0, 0), (0, 0), (0, 0), text="Clicking here will pick a random name",
                                                textcolor=WHITE_SMOKE, bgColor=SPACE_GREY,
                                                optiontext="", optioncolor=LIGHT_SLATE_BLUE, fontsize=22,
                                                col=1, max_col=2, row=1, max_row=12, canEdit=True,
                                                maxWidth=420)
        self.generate_character_button = TextButton("H1", (0, 0), (0, 0), (0, 0), text="Generate Character",
                                                    textcolor=WHITE_SMOKE, bgColor=SPACE_GREY,
                                                    optiontext="", optioncolor=LIGHT_SLATE_BLUE, fontsize=22,
                                                    col=1, max_col=2, row=2, max_row=12, maxWidth=420)
        self.character_card_preview = Button("H2", (0, 0), (128, 128), (128, 128),
                                             col=1, max_col=2, row=3, max_row=12)
        self.add_character_to_party_button = TextButton("H3", (0, 0), (0, 0), (0, 0),
                                                        text=f"Broken button for now",
                                                        textcolor=WHITE_SMOKE, bgColor=SPACE_GREY,
                                                        optiontext="", optioncolor=LIGHT_SLATE_BLUE, fontsize=22,
                                                        col=1, max_col=3, row=6, max_row=12, maxWidth=210)
        self.generate_random_team_button = TextButton("H8", (0, 0), (128, 128), (128, 128), text="Generate Random Team",
                                                      textcolor=WHITE_SMOKE, bgColor=SPACE_GREY,
                                                      optiontext="", optioncolor=LIGHT_SLATE_BLUE, fontsize=22,
                                                      col=2, max_col=3, row=6, max_row=12, maxWidth=210)
        self.first_character_card = Button("H4", (0, 0), (128, 128), (128, 128),
                                           col=1, max_col=4, row=7, max_row=12)
        self.second_character_card = Button("H5", (0, 0), (128, 128), (128, 128),
                                            col=2, max_col=4, row=7, max_row=12)
        self.third_character_card = Button("H6", (0, 0), (128, 128), (128, 128),
                                           col=3, max_col=4, row=7, max_row=12)
        self.enter_battle_button = TextButton("H7", (0, 0), (0, 0), (0, 0),
                                              text=f"Enter game",
                                              textcolor=WHITE_SMOKE, bgColor=SPACE_GREY,
                                              optiontext="", optioncolor=LIGHT_SLATE_BLUE, fontsize=22,
                                              col=1, max_col=3, row=10, max_row=12, maxWidth=210)
        self.enter_tutorial_button = TextButton("H7", (0, 0), (0, 0), (0, 0),
                                                text=f"Tutorial",
                                                textcolor=WHITE_SMOKE, bgColor=SPACE_GREY,
                                                optiontext="", optioncolor=LIGHT_SLATE_BLUE, fontsize=22,
                                                col=2, max_col=3, row=10, max_row=12, maxWidth=210)
        self.text_buttons.append(self.name_character_button)
        self.text_buttons.append(self.generate_character_button)
        self.text_buttons.append(self.generate_random_team_button)
        self.text_buttons.append(self.add_character_to_party_button)
        self.all_buttons.append(self.name_character_button)
        self.all_buttons.append(self.generate_character_button)
        self.all_buttons.append(self.add_character_to_party_button)
        self.all_buttons.append(self.enter_battle_button)
        self.all_buttons.append(self.enter_tutorial_button)
        self.all_buttons.append(self.generate_random_team_button)

        self.all_buttons.append(self.character_card_preview)
        self.card_buttons.append(self.first_character_card)
        self.card_buttons.append(self.second_character_card)
        self.card_buttons.append(self.third_character_card)
        self.all_buttons.append(self.first_character_card)
        self.all_buttons.append(self.second_character_card)
        self.all_buttons.append(self.third_character_card)

    def startup(self, persistent):
        pass

    def get_event(self, event):
        super(HomeMenu, self).get_event(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            for ab in self.all_buttons:
                ab.active = False
                if ab.rect.collidepoint(self.mouse_pos):
                    ab.active = True
            if self.name_character_button.rect.collidepoint(self.mouse_pos):
                self.next_name = random.choice(EXAMPLE_NAMES)
                self.name_character_button.update_button_text(self.next_name)
                self.add_character_to_party_button.update_button_text(f"Add {self.next_name}")
            if self.generate_character_button.rect.collidepoint(self.mouse_pos):
                if self.name_character_button.text != self.prev_name:
                    new_character_data = generate_new_card_data(name=self.name_character_button.text,
                                                                creation_time=random.randint(100000, 999999),
                                                                card_type="Character",
                                                                class_group="Magic")
                    self.prev_name = self.name_character_button.text
                    self.character_card_preview.update_image(pg.Surface((128, 128)),
                                                             generate_card_preview(new_character_data))
                    self.new_card_data = new_character_data
            if self.add_character_to_party_button.rect.collidepoint(self.mouse_pos):
                if self.new_card_data["Name"] not in self.character_name_list:
                    if len(self.player_character_list) < self.max_party_size:
                        self.player_character_list.append(self.new_card_data)
                        self.enemy_character_list.append(self.new_card_data)
                        self.character_name_list.append(self.new_card_data["Name"])
            if self.generate_random_team_button.rect.collidepoint(self.mouse_pos):
                self.player_character_list = []
                self.enemy_character_list = []
                for i in range(self.max_party_size):
                    new_character_data = generate_new_card_data(name=random.choice(EXAMPLE_NAMES),
                                                                creation_time=random.randint(100000, 999999),
                                                                card_type="Character",
                                                                class_group=random.choice(CLASS_GROUPS))
                    new_enemy_data = generate_new_card_data(name=random.choice(EXAMPLE_NAMES),
                                                            creation_time=random.randint(100000, 999999),
                                                            card_type="Enemy Character",
                                                            class_group=random.choice(CLASS_GROUPS))
                    self.player_character_list.append(new_character_data)
                    self.enemy_character_list.append(new_enemy_data)
                    self.character_name_list.append(self.new_card_data["Name"])
                self.first_character_card.update_image(pg.Surface((128, 128)),
                                                       generate_card_preview(self.player_character_list[0]))
                self.second_character_card.update_image(pg.Surface((128, 128)),
                                                        generate_card_preview(self.player_character_list[1]))
                self.third_character_card.update_image(pg.Surface((128, 128)),
                                                       generate_card_preview(self.player_character_list[2]))

            if self.enter_battle_button.rect.collidepoint(self.mouse_pos):
                if len(self.player_character_list) == self.max_party_size:
                    self.persist = {
                        "Player's new Party": self.player_character_list,
                        "Enemy's new Party": self.enemy_character_list
                    }
                    self.next_state_name = "GAME"
                    self.done = True

            if self.enter_tutorial_button.rect.collidepoint(self.mouse_pos):
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
                    else:
                        tb.text += event.unicode
                        tb.update_button_text(tb.text)
                        self.add_character_to_party_button.update_button_text(f"Add {tb.text}")

    def update(self, dt):
        super(HomeMenu, self).update(dt)

    def draw(self, surface: pg.Surface):
        surface.fill(BLACK)
        super(HomeMenu, self).draw(surface)
