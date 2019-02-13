

# = Room ======================================================================
# Implement a class to hold room information. This should have name and
# description attributes.

# - Dependencies ---------------------------------
import contents
from config import *


# - Initialization -------------------------------
class Room(contents.Container):
    def __init__(self, name, description):
        # Configure name and description
        self.name = name
        self.description = description
        # Set exit locations to default (None)
        self.n_to = None  # Cardinal compass directions
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.u_to = None  # Up and Down
        self.d_to = None

    # - Movement -------------------------------------
    def get_exit(self, direction):
        if(direction is DIRECTION_NORTH):
            return self.n_to
        if(direction is DIRECTION_SOUTH):
            return self.s_to
        if(direction is DIRECTION_EAST):
            return self.e_to
        if(direction is DIRECTION_WEST):
            return self.w_to
        if(direction is DIRECTION_UP):
            return self.u_to
        if(direction is DIRECTION_DOWN):
            return self.d_to
