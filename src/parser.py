

# = Command Parsing ===========================================================

# - Dependencies ---------------------------------
# Language Modules
# Game Modules
from config import *
from language import MESSAGE


# = Parser ====================================================================

class Parser:

    # - Initialization -------------------------------
    def __init__(self):
        self.language = LANGUAGE_DEFAULT

    # - Command Parsing ------------------------------
    def parse(self, command):
        if(not command):
            return
        # Split command into words
        words = command.split(' ')
        verb = words[0]
        # Check for exit command
        if(verb is COMMAND_EXIT):
            exit(0)

    def get_string(string_code, *args):
        # Get message for language
        try:
            template = MESSAGE[self.language][string_code]
        except KeyError:
            template = MESSAGE[self.language][MESSAGE_STRING_NOT_FOUND]
            return template.formate(string_code)
        # Format message
        return template.formate(*args)


# = Verb ======================================================================

class Verb:
    def __init__(self, **options):
