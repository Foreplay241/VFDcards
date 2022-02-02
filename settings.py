import random
from enum import Enum
import pygame as pg


class Soldier(Enum):
    TIER1 = {
        "Warrior": [6, 2, 0],
        "Brawler": [5, 3, 0],
        "Spell-Sword": [5, 1, 2],
    }
    TIER2 = {
        "Gladiator": [7, 4, 0],
        "Rogue": [6, 3, 2],
        "Templar": [5, 1, 2],
    }


TITLE = "spaceDits - Reddit space shooter"
pg.font.init()

# SCALING AND FPS
FULL_SCREEN = 0
SCALE = 1
FPS = 60

# DISPLAY INFORMATION
NATIVE_WIDTH = 640
NATIVE_HEIGHT = 640
NATIVE_SIZE = (NATIVE_WIDTH, NATIVE_HEIGHT)
NATIVE_WIDTH_CENTER = NATIVE_WIDTH // 2
NATIVE_HEIGHT_CENTER = NATIVE_HEIGHT // 2
NATIVE_TOP = 0
NATIVE_RIGHT = NATIVE_WIDTH
NATIVE_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_HEIGHT_CENTER)
NATIVE_BOTTOM = NATIVE_HEIGHT
NATIVE_LEFT = 0
NATIVE_TOP_LEFT = (NATIVE_LEFT, NATIVE_TOP)
NATIVE_TOP_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_TOP)
NATIVE_TOP_RIGHT = (NATIVE_RIGHT, NATIVE_TOP)
NATIVE_RIGHT_CENTER = (NATIVE_RIGHT, NATIVE_HEIGHT_CENTER)
NATIVE_BOTTOM_RIGHT = (NATIVE_RIGHT, NATIVE_BOTTOM)
NATIVE_BOTTOM_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_HEIGHT)
NATIVE_BOTTOM_LEFT = (NATIVE_LEFT, NATIVE_HEIGHT)
NATIVE_LEFT_CENTER = (NATIVE_LEFT, NATIVE_HEIGHT_CENTER)

DISPLAY_WIDTH = NATIVE_WIDTH * SCALE
DISPLAY_HEIGHT = NATIVE_HEIGHT * SCALE
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
DISPLAY_WIDTH_CENTER = DISPLAY_WIDTH // 2
DISPLAY_HEIGHT_CENTER = DISPLAY_HEIGHT // 2
DISPLAY_TOP = 0
DISPLAY_RIGHT = DISPLAY_WIDTH
DISPLAY_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_HEIGHT_CENTER)
DISPLAY_BOTTOM = DISPLAY_HEIGHT
DISPLAY_LEFT = 0
DISPLAY_TOP_LEFT = (DISPLAY_LEFT, DISPLAY_TOP)
DISPLAY_TOP_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_TOP)
DISPLAY_TOP_RIGHT = (DISPLAY_RIGHT, DISPLAY_TOP)
DISPLAY_RIGHT_CENTER = (DISPLAY_RIGHT, DISPLAY_HEIGHT_CENTER)
DISPLAY_BOTTOM_RIGHT = (DISPLAY_RIGHT, DISPLAY_BOTTOM)
DISPLAY_BOTTOM_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_HEIGHT)
DISPLAY_BOTTOM_LEFT = (DISPLAY_LEFT, DISPLAY_HEIGHT)
DISPLAY_LEFT_CENTER = (DISPLAY_LEFT, DISPLAY_HEIGHT_CENTER)

# PRIMARY COLORS
LIGHT_RED = (230, 173, 216)
LIGHT_GREEN = (216, 230, 173)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (79, 47, 47)
DARK_GREEN = (47, 79, 47)
DARK_BLUE = (47, 47, 79)

# SHADES
BLACK = (0, 0, 0)
SPACE_GREY = (22, 22, 22, 69)
DISABLED_TRIBLOCK = (29, 29, 29)
DARK_GREY = (60, 60, 60)
DARK_SLATE_GREY = (47, 79, 79)
DIM_GREY = (105, 105, 105)
FREE_SPEECH_GREY = (99, 86, 136)
GREY = (190, 190, 190)
GREY25 = (64, 64, 64)
GREY50 = (127, 127, 127)
GREY75 = (191, 191, 191)
GREY99 = (252, 252, 252)
LIGHT_GREY = (211, 211, 211)
SLATE_GREY = (112, 128, 144)
VERY_LIGHT_GREY = (205, 205, 205)
WHITE = (255, 255, 255)

