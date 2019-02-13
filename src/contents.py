

# = Containers and Containables - Base movement classes =======================

# - Dependencies ---------------------------------
import weakref


# = Container - game objects which can contain other objects ==================

class Container:
    def __init__(self):
        self.contents = None

    # - Movement -------------------------------------
    def contain(self, mover):
        """
        Attempt to place mover into contents.
        Returns a Boolean representation of success.
        """
        # Check if mover can exit old location
        old_location = mover.location
        if(not old_location):
            return False
        if(not old_location.allow_exit(mover)):
            return False
        # Check if mover can enter current location
        if(not self.allow_entry(mover)):
            return False
        # Set new location
        if(not self.contents):
            self.contents = []
        self.contents.append(mover)
        mover.location = self
        # Inform both locations of movement
        if(old_location):
            old_location.exited(mover)
        self.entered(mover)
        return True

    def allow_entry(self, mover):
        """Determines if the mover is permitted to enter the room"""
        return True

    def allow_exit(self, mover):
        """Determines if the mover is permitted to exit the room."""
        return True

    def entered(self, mover):
        """Called after the mover has entered the room."""
        pass

    def exited(self, mover):
        """Called after the mover has exited the room."""
        pass


# = Containable - game objects which can be contained in other objects ========

class Containable(Container):
    def __init__(self):
        super().__init__()
        self._location_resolver = None

    # - Location -------------------------------------
    @property
    def location(self):
        if(self._location_resolver):
            return self._location_resolver()
        return None

    @location.setter
    def location(self, newValue):
        if(not newValue):
            self._location_resolver = None
            return
        self._location_resolver = weakref.ref(newValue)
