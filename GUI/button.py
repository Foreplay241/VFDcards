import os

from settings import *


class Button(pg.sprite.Sprite):

    def __init__(self, id_num: str, pos: tuple, BGimg, FGimg,
                 col=0, max_col=0, row=0, max_row=0):
        super(Button, self).__init__()
        self.id_num = id_num
        self.pos = pos
        self.sourceFileDir = os.path.dirname(os.path.abspath(__file__))
        self.assetsPath = os.path.join(self.sourceFileDir, "assets")
        self.BGimage = pg.Surface((0, 0))
        self.FGimage = pg.Surface((0, 0))
        # DETERMINE IF LOADABLE IMAGE OR NEW BLANK IMAGE.
        if type(BGimg) is tuple:
            self.BGimage = pg.Surface(BGimg)
            self.BGimage.fill(WHITE)
        elif type(BGimg) is str:
            self.BGimage = pg.image.load(os.path.join(self.assetsPath, BGimg + ".png")).convert_alpha()

        if type(FGimg) is tuple:
            self.FGimage = pg.Surface(FGimg)
        elif type(FGimg) is str:
            self.FGimage = pg.image.load(os.path.join(self.assetsPath, FGimg + ".png")).convert_alpha()
        
        # SET UP LOCATION ON THE GRID
        self.column = col
        self.row = row
        self.max_column = max_col
        self.max_row = max_row
        
        # SET IMAGE AND RECTANGLE
        self.image = self.BGimage
        self.rect = self.image.get_rect()
        self.clicked = False
        self.active = False
        self.selected = False

    def update_image(self, newBGimg: pg.Surface, newFGimg: pg.Surface):
        """
        Set the background image and foreground image on top, then colorkey and rectangle.
        :param newBGimg: Background image to be set for this button.
        :param newFGimg: Foreground image to be set on top of background.
        :return:
        """
        self.BGimage = newBGimg
        self.FGimage = newFGimg
        self.image.blit(self.BGimage, (0, 0))
        self.image.blit(self.FGimage, (0, 0))
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def events(self):
        pass

    def update(self):
        super(Button, self).update()
        # IF ROW/COL ARE ALL 0, IGNORE THE GRID
        if self.column == 0 and self.row == 0:
            if self.max_row == 0 and self.max_column == 0:
                pass
        else:
            self.pos = ((DISPLAY_WIDTH * self.column) // self.max_column - (self.image.get_width() // 2),
                        (DISPLAY_HEIGHT * self.row) // self.max_row)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def draw(self, window):
        window.blit(self.image, self.rect)
        if self.active:
            pg.draw.rect(self.image, MIDNIGHT_BLUE, self.rect, 4)

    def draw_selection_outline(self):
        pg.draw.rect(self.image, MIDNIGHT_BLUE, self.rect, 4)
