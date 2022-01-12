from GUI.text_button import TextButton
from Gamestates.game import Game
from settings import *


class TutorialGame(Game):
    def __init__(self):
        super(TutorialGame, self).__init__()

        self.tutorialActive = True
        self.tutorial_text_list = [
            "These are your character cards, you can click on any one at a time",
            "once one is selected, press the \'v\'",
            "red represents their vitality, green represents their finesse, and blue shows their divinity."
        ]

        self.tutorial_text_button = TextButton("TUT0", (0, 0), (256, 64), (256, 64), self.tutorial_text_list[0],
                                               textcolor=GHOST_WHITE, row=15, max_row=16, col=5, max_col=10,
                                               maxWidth=420, optiontext="TUT")
        self.all_buttons.append(self.tutorial_text_button)
    
    def draw(self, surface: pg.Surface):
        surface.fill(HONEYDEW)
        super(TutorialGame, self).draw(surface)
