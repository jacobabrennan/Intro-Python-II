

# = Room ======================================================================
# Implement a class to hold room information. This should have name and
# description attributes.

# - Dependencies ---------------------------------
# Language Modules
# Game Modules
from config import *
import contents


# - Initialization -------------------------------
class Room(contents.Container):
    def __init__(self, name, description):
        super().__init__()
        self.contents = []
        # Configure name and description
        self.name = name
        self.description = description
        # Setup exits
        self.exits = {}

    def pack(self):
        """Provides all necessary data to describe self to the client."""
        package = super().pack()
        package["contents"] = [thing.pack() for thing in self.contents]
        return package

    # - Movement -------------------------------------
    def add_exit(self, room, direction):
        self.exits[direction] = room

    def get_exit(self, direction):
        if(not (direction in self.exits)):
            return None
        return self.exits[direction]
