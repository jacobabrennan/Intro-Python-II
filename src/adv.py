from config import *
from room import Room
from player import Player
from parser import Parser


# = Create game world =========================================================

# - Declare all the rooms ------------------------
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# - Link rooms together --------------------------
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# = Main ======================================================================
# Create client to handle interfacing with the player.
client = Client()
# Make a new player object that is currently in the 'outside' room.
main_player = Player()
start_room = room['outside']
start_room.contain(main_player)

# Write the game loop
while(True):
    # Get player command
    player_command = input(CLIENT_PROMPT)
    main_parser.parse(player_command)