# BLUES
ALICE_BLUE = (240, 248, 255)
AQUA = (0, 255, 255)
AQUAMARINE = (127, 255, 212)
AZURE = (240, 255, 255)
DIVINATION_BLUE = (42, 69, 241)
BLUE_3 = (0, 0, 205)
BLUE_4 = (0, 0, 139)
BLUE_VIOLET = (138, 43, 226)
CADET_BLUE = (95, 159, 159)
CORN_FLOWER_BLUE = (66, 66, 111)
CYAN = (0, 255, 255)
DARK_SLATE_BLUE = (36, 24, 130)
DARK_TURQUOISE = (112, 147, 219)
DEEP_SKY_BLUE = (0, 191, 255)
DODGER_BLUE = (30, 144, 255)
FREE_SPEECH_BLUE = (65, 86, 197)
LIGHT_CYAN = (224, 255, 255)
LIGHT_SKY_BLUE = (135, 206, 250)
LIGHT_SLATE_BLUE = (132, 112, 255)
LIGHT_STEEL_BLUE = (176, 196, 222)
MEDIUM_BLUE = (0, 0, 205)
MEDIUM_SLATE_BLUE = (123, 104, 238)
MEDIUM_TURQUOISE = (72, 209, 204)
MIDNIGHT_BLUE = (25, 25, 112)
NAVY = (0, 0, 128)
NAVY_BLUE = (0, 0, 128)
NEON_BLUE = (77, 77, 255)
NEW_MIDNIGHT_BLUE = (0, 0, 156)
PALE_TURQUOISE = (187, 255, 255)
POWDER_BLUE = (176, 224, 230)
RICH_BLUE = (89, 89, 171)
ROYAL_BLUE = (65, 105, 225)
SKY_BLUE = (135, 206, 235)
SLATE_BLUE = (131, 111, 255)
STEEL_BLUE = (70, 130, 180)
SUMMER_SKY = (56, 176, 222)
TEAL = (0, 128, 128)
TRUE_IRIS_BLUE = (3, 180, 204)
TURQUOISE = (64, 224, 208)

# BROWNS
BAKERS_CHOCOLATE = (92, 51, 23)
BEIGE = (245, 245, 220)
BROWN = (166, 42, 42)
BURLYWOOD = (222, 184, 135)
CHOCOLATE = (210, 105, 30)
DARK_BROWN = (92, 64, 51)
DARK_TAN = (151, 105, 79)
DARK_WOOD = (133, 94, 66)
LIGHT_WOOD = (133, 99, 99)
MEDIUM_WOOD = (166, 128, 100)
NEW_TAN = (235, 199, 158)
PERU = (205, 133, 63)
ROSY_BROWN = (188, 143, 143)
SADDLE_BROWN = (139, 69, 19)
SANDY_BROWN = (244, 164, 96)
SEMI_SWEET_CHOCOLATE = (107, 66, 38)
SIENNA = (142, 107, 35)
TAN = (219, 147, 112)
VERY_DARK_BROWN = (92, 64, 51)

# GREENS
CHARTREUSE = (127, 255, 0)
DARK_GREEN_COPPER = (74, 118, 110)
DARK_KHAKI = (189, 183, 107)
DARK_OLIVE_GREEN = (85, 107, 47)
DARK_SEA_GREEN = (143, 188, 143)
FOREST_GREEN = (34, 139, 34)
FREE_SPEECH_GREEN = (9, 249, 17)
GREEN_YELLOW = (173, 255, 47)
KHAKI = (240, 230, 140)
LAWN_GREEN = (124, 252, 0)
LIGHT_SEA_GREEN = (32, 178, 170)
LIME = (0, 255, 0)
MEDIUM_SEA_GREEN = (60, 179, 113)
MEDIUM_SPRING_GREEN = (0, 250, 154)
MINT_CREAM = (245, 255, 250)
OLIVE = (128, 128, 0)
OLIVE_DRAB = (107, 142, 35)
PALE_GREEN = (152, 251, 152)
SEA_GREEN = (46, 139, 87)
SPRING_GREEN = (0, 255, 127)
YELLOW_GREEN = (154, 205, 50)
SAGE_GREEN = (157, 193, 131)
FINESSE_GREEN = (142, 190, 111)
ARMY_GREEN = (75, 83, 32)

# ORANGES
BISQUE = (255, 228, 196)
CORAL = (255, 127, 0)
DARK_ORANGE = (255, 140, 0)
DARK_SALMON = (233, 150, 122)
HONEYDEW = (240, 255, 240)
LIGHT_CORAL = (240, 128, 128)
LIGHT_SALMON = (255, 160, 122)
MANDARIN_ORANGE = (142, 35, 35)
ORANGE = (255, 165, 0)
ORANGE_RED = (255, 36, 0)
PEACH_PUFF = (255, 218, 185)
SALMON = (250, 128, 114)

# RED/PINK
DEEP_PINK = (255, 20, 147)
DUSTY_ROSE = (133, 99, 99)
FIREBRICK = (178, 34, 34)
FELDSPAR = (209, 146, 117)
FLESH = (245, 204, 176)
FREE_SPEECH_MAGENTA = (227, 91, 216)
FREE_SPEECH_RED = (192, 0, 0)
HOT_PINK = (255, 105, 180)
INDIAN_RED = (205, 92, 92)
VITALITY_RED = (205, 69, 69)
LIGHT_PINK = (255, 182, 193)
MEDIUM_VIOLET_RED = (199, 21, 133)
MISTY_ROSE = (255, 228, 225)
PALE_VIOLET_RED = (219, 112, 147)
PINK = (255, 192, 203)
SCARLET = (140, 23, 23)
SPICY_PINK = (255, 28, 174)
TOMATO = (255, 99, 71)
VIOLET_RED = (208, 32, 144)

