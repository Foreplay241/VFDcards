from Cards.Characters.Ranger.ranger_card import Ranger
from Cards.Characters.Seer.seer_card import Seer
from Cards.Characters.Soldier.soldier_card import Soldier
from Cards.character_card import Character
from Gamestates.gamestate import GameState
from settings import *


def compare_VFD_scores(player: Character, enemy: Character) -> str:
    if player.chosen_VFD == "Vitality":
        if enemy.chosen_VFD == "Vitality":
            return "Tie"
        elif enemy.chosen_VFD == "Finesse":
            player.card_data["Vitality"] += 1
            return "Player"
        elif enemy.chosen_VFD == "Divination":
            enemy.card_data["Divination"] += 1
            return "Enemy"
    elif player.chosen_VFD == "Finesse":
        if enemy.chosen_VFD == "Vitality":
            enemy.card_data["Vitality"] += 1
            return "Enemy"
        elif enemy.chosen_VFD == "Finesse":
            return "Tie"
        elif enemy.chosen_VFD == "Divination":
            player.card_data["Finesse"] += 1
            return "Player"
    elif player.chosen_VFD == "Divination":
        if enemy.chosen_VFD == "Vitality":
            player.card_data["Divination"] += 1
            return "Player"
        elif enemy.chosen_VFD == "Finesse":
            enemy.card_data["Finesse"] += 1
            return "Enemy"
        elif enemy.chosen_VFD == "Divination":
            return "Tie"


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
            for pc in persistent["Player's new Party"]:
                new_character = None
                if pc["Class Title"] == "Soldier":
                    new_character = Soldier(pc, col=x + 1, max_col=4, row=9, max_row=15)
                elif pc["Class Title"] == "Ranger":
                    new_character = Ranger(pc, col=x + 1, max_col=4, row=9, max_row=15)
                elif pc["Class Title"] == "Seer":
                    new_character = Seer(pc, col=x + 1, max_col=4, row=9, max_row=15)
                new_character.flip_card()
                new_character.switch_skill_to(new_character.chosen_VFD)
                self.players_party.append(new_character)
                self.all_buttons.append(new_character)
                x += 1
        if "Enemy's new Party" in persistent:
            for e in persistent["Enemy's new Party"]:
                new_character = None
                if e["Class Title"] == "Soldier":
                    new_character = Soldier(e, col=b + 1, max_col=4, row=2, max_row=15)
                elif e["Class Title"] == "Ranger":
                    new_character = Ranger(e, col=b + 1, max_col=4, row=2, max_row=15)
                elif e["Class Title"] == "Seer":
                    new_character = Seer(e, col=b + 1, max_col=4, row=2, max_row=15)
                new_character.card_data["Card Type"] = "Enemy Character"
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
            if event.key == pg.K_o and self.num_of_battles == 3:
                self.persist = {
                    "Player's Party": self.players_party,
                    "Enemy's Party": self.enemys_party
                }
                self.next_state_name = "OUTCOME_MENU"
                self.done = True
            if event.key == pg.K_SPACE:
                self.character_combat(self.char_pos)
            if event.key == pg.K_KP_1:
                self.select_character(0)
            if event.key == pg.K_KP_2:
                self.select_character(1)
            if event.key == pg.K_KP_3:
                self.select_character(2)
            if event.key == pg.K_v:
                for pc in self.players_party:
                    if pc.selected:
                        pc.switch_skill_to("Vitality")
            if event.key == pg.K_f:
                for pc in self.players_party:
                    if pc.selected:
                        pc.switch_skill_to("Finesse")
            if event.key == pg.K_d:
                for pc in self.players_party:
                    if pc.selected:
                        pc.switch_skill_to("Divination")

    def battle(self, player_char: Character, enemy_char: Character):
        pass

    def character_combat(self, character_position: int):
        player: Character = self.players_party[character_position]
        enemy: Character = self.enemys_party[character_position]
        if not player.hasBattled and not enemy.hasBattled:
            compare_VFD_scores(player, enemy)
            difference = player.card_data[player.chosen_VFD] - enemy.card_data[enemy.chosen_VFD]
            print(player.card_data[player.chosen_VFD])
            print(enemy.card_data[player.chosen_VFD])
            enemy.isFaceUp = False
            enemy.flip_card()
            if difference > 0:
                player.win()
                enemy.lose()
            elif difference == 0:
                player.tie()
                enemy.tie()
            elif difference < 0:
                enemy.win()
                player.lose()
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
        super(Game, self).update(dt)

    def draw(self, surface: pg.Surface):
        surface.fill(DARK_WOOD)
        super(Game, self).draw(surface)
