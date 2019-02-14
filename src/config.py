

# = Constants and Utilities ===================================================


# = Simple Constants ==========================================================

# - Language System --------------------------------
LANGUAGE_ENGLISH = 'English'
LANGUAGE_DEFAULT = LANGUAGE_ENGLISH
LANG_ALIASES = 'aliases'
LANG_STRINGS = 'strings'
LANG_CONSTANTS = 'constants'
REFERENCE_SELF = 'self'

# - Movement -------------------------------------
DIR_NORTH = 1
DIR_SOUTH = 2
DIR_EAST = 4
DIR_WEST = 8
DIR_UP = 16
DIR_DOWN = 32

# - Commands -------------------------------------
COMMAND_EXIT = 33
COMMAND_MOVE = 34
COMMAND_LOOK = 35
COMMAND_MOVE_NORTH = 36
COMMAND_MOVE_SOUTH = 37
COMMAND_MOVE_EAST = 38
COMMAND_MOVE_WEST = 39
COMMAND_MOVE_UP = 40
COMMAND_MOVE_DOWN = 41


# = String Codes ==============================================================

# - String Code Generation -----------------------
_STRING_CODE = 0


def _STRING_CODE_GENERATOR():
    global _STRING_CODE
    _STRING_CODE += 64
    return _STRING_CODE


# - Client Interface -----------------------------
CLIENT_PROMPT = _STRING_CODE_GENERATOR()

# - Problems (exceptions) ------------------------
MESSAGE_ALIAS_UNKNOWN = _STRING_CODE_GENERATOR()
MESSAGE_REFERENCE_UNKNOWN = _STRING_CODE_GENERATOR()
MESSAGE_ARGUMENTS_MANY = _STRING_CODE_GENERATOR()
MESSAGE_ARGUMENTS_FEW = _STRING_CODE_GENERATOR()
MESSAGE_EXIT_DISALLOWED = _STRING_CODE_GENERATOR()
MESSAGE_ENTRY_DISALLOWED = _STRING_CODE_GENERATOR()
MESSAGE_CANNOT_MOVE = _STRING_CODE_GENERATOR()
MESSAGE_NO_EXIT = _STRING_CODE_GENERATOR()

# - Names and Descriptions -----------------------
NAME_SELF = _STRING_CODE_GENERATOR()
NAME_PLACE_OUTSIDE = _STRING_CODE_GENERATOR()
NAME_PLACE_FOYER = _STRING_CODE_GENERATOR()
NAME_PLACE_OVERLOOK = _STRING_CODE_GENERATOR()
NAME_PLACE_NARROW = _STRING_CODE_GENERATOR()
NAME_PLACE_TREASURE = _STRING_CODE_GENERATOR()
NAME_ITEM_DEFAULT = _STRING_CODE_GENERATOR()
DESCRIPTION_PLACE_OUTSIDE = _STRING_CODE_GENERATOR()
DESCRIPTION_PLACE_FOYER = _STRING_CODE_GENERATOR()
DESCRIPTION_PLACE_OVERLOOK = _STRING_CODE_GENERATOR()
DESCRIPTION_PLACE_NARROW = _STRING_CODE_GENERATOR()
DESCRIPTION_PLACE_TREASURE = _STRING_CODE_GENERATOR()
DESCRIPTION_ITEM_DEFAULT = _STRING_CODE_GENERATOR()


# = Utilities =================================================================

# - Exceptions -----------------------------------
class GAME_PROBLEM(Exception):
    def __init__(self, problem_type, *args):
        self.problem_type = problem_type
        self.data = args


class ERROR_NO_STRING(Exception):
    pass


# - Math -----------------------------------------
def DIR_FLIP(direction):
    flip_dir = 0
    if(direction & DIR_NORTH):
        flip_dir |= DIR_SOUTH
    if(direction & DIR_SOUTH):
        flip_dir |= DIR_NORTH
    if(direction & DIR_EAST):
        flip_dir |= DIR_WEST
    if(direction & DIR_WEST):
        flip_dir |= DIR_EAST
    if(direction & DIR_UP):
        flip_dir |= DIR_DOWN
    if(direction & DIR_DOWN):
        flip_dir |= DIR_UP
    return flip_dir
