from Cards.character_card import Character
from Gamestates.gamestate import GameState
from settings import *


class Game(GameState):
    def __init__(self):
        super().__init__()
        self.players_party = []
        self.enemys_party = []
        self.char_pos = random.randint(0, 2)
        self.battle_winners = []
        self.battle_losers = []
        self.num_of_battles = 0

    def startup(self, persistent):
        x = 0
        b = 0
        self.num_of_battles = 0
        self.battle_winners = []
        self.enemys_party = []
        self.players_party = []

        if "Player's new Party" in persistent:
            for p in persistent["Player's new Party"]:
                new_character = Character(p, col=x + 1, max_col=4, row=10, max_row=15)
                new_character.flip_card()
                new_character.switch_to(new_character.chosen_VFD)
                self.players_party.append(new_character)
                self.all_buttons.append(new_character)
                x += 1
        if "Enemy's new Party" in persistent:
            for e in persistent["Enemy's new Party"]:
                new_character = Character(e, col=b + 1, max_col=4, row=1, max_row=15)
                new_character.chosen_VFD = random.choice(["Vitality", "Finesse", "Divination"])
                new_character.front_image = new_character.generateImg()
                new_character.front_image = pg.transform.flip(new_character.front_image, False, True)
                self.enemys_party.append(new_character)
                self.all_buttons.append(new_character)
                b += 1
        if "Player's Party" in persistent:
            self.players_party = persistent["Player's Party"]
            for pc in self.players_party:
                self.all_buttons.append(pc)
        if "Enemy's Party" in persistent:
            self.enemys_party = persistent["Enemy's Party"]
            for ec in self.enemys_party:
                self.all_buttons.append(ec)
        super(Game, self).startup(persistent)

    def get_event(self, event: pg.event):
        super(Game, self).get_event(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            for pc in self.players_party:
                if pc.rect.collidepoint(self.mouse_pos):
                    self.select_character(self.players_party.index(pc))
        if event.type == pg.KEYDOWN:
            # if event.key == pg.K_p:
            #     self.persist = {
            #         "Player's Party": self.players_party,
            #         "Enemy's Party": self.enemys_party
            #     }
            #     self.next_state_name = "PAUSE_MENU"
            #     self.done = True
            if event.key == pg.K_SPACE:
                self.character_battle(self.char_pos)
            if event.key == pg.K_KP_1:
                self.select_character(0)
            if event.key == pg.K_KP_2:
                self.select_character(1)
            if event.key == pg.K_KP_3:
                self.select_character(2)
            if event.key == pg.K_v:
                for pc in self.players_party:
                    if pc.selected:
                        pc.switch_to("Vitality")
            if event.key == pg.K_f:
                for pc in self.players_party:
                    if pc.selected:
                        pc.switch_to("Finesse")
            if event.key == pg.K_d:
                for pc in self.players_party:
                    if pc.selected:
                        pc.switch_to("Divination")

    def character_battle(self, character_position: int):
        player: Character = self.players_party[character_position]
        enemy: Character = self.enemys_party[character_position]
        if not player.hasBattled and not enemy.hasBattled:
            difference = player.card_data[player.chosen_VFD] - enemy.card_data[enemy.chosen_VFD]
            print(difference)
            player.row -= 2
            enemy.row += 2
            enemy.isFaceUp = False
            enemy.flip_card()
            if difference > 0:
                # PLAYER WINS
                player.isWinner = True
                enemy.isWinner = False
                enemy.disable()
                self.battle_winners.append(player)
                self.battle_losers.append(enemy)
            elif difference == 0:
                # TIE
                player.isWinner = False
                enemy.isWinner = False
            elif difference < 0:
                # ENEMY WINS
                enemy.isWinner = True
                player.isWinner = False
                player.disable()
                self.battle_winners.append(enemy)
                self.battle_losers.append(player)
            player.hasBattled = True
            enemy.hasBattled = True
            self.num_of_battles += 1

    def select_character(self, char_position: int):
        if self.players_party[char_position].selectable:
            self.char_pos = char_position
            for pc in self.players_party:
                if pc.selectable:
                    pc.selected = False
            self.players_party[char_position].selected = True

    def update(self, dt):
        if self.num_of_battles == 3:
            self.persist = {
                "Player's Party": self.players_party,
                "Enemy's Party": self.enemys_party,
            }
            self.next_state_name = "OUTCOME_MENU"
            self.done = True

        super(Game, self).update(dt)

    def draw(self, surface: pg.Surface):
        surface.fill(DARK_WOOD)
        super(Game, self).draw(surface)
