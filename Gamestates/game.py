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
        for p in persistent["Player's Party"]:
            newCharacter = Character(p["Name"], p["Creation Number"], p["Class Group"], p["Card Type"],
                                     col=x+1, max_col=4, row=10, max_row=15)
            newCharacter.flip_card()
            self.players_party.append(newCharacter)
            self.all_buttons.append(newCharacter)
            x += 1
            print(newCharacter.card_data)
        for e in persistent["Enemy's Party"]:
            newCharacter = Character(e["Name"], e["Creation Number"], e["Class Group"], e["Card Type"],
                                     col=b+1, max_col=4, row=1, max_row=15)
            self.enemys_party.append(newCharacter)
            self.all_buttons.append(newCharacter)
            b += 1

    def get_event(self, event):
        super(Game, self).get_event(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            for pc in self.players_party:
                if pc.rect.collidepoint(self.mouse_pos):
                    if self.mouse_pos[0] <= 63:
                        pc.rotate_triblocks(120)
                    if self.mouse_pos[0] > 64:
                        pc.rotate_triblocks(240)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_v:
                pass

    def update(self, dt):
        super(Game, self).update(dt)

    def draw(self, surface: pg.Surface):
        surface.fill(DARK_WOOD)
        super(Game, self).draw(surface)
