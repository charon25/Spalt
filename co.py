import pygame as pyg

WIDTH = 1280
HEIGHT = 600
WINDOW_HEIGHT = 720
SCREEN_SIZE = (WIDTH, WINDOW_HEIGHT)
SCREEN_TITLE = "SPALT"
FRAME_INTERVAL = 16
LEVELS_COUNT = 8

###CHEMINS
RESOURCES_PATH = "resources/"
TEXTURES_PATH = RESOURCES_PATH + "textures/"
SOUND_PATH = RESOURCES_PATH + "sounds/"
#TEXTURES
BACKGROUND_PATH = TEXTURES_PATH + "background.png"
MENU_PATH = TEXTURES_PATH + "menu.png"
EOL_PATH = TEXTURES_PATH + "end_of_level.png"
EOG_PATH = TEXTURES_PATH + "end_of_game.png"

###ETAT JEU
MENU_STATE = 0
PLAY_STATE = 1
EOL_STATE = 2
EOG_STATE = 3
#MODE
LEVEL_MODE = 0
RANDOM_MODE = 1

###POLICE & TEXTE
FONT_PATH = RESOURCES_PATH + "font/betterpixels.ttf"
TEXT_X = 10
TEXT_SIZE = 40
TEXT_Y1 = 600 - 2*TEXT_SIZE
TEXT_Y2 = 600 - TEXT_SIZE

###MENU
BT_WIDTH = 600
BT_HEIGHT = 60
BT_X = 340
LEVELS_BT = pyg.Rect(BT_X, 360, BT_WIDTH, BT_HEIGHT)
RANDOM_BT = pyg.Rect(BT_X, 480, BT_WIDTH, BT_HEIGHT)
QUIT_BT = pyg.Rect(BT_X, 600, BT_WIDTH, BT_HEIGHT)

###HELP
HELP_PATH = TEXTURES_PATH + "help.png"
HELP_X = 0
HELP_Y = 600
MIN_LEVEL_HELP = 6

###NEUTRONS
NEUTRON_SIZE = 25
NEUTRON_SPEED = 10
NEUTRON_PATH = TEXTURES_PATH + "neutron.png"
NEUTRON_CREATION_ANGLE_U = 40
NEUTRON_CREATION_ANGLE_PU = 110
NEUTRON_MAX_BOUNCES = 2
#NOMBRE
NEUTRON_COUNT_X = 5
NEUTRON_COUNT_Y = 5
NEUTRON_COUNT_TEXT_X = NEUTRON_COUNT_X + NEUTRON_SIZE + 5
NEUTRON_COUNT_TEXT_Y = NEUTRON_COUNT_Y
NEUTRON_COUNT_TEXT_SIZE = 32
NEUTRON_COUNT_0_COLOR = (0, 0, 0)
NEUTRON_COUNT_LESS_COLOR = (0, 0, 230)
NEUTRON_COUNT_EQUAL_COLOR = (0, 130, 0)
NEUTRON_COUNT_MORE_COLOR = (230, 0, 0)

###BOUTON RESTART
RESTART_BT_PATH = TEXTURES_PATH + "restart_bt.png"
RESTART_BT_X = 5
RESTART_BT_Y = 40
RESTART_BT = pyg.Rect(RESTART_BT_X, RESTART_BT_Y, 150, 40)

###ELECTRONS
ELECTRON_SIZE = 15
ELECTRON_SPEED = 18
ELECTRON_PATH = TEXTURES_PATH + "electron.png"

