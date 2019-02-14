

# = Item ======================================================================

# - Dependencies ---------------------------------
# Language Modules
# Game Modules
import contents


# - Initialization -------------------------------
class Item(contents.containable):
    def __init__(self):
        super().__init__()
        self.name = NAME_ITEM_DEFAULT
        self.description = DESCRIPTION_ITEM_DEFAULT
