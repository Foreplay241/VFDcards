from settings import *


class GameState(object):
    """
    Parent class for individual game states to inherit from.
    """
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state_name = None
        self.persist = {}
        self.font = pg.font.Font(None, 24)
        self.mouse_pos = (0, 0)
        self.all_buttons = []
        self.text_buttons = []

    def startup(self, persistent: dict):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        self.persist = persistent
        print(self.persist.keys())

    def get_event(self, event: pg.event):
        """
        Handle a single event passed by the Game object.
        """
        if event.type == pg.QUIT:
            self.quit = True
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
        if event.type == pg.MOUSEMOTION:
            self.mouse_pos = pg.mouse.get_pos()

    def update(self, dt: float):
        """
        Update the state. Called by the Game object once
        per frame.

        dt: time since last frame
        """
        if self.quit:
            pg.quit()
        for ab in self.all_buttons:
            ab.update()

    def draw(self, surface: pg.surface):
        """
        Draw everything to the screen.
        """
        for ab in self.all_buttons:
            ab.draw(surface)
        pg.display.flip()
