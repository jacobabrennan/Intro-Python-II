

# = Item ======================================================================

# - Dependencies ---------------------------------
import contents


# - Initialization -------------------------------
class Item(contents.containable):
    def __init__(self):
        super().__init__()
        self.name = "item"
        self.description = "an item"
