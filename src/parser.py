
# = Parser ====================================================================

# - Dependencies ---------------------------------
from config import *


# - Initialization -------------------------------
class Parser:
    def parse(self, command):
        if(not command):
            return
        # Split command into words
        words = command.split(' ')
        verb = words[0]
        # Check for exit command
        if(verb is COMMAND_EXIT):
            exit(0)
