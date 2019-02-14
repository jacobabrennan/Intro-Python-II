

# = Constants and Utilities ===================================================


# = Simple Constants ==========================================================

# - Languages ------------------------------------
LANGUAGE_ENGLISH = 'English'
LANGUAGE_DEFAULT = LANGUAGE_ENGLISH

# - Movement -------------------------------------
DIRECTION_NORTH = 1
DIRECTION_SOUTH = 2
DIRECTION_EAST = 4
DIRECTION_WEST = 8
DIRECTION_UP = 16
DIRECTION_DOWN = 32

# - Commands -------------------------------------
COMMAND_EXIT = 33


# = String Codes ==============================================================

# - String Code Generation -----------------------
_STRING_CODE = 0


def _STRING_CODE_GENERATOR():
    global _STRING_CODE
    _STRING_CODE += 1
    return _STRING_CODE

# - Client Interface -----------------------------
CLIENT_PROMPT = _STRING_CODE_GENERATOR()

# - Problems (exceptions) ------------------------
MESSAGE_EXIT_DISALLOWED = _STRING_CODE_GENERATOR()
MESSAGE_ENTRY_DISALLOWED = _STRING_CODE_GENERATOR()
MESSAGE_CANNOT_MOVE = _STRING_CODE_GENERATOR()
MESSAGE_NO_EXIT = _STRING_CODE_GENERATOR()
MESSAGE_STRING_NOT_FOUND = _STRING_CODE_GENERATOR()

# - Names and Descriptions -----------------------
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


# = Problems (exceptions) =====================================================

class GAME_PROBLEM(Exception):
    def __init__(self, problem_type, *args):
        self.problem_type = problem_type
        self.data = args
