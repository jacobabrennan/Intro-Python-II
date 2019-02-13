

# = Room ======================================================================
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    # - Initialization -------------------------------
    def __init__(self, name, description):
        # Configure name and description
        self.name = name
        self.description = description
        # Initialize contents
        self.contents = []
        # Set exit locations to default (None)
        self.n_to = None  # Cardinal compass directions
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.u_to = None  # Up and Down
        self.d_to = None

    # - Movement -------------------------------------
    def enter(self, mover):
        # Determines if the mover is permitted to enter the room
        return True

    def exit(self, mover):
        # Determines if the mover is permitted to exit the room
        return True

    def entered(self, mover):
        # Called after the mover has entered the room
        pass

    def exited(self, mover):
        # Called after the mover has exited the room
        pass
