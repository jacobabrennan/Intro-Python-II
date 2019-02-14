

# = Map =======================================================================

# - Dependencies ---------------------------------
# Language Modules
# Game Modules
from config import *
from room import Room


# - Definition and Initialization ----------------
class Map:
    """A collection of Rooms linked by exits, and methods for managing them."""
    def __init__(self):
        self.rooms = {}
        self.load()

    # - Map Loading ----------------------------------
    def load(self):
        """Ready map for gameplay by loading and linking rooms."""
        # Declare all the rooms
        self.add_room(NAME_PLACE_OUTSIDE, DESCRIPTION_PLACE_OUTSIDE)
        self.add_room(NAME_PLACE_FOYER, DESCRIPTION_PLACE_FOYER)
        self.add_room(NAME_PLACE_OVERLOOK, DESCRIPTION_PLACE_OVERLOOK)
        self.add_room(NAME_PLACE_NARROW, DESCRIPTION_PLACE_NARROW)
        self.add_room(NAME_PLACE_TREASURE, DESCRIPTION_PLACE_TREASURE)
        # Link rooms together
        self.link_rooms(NAME_PLACE_OUTSIDE, NAME_PLACE_FOYER, DIR_NORTH)
        self.link_rooms(NAME_PLACE_FOYER, NAME_PLACE_OVERLOOK, DIR_NORTH)
        self.link_rooms(NAME_PLACE_FOYER, NAME_PLACE_NARROW, DIR_EAST)
        self.link_rooms(NAME_PLACE_NARROW, NAME_PLACE_TREASURE, DIR_NORTH)

    def link_rooms(self, name_from, name_to, direction, symmetric=True):
        """Creates an exit from one room to another."""
        # Create the exit
        start_room = self.rooms[name_from]
        end_room = self.rooms[name_to]
        start_room.add_exit(end_room, direction)
        # Create a return path (exit from end to start)
        if(not symmetric):
            return
        end_room.add_exit(start_room, DIR_FLIP(direction))

    # - Room Management --------------------------
    def get_room(self, room_name):
        """Gets a room by name, or None if no such room exists."""
        if(not (room_name in self.rooms)):
            return None
        return self.rooms[room_name]

    def add_room(self, room_name, room_description):
        """Add a room to the map."""
        self.rooms[room_name] = Room(room_name, room_description)

    def remove_room(self, room_name):
        """Remove a room from the map."""
        self.rooms.pop(room_name, None)
