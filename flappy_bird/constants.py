from pygame import Color
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BIRD_SIZE = 50
PIPE_WIDTH = 70

PIPE_HORIZONTAL_GAP = int(SCREEN_WIDTH / 3)
PIPE_VERTICAL_GAP = 200

GRAVITY_ACCELERATION = 2
FLY_ACCELERATION = 5

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
BLUE = Color(93, 188, 210)
GREEN = Color(121, 192, 0)
YELLOW = Color(255, 238, 39)

FONT_PATH = os.path.join(
    os.getcwd(),
    'flappy_bird/res/fonts/ArcadeClassic.ttf'
)
FONT_SIZE = 96