# PURPLE/PINK
DARK_ORCHID = (153, 50, 204)
DARK_PURPLE = (135, 31, 120)
DARK_VIOLET = (148, 0, 211)
FUCHSIA = (255, 0, 255)
LAVENDER = (230, 230, 250)
LAVENDER_BLUSH = (255, 240, 245)
MAGENTA = (255, 0, 255)
MAROON = (176, 48, 96)
MEDIUM_ORCHID = (186, 85, 211)
MEDIUM_PURPLE = (147, 112, 219)
NEON_PINK = (255, 110, 199)
ORCHID = (218, 112, 214)
PLUM = (221, 160, 221)
PURPLE = (160, 32, 240)
THISTLE = (216, 191, 216)
VIOLET = (238, 130, 238)
VIOLET_BLUE = (159, 95, 159)

# YELLOWS/GOLDS
BLANCHED_ALMOND = (255, 235, 205)
DARK_GOLDENROD = (184, 134, 11)
LEMON_CHIFFON = (255, 250, 205)
LIGHT_GOLDENROD = (238, 221, 130)
LIGHT_GOLDENROD_YELLOW = (250, 250, 210)
LIGHT_YELLOW = (255, 255, 224)
PALE_GOLDENROD = (238, 232, 170)
PAPAYA_WHIP = (255, 239, 213)
CORNSILK = (255, 248, 220)
GOLDENROD = (218, 165, 32)
MOCCASIN = (255, 228, 181)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
MEDIUM_GOLDENROD = (234, 234, 174)
MUSTARD_YELLOW = (254, 220, 86)
BURNT_YELLOW = ()

# WHITES/OFF-WHITES
ANTIQUE_WHITE = (250, 235, 215)
FLORAL_WHITE = (255, 250, 240)
GHOST_WHITE = (248, 248, 255)
NAVAJO_WHITE = (255, 222, 173)
OLD_LACE = (253, 245, 230)
WHITE_SMOKE = (245, 245, 245)
GAINSBORO = (220, 220, 220)
IVORY = (255, 255, 240)
LINEN = (250, 240, 230)
SEASHELL = (255, 245, 238)
SNOW = (255, 250, 250)
WHEAT = (245, 222, 179)
QUARTZ = (217, 217, 243)

RANDOM_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
RANDOM_COLOR2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
RANDOM_COLOR3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

RANDOM_RED = (random.randint(185, 255), random.randint(0, 125), random.randint(0, 125))
RANDOM_GREEN = (random.randint(0, 125), random.randint(185, 255), random.randint(0, 125))
RANDOM_BLUE = (random.randint(0, 125), random.randint(0, 125), random.randint(185, 255))

EXAMPLE_NAMES = [
    "Numo", "Windel", "Moris-ko", "UnDah", "Bilowen", "Ashia", "Manekot", "LoGey", "Mellon",
    "Kappa", "Aggie", "LoKul", "Shondora", "HuKalta", "RoMinta"
]

CLASS_GROUPS = ["Melee", "Ranged", "Magic"]

COLOR_DICT = {
    "Melee": [RED, DARK_RED, LIGHT_RED, PALE_VIOLET_RED, VITALITY_RED, ORANGE_RED,
              FREE_SPEECH_RED, MEDIUM_VIOLET_RED, INDIAN_RED, RANDOM_RED],
    "Ranged": [SAGE_GREEN, SEA_GREEN, ARMY_GREEN, SPRING_GREEN, LAWN_GREEN,
               FOREST_GREEN, FINESSE_GREEN, DARK_GREEN_COPPER, PALE_GREEN, GREEN_YELLOW],
    "Magic": [BLUE, BLUE_4, SKY_BLUE, CORN_FLOWER_BLUE, STEEL_BLUE, TRUE_IRIS_BLUE,
              DIVINATION_BLUE, POWDER_BLUE, NEW_MIDNIGHT_BLUE, LIGHT_STEEL_BLUE]
}
CLASS_DICT = {
    "Melee": ["Warrior", "Berserker", "Soldier", "Knight", "Paladin",
              "Sell-sword", "Gladiator", "Samurai", "Brawler", "Dragoon"],
    "Ranged": ["Archer", "Ranger", "Pirate", "Beast-Master", "Hunter",
               "Ninja", "Monk", "Axe-thrower", "Druid", "Assassin"],
    "Magic": ["Wizard", "Priest", "Cleric", "Mage", "Seer",
              "Warlock", "Witch", "Shaman", "Necromancer", "BattleMage"]
}
CARD_TYPES = ["Action", "Character", "Equipment"]

random_color_list = [RANDOM_COLOR, RANDOM_COLOR2, RANDOM_COLOR3,
                     RANDOM_RED, RANDOM_GREEN, RANDOM_BLUE,
                     QUARTZ, BISQUE, MANDARIN_ORANGE, CADET_BLUE]

fontname = pg.font.match_font('ariel')


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
