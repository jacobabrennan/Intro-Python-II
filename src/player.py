

# = Player ====================================================================
# Write a class to hold player information, e.g. what room they are in
# currently.

# - Dependencies ---------------------------------
# Language Modules
# Game Modules
from config import *
import contents


# - Initialization -------------------------------
class Player(contents.Containable):

    # - Movement -------------------------------------
    def move(self, direction):
        """
        Attempts to move self between rooms in the specified direction.
        Returns data about new surroundings if successful.
        """
        # Find current location. Cancel if not currently in a location.
        current_loc = self.location
        if(not current_loc):
            raise GAME_PROBLEM(MESSAGE_CANNOT_MOVE, self)
        # Attempt to get new room from current location.
        # This will fail in when self isn't located in a Room.
        try:
            new_loc = current_loc.get_exit(direction)
        except AttributeError:
            raise GAME_PROBLEM(MESSAGE_NO_EXIT, direction)
        # Cancel if no exit in that direction
        if(not new_loc):
            raise GAME_PROBLEM(MESSAGE_NO_EXIT, direction)
        # Attempt to move into new location
        new_loc.contain(self)
        # Compile data about new surroundings, and return
        return self.surroundings()

    # - ----------------------------------------------
    def surroundings(self):
        current_room = self.location
        package = {
            "room": current_room.pack(),
        }
        return package
