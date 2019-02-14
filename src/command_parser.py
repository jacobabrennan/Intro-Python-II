

# = Command Parsing ===========================================================

# - Dependencies ---------------------------------
# Language Modules
# Game Modules
from config import *
from language import MESSAGE


# = Parser ====================================================================

class Parser:
    def __init__(self):
        self.language = LANGUAGE_DEFAULT

    # - Input / Output -------------------------------
    def input(self):
        #
        try:
            player_command = input(self.get_string(CLIENT_PROMPT))
        except EOFError:
            player_command = ''
        #
        result = self.parse(player_command)
        #
        self.output(result)

    def output(self, message):
        print('\n'+message+'\n')

    # - Command Parsing ------------------------------
    def parse(self, command):
        # Split command into words
        words = command.split(' ')
        verb = words[0]
        # Check for exit command
        # if(verb is COMMAND_EXIT):
        #     exit(0)
        # Execute command
        try:
            pass
        except GAME_PROBLEM as problem:
            return get_string(problem.problem_type, *problem.data)
        return "Working"

    def get_string(self, string_code, *args):
        # Get message for language
        try:
            template = MESSAGE[self.language][string_code]
        except KeyError:
            template = MESSAGE[self.language][MESSAGE_STRING_NOT_FOUND]
            return template.format(string_code)
        # Format message
        return template.format(*args)


# = Verb ======================================================================

class Verb:
    def __init__(self, **options):
        pass
