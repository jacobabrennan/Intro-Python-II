

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
    """
    The main form of location for both the player and other game objects.
    Provides exits for movement from one Room to another, and methods
    for managing exits.
    """
    def __init__(self, name, description):
        super().__init__()
        # Initialize iterables
        self.contents = []
        self.exits = {}
        # Configure name and description
        self.name = name
        self.description = description

    def pack(self):
        """Provides all necessary data to describe self to the client."""
        package = super().pack()
        package["contents"] = [thing.pack() for thing in self.contents]
        return package

    # - Movement -------------------------------------
    def add_exit(self, room, direction):
        """Adds an exit from one room to another, allowing movement."""
        self.exits[direction] = room

    def get_exit(self, direction):
        """
        Returns the exit from this Room in the provided direction,
        or None if no exit exists in that direction.
        """
        if(not (direction in self.exits)):
            return None
        return self.exits[direction]
