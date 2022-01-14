from GUI.text_button import TextButton
from Gamestates.game import Game
from settings import *


class TutorialGame(Game):
    def __init__(self):
        super(TutorialGame, self).__init__()
        self.tutorial_step = 0
        self.tutorialActive = True
        self.tutorial_text_list = [
            "These are your character cards, you can click on any one at a time",
            "Your VFD-score has a skill power for ranking from 0-9.",
            "Red shows vitality level, green is finesse level, and blue shows divinity level.",
            "Once one is selected, press the \'v\', \'f\', or \'d\' key and then space to \"battle\".",
            "It compares your character's chosen VFD-score to the enemy's and highlights the winner.",
            "",
            "",
        ]

        self.tutorial_text_button = TextButton("TUT0", (0, 0), (256, 64), (256, 64), self.tutorial_text_list[0],
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
        super(TutorialGame, self).get_event(event)

    def update(self, dt):
        self.tutorial_step = clamp(self.tutorial_step, 0, len(self.tutorial_text_list) - 1)
        self.tutorial_text_button.update_button_text(self.tutorial_text_list[self.tutorial_step])
        super(TutorialGame, self).update(dt)

    def draw(self, surface):
        surface.fill(HONEYDEW)
        super(TutorialGame, self).draw(surface)