###ATOMES
#TAILLES
KR93_SIZE = SR94_SIZE = 40
ZR103_SIZE = 41
XE134_SIZE = XE140_SIZE = BA140_SIZE = 45
U234_SIZE = U235_SIZE = U236_SIZE = U237_SIZE = U238_SIZE = U239_SIZE = NP237_SIZE = NP238_SIZE = NP239_SIZE = PU238_SIZE = PU239_SIZE = 55
#TEXTURES
KR93_PATH = TEXTURES_PATH + "kr93.png"
SR94_PATH = TEXTURES_PATH + "sr94.png"
ZR103_PATH = TEXTURES_PATH + "zr103.png"
XE134_PATH = TEXTURES_PATH + "xe134.png"
XE140_PATH = TEXTURES_PATH + "xe140.png"
BA140_PATH = TEXTURES_PATH + "ba140.png"
U234_PATH = TEXTURES_PATH + "u234.png"
U235_PATHS = [TEXTURES_PATH + "u235_0.png", TEXTURES_PATH + "u235_1.png", TEXTURES_PATH + "u235_2.png"]
U236_PATH = TEXTURES_PATH + "u236.png"
U237_PATH = TEXTURES_PATH + "u237.png"
U238_PATH = TEXTURES_PATH + "u238.png"
U239_PATH = TEXTURES_PATH + "u239.png"
NP237_PATH = TEXTURES_PATH + "np237.png"
NP238_PATH = TEXTURES_PATH + "np238.png"
NP239_PATH = TEXTURES_PATH + "np239.png"
PU238_PATH = TEXTURES_PATH + "pu238.png"
PU239_PATH = TEXTURES_PATH + "pu239.png"
#TEMPS DE DESINTEGRATION
U237_DECAY = 733
U239_DECAY = 400
NP238_DECAY = 668
NP239_DECAY = 678
PU239_DECAY = 1250
DECAY_MAX_SHAKE = 5
#FISSION
ATOM_CREATION_ANGLE_MIN = 60
ATOM_CREATION_ANGLE_MAX = 85
ATOM_CREATION_SPEED_FACTOR = 0.3
#TYPE U235
U235_NEUTRON = 0
U235_SRXE2 = 1
U235_KRBA3 = 2
#AUTRES
ATOM_BRAKE = 0.01


###JOUEUR
ARROW_COLOR_FAR = (255, 0, 0)
ARROW_COLOR_CLOSE = (50, 50, 50)
ARROW_WIDTH = 10
LEFT_CLICK = 1
RIGHT_CLICK = 3
MIN_DISTANCE_TO_PLAY = 40

###FIN DE NIVEAU
TIME_WITHOUT_ACTION = 1800
EOL_X = 320
EOL_Y = 150
EOL_BT_WIDTH = 150
EOL_BT_HEIGHT = 40
EOL_MENU_BT = pyg.Rect(EOL_X + 50, EOL_Y + 220, EOL_BT_WIDTH, EOL_BT_HEIGHT)
EOL_RESTART_BT = pyg.Rect(EOL_X + 245, EOL_Y + 220, EOL_BT_WIDTH, EOL_BT_HEIGHT)
EOL_NEXT_BT = pyg.Rect(EOL_X + 440, EOL_Y + 220, EOL_BT_WIDTH, EOL_BT_HEIGHT)
EOL_TEXT_SIZE = 32
EOL_REQUIRED_TEXT_X = EOL_X + 497
EOL_REQUIRED_TEXT_Y = EOL_Y + 127
EOL_NUMBER_TEXT_X = EOL_REQUIRED_TEXT_X
EOL_NUMBER_TEXT_Y = EOL_Y + 158

###NIVEAU RANDOM
RAND_MIN_ATOMS = 15
RAND_MAX_ATOMS = 30

###SONS
#EVENT TYPE
DISINTEGRATION_TYPE = 12345
FISSION_TYPE = 12346
ABSORB_TYPE = 12347
WALL_TYPE = 12348
#PATH
CLICK_PATH = SOUND_PATH + "click.wav"
LAUNCH_NEUTRON_PATH = SOUND_PATH + "launch_neutron.wav"
DISINTEGRATION_PATH = SOUND_PATH + "disintegration.wav"
FISSION_PATH = SOUND_PATH + "fission.wav"
ABSORB_PATH = SOUND_PATH + "absorb.wav"
WALL_PATH = SOUND_PATH + "wall.wav"
EOL_SOUND_PATH = SOUND_PATH + "eol.wav"
MUSIC_PATH = SOUND_PATH + "music.wav"










