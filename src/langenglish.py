

# = English Language Strings ==================================================

# - Dependencies ---------------------------------
# Language Modules
# Game Modules
from config import *

# - Strings --------------------------------------
language = {
    LANG_CONSTANTS: {
        'north': DIR_NORTH,
        'south': DIR_SOUTH,
        'east': DIR_EAST,
        'west': DIR_WEST,
        'up': DIR_UP,
        'down': DIR_DOWN,
        'self': REFERENCE_SELF,
        'myself': REFERENCE_SELF,
        'yourself': REFERENCE_SELF,
    },
    LANG_ALIASES: {
        'north': COMMAND_MOVE_NORTH,
        'south': COMMAND_MOVE_SOUTH,
        'east': COMMAND_MOVE_EAST,
        'west': COMMAND_MOVE_WEST,
        'up': COMMAND_MOVE_UP,
        'down': COMMAND_MOVE_DOWN,
        'move': COMMAND_MOVE,
        'go': COMMAND_MOVE,
        'walk': COMMAND_MOVE,
    },
    LANG_STRINGS: {
        # Client interface
        CLIENT_PROMPT: 'Command:: ',
        # Game Metrics
        DIR_NORTH: 'North',
        DIR_SOUTH: 'South',
        DIR_EAST: 'East',
        DIR_WEST: 'West',
        DIR_UP: 'Up',
        DIR_DOWN: 'Down',
        # Exception messages
        MESSAGE_ALIAS_UNKNOWN: 'Unknown command: "{}"',
        MESSAGE_REFERENCE_UNKNOWN: 'Unknown reference: "{}"',
        MESSAGE_ARGUMENTS_MANY: 'Too much information provided to "{}"',
        MESSAGE_ARGUMENTS_FEW: 'Not enough information provided to "{}"',
        MESSAGE_EXIT_DISALLOWED: '{} cannot exit {}.',
        MESSAGE_EXIT_DISALLOWED: '{} cannot enter {}.',
        MESSAGE_CANNOT_MOVE: '{} cannot move.',
        MESSAGE_NO_EXIT: 'There is no exit in the direction of {}.',
        # Place names and descriptions
        NAME_SELF: 'You',
        NAME_PLACE_OUTSIDE: 'Outside Cave Entrance',
        NAME_PLACE_FOYER: 'Foyer',
        NAME_PLACE_OVERLOOK: 'Grand Overlook',
        NAME_PLACE_NARROW: 'Narrow Passage',
        NAME_PLACE_TREASURE: 'Treasure Chamber',
        DESCRIPTION_PLACE_OUTSIDE: 'North of you, the cave mount beckons',
        DESCRIPTION_PLACE_FOYER: """Dim light filters in from the south. \
Dusty passages run north and east.""",
        DESCRIPTION_PLACE_OVERLOOK: """A steep cliff appears before you, \
falling into the darkness. Ahead to the north, a light flickers in \
the distance, but there is no way across the chasm.""",
        DESCRIPTION_PLACE_NARROW: """The narrow passage bends here from west \
to north. The smell of gold permeates the air.""",
        DESCRIPTION_PLACE_TREASURE: """You've found the long-lost treasure \
chamber! Sadly, it has already been completely emptied by \
earlier adventurers. The only exit is to the south.""",
    }
}
