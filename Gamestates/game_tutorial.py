from enum import Enum

from GUI.text_button import TextButton
from Gamestates.game import Game
from settings import *


class Tut(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    ELEVEN = 11
    TWELVE = 12
    THIRTEEN = 13
    FOURTEEN = 14


class TutorialGame(Game):
    def __init__(self):
        super(TutorialGame, self).__init__()
        self.tutorial_step = 0
        self.tutorialActive = True
        self.tutorial_dict = {
            Tut.ZERO: ["Press \'n\' for the next tutorial step and \'b\' for previous step.", 15],
            Tut.ONE: ["These are your character Tri-blocks, you can select one at a time.", 13],
            Tut.TWO: ["You can click on them or press 1, 2, or 3 on the keypad.", 14],
            Tut.THREE: ["Your Opponent has the same thing but hidden with a \'Class color\'.", 1],
            Tut.FOUR: ["Each Character has red, green, and blue stones attached to each corner.", 14],
            Tut.FIVE: ["Red shows how much vitality a character has.", 14],
            Tut.SIX: ["Green represents their finesse level.", 14],
            Tut.SEVEN: ["Blue stones show how much divination for that character.", 14],
            Tut.EIGHT: ["Once a character is selected, press the \'v\', \'f\', or \'d\' key.", 14],
            Tut.NINE: ["When the character and skill are chosen, press space.", 14],
            Tut.TEN: ["This will compare your skill level against the opponents choice.", 14],
            Tut.ELEVEN: ["The winner remains face up and the loser is flipped down.", 14],
            Tut.TWELVE: ["Character score is increased by how much you beat the enemy.", 14],
            Tut.THIRTEEN: ["After all characters have competed, press the \'o\' key.", 14],
            Tut.FOURTEEN: ["Step Fifteen", 14],
        }

        self.tutorial_text_button = TextButton("TUT0", (0, 0), (256, 64), (256, 64), self.tutorial_dict[Tut(0)][0],
                                               textcolor=GHOST_WHITE, row=15, max_row=16, col=5, max_col=10,
                                               maxWidth=620, optiontext="b4bak", valuetext="n4nxt", fontsize=22)
        self.all_buttons.append(self.tutorial_text_button)

    def startup(self, persistent):
        super(TutorialGame, self).startup(persistent)

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_n:
                self.tutorial_step += 1
            if event.key == pg.K_b:
                self.tutorial_step -= 1
            self.tutorial_step = clamp(self.tutorial_step, 0, len(self.tutorial_dict) - 1)
            self.tutorial_text_button.row = self.tutorial_dict[Tut(self.tutorial_step)][1]
            self.tutorial_text_button.update_button_text(self.tutorial_dict[Tut(self.tutorial_step)][0])
        super(TutorialGame, self).get_event(event)

    def update(self, dt):
        super(TutorialGame, self).update(dt)

    def draw(self, surface):
        surface.fill(HONEYDEW)
        super(TutorialGame, self).draw(surface)
