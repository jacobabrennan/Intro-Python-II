

# = Player ====================================================================
# Write a class to hold player information, e.g. what room they are in
# currently.

# - Dependencies ---------------------------------
import contents


# - Initialization -------------------------------
class Player(contents.containable):

    # - Movement -------------------------------------
    def move(self, direction):
        """
        Attempts to move self between rooms in the specified direction
        Returns a Boolean representation of success.
        """
        # Find current location. Cancel if not currently in a location.
        current_loc = self.location
        if(not current_loc):
            return False
        # Attempt to get new room from current location.
        # This will fail in when self isn't located in a Room.
        try:
            new_loc = current_loc.get_exit(direction)
        except AttributeError:
            return False
        # Attempt to move into new location
        return new_loc.contain(self)
