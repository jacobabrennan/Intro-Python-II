

# = Create game world =========================================================

# - Dependencies ---------------------------------
# Language Modules
# Game Modules
from config import *
from room import Room
from player import Player
from parser import Parser

# - Declare all the rooms ------------------------
room = {
    NAME_PLACE_OUTSIDE:  Room(NAME_PLACE_OUTSIDE, DESCRIPTION_PLACE_OUTSIDE),
    NAME_PLACE_FOYER:    Room(NAME_PLACE_FOYER, DESCRIPTION_PLACE_FOYER),
    NAME_PLACE_OVERLOOK: Room(NAME_PLACE_OVERLOOK, DESCRIPTION_PLACE_OVERLOOK),
    NAME_PLACE_NARROW:   Room(NAME_PLACE_NARROW, DESCRIPTION_PLACE_NARROW),
    NAME_PLACE_TREASURE: Room(NAME_PLACE_TREASURE, DESCRIPTION_PLACE_TREASURE),
}

# - Link rooms together --------------------------
room[NAME_PLACE_OUTSIDE].add_exit(room[NAME_PLACE_FOYER], DIRECTION_NORTH)
room[NAME_PLACE_FOYER].add_exit(room[NAME_PLACE_OUTSIDE], DIRECTION_SOUTH)
room[NAME_PLACE_FOYER].add_exit(room[NAME_PLACE_OVERLOOK], DIRECTION_NORTH)
room[NAME_PLACE_FOYER].add_exit(room[NAME_PLACE_NARROW], DIRECTION_EAST)
room[NAME_PLACE_OVERLOOK].add_exit(room[NAME_PLACE_FOYER], DIRECTION_SOUTH)
room[NAME_PLACE_NARROW].add_exit(room[NAME_PLACE_FOYER], DIRECTION_WEST)
room[NAME_PLACE_NARROW].add_exit(room[NAME_PLACE_TREASURE], DIRECTION_NORTH)
room[NAME_PLACE_TREASURE].add_exit(room[NAME_PLACE_NARROW], DIRECTION_SOUTH)


# = Main ======================================================================

# Create parser to handle interfacing with the player.
main_parser = Parser()
# Make a new player object that is currently in the 'outside' room.
main_player = Player()
start_room = room[NAME_PLACE_OUTSIDE]
start_room.contain(main_player)

# Write the game loop
while(True):
    # Get player command
    player_command = input(CLIENT_PROMPT)
    main_parser.parse(player_command)
