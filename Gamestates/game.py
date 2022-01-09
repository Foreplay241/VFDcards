from Cards.card import Card
from Cards.character_card import Character
from GUI.button import Button
from Gamestates.gamestate import GameState
from settings import *


class Game(GameState):
    def __init__(self):
        super().__init__()
        self.players_party = []
        self.enemys_party = []

    def startup(self, persistent):
        x = 0
        b = 0
        if "Player's new Party" in persistent:
            for p in persistent["Player's new Party"]:
                new_character = Character(p["Name"], p["Creation Number"], p["Class Group"], p["Card Type"],
                                          col=x + 1, max_col=4, row=10, max_row=15)
                new_character.flip_card()
                self.players_party.append(new_character)
                self.all_buttons.append(new_character)
                x += 1
                print(new_character.card_data)
            for e in persistent["Enemy's new Party"]:
                new_character = Character(e["Name"], e["Creation Number"], e["Class Group"], e["Card Type"],
                                          col=b + 1, max_col=4, row=1, max_row=15)
                new_character.chosen_VFD = random.choice(["Vitality", "Finesse", "Divination"])
                new_character.front_image = new_character.generateImg()
                new_character.front_image = pg.transform.flip(new_character.front_image, False, True)
                self.enemys_party.append(new_character)
                self.all_buttons.append(new_character)
                b += 1
        if "Player's Party" in persistent:
            self.players_party = persistent["Player's Party"]
            self.enemys_party = persistent["Enemy's Party"]

    def get_event(self, event):
        super(Game, self).get_event(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            for pc in self.players_party:
                pc.selected = False
                if pc.rect.collidepoint(self.mouse_pos):
                    pc.selected = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                self.persist = {
                    "Player's Party": self.players_party,
                    "Enemy's Party": self.enemys_party
                }
                self.next_state_name = "PAUSE_MENU"
                self.done = True
            if event.key == pg.K_SPACE:
                for ec in self.enemys_party:
                    ec.flip_card()
            if event.key == pg.K_v:
                for pc in self.players_party:
                    if pc.selected:
                        pc.chosen_VFD = "Vitality"
                        pc.update_image(pc.generateImg(), pc.generateImg())
            if event.key == pg.K_f:
                for pc in self.players_party:
                    if pc.selected:
                        pc.chosen_VFD = "Finesse"
                        pc.update_image(pc.generateImg(), pc.generateImg())
            if event.key == pg.K_d:
                for pc in self.players_party:
                    if pc.selected:
                        pc.chosen_VFD = "Divination"
                        pc.update_image(pc.generateImg(), pc.generateImg())

    def update(self, dt):
        super(Game, self).update(dt)

    def draw(self, surface: pg.Surface):
        surface.fill(DARK_WOOD)
        super(Game, self).draw(surface)
