

# = Create game world =========================================================

# - Dependencies ---------------------------------
# Language Modules
# Game Modules
from config import *
from player import Player
from command_parser import Parser
from geography import Map

# - Main -----------------------------------------
# Create parser to handle interfacing with the player.
main_player = Player()
main_parser = Parser(main_player)
# Setup new game world
main_map = Map()
main_map.load()
start_room = main_map.get_room(NAME_PLACE_OUTSIDE)
start_room.contain(main_player)
# Write the game loop
while(True):
    # Get player command
    main_parser.input()
