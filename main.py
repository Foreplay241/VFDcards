#!/usr/bin/env python3

from Gamestates.game import Game
from Gamestates.game_tutorial import TutorialGame
from Gamestates.menu_home import HomeMenu
from Gamestates.menu_outcome import OutcomeMenu
from Gamestates.menu_pause import PauseMenu
from settings import *


class App(object):
    def __init__(self, screen, states):
        pg.mixer.pre_init()
        pg.init()
        pg.font.init()
        pg.mixer.init()
        self.screen = screen
        self.states = states
        self.prev_state = None
        self.current_state = self.states["HOME_MENU"]
        self.next_state = self.states["HOME_MENU"]
        self.clock = pg.time.Clock()
        self.game = Game()
        self.current_state.startup({})
        self.running = True
    
    def event_loop(self):
        """
        Events are passed for handling to the current state.
        :return:
        """
        for event in pg.event.get():
            self.current_state.get_event(event)
    
    def flip_state(self, current_state, new_state):
        """
        Switch game state to a different game state.
        :return: gamestate
        """
        self.prev_state = current_state
        self.prev_state.done = False
        persistent = self.current_state.persist
        self.current_state = new_state
        self.current_state.startup(persistent)
        self.screen.fill(BLACK)
        return self.current_state
    
    def update(self, dt):
        """
        Check for state flip and update active state
        :param dt: milliseconds since last frame
        :return:
        """
        if self.current_state.done:
            self.flip_state(self.current_state, self.states[self.current_state.next_state_name])
        self.current_state.update(dt)
    
    def draw(self):
        """
        Pass display surface to active state for drawing.
        :return:
        """
        self.current_state.draw(self.screen)
    
    def run(self):
        """
        Pretty much the entirety of the game's runtime will be
        spent inside this while loop.
        """
        while self.running:
            dt = self.clock.tick(FPS)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()


if __name__ == '__main__':
    SCREEN = pg.display.set_mode(DISPLAY_SIZE)
    GAME_STATES = {
        "HOME_MENU": HomeMenu(),
        "PAUSE_MENU": PauseMenu(),
        "OUTCOME_MENU": OutcomeMenu(),
        "GAME": Game(),
        "TUTORIAL": TutorialGame()
    }
    app = App(SCREEN, GAME_STATES)
    app.run()
