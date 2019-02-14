

# = Command Parsing ===========================================================

# - Dependencies ---------------------------------
# Language Modules
# Game Modules
from config import *
from language import languages


# = Parser ====================================================================

class Parser:
    def __init__(self, player):
        self.player = player
        # Set language
        self.language = LANGUAGE_DEFAULT
        # Generate verbs
        # self.verbs = {}

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
        words = command.lower().split(' ')
        verb_alias = words[0]
        # Retrieve verb by alias
        aliases = languages[self.language][LANG_ALIASES]
        try:
            verb_code = aliases[verb_alias]
        except KeyError:
            return self.get_string(MESSAGE_ALIAS_UNKNOWN, command_verb)
        command_verb = verbs[verb_code]
        # Execute command
        try:
            command_verb(self.player, *words[1:])
        except GAME_PROBLEM as problem:
            return self.get_string(problem.problem_type, *problem.data)
        return "Working"

    # - String Formatting ----------------------------
    def get_string(self, string_code, *args):
        # Get language dictionary
        strings = languages[self.language][LANG_STRINGS]
        # Get message for language
        try:
            # Try as a string_code (int) first
            template = strings[string_code]
        except KeyError:
            # If that fails, try as an object with a string_code name
            try:
                template = strings[string_code.name]
            # If that fails, raise a 'no string' exception
            except AttributeError:
                raise ERROR_NO_STRING(string_code)
        # Format numeric args to strings
        pass_args = []
        for arg in args:
            try:
                arg_string = self.get_string(arg)
            except ERROR_NO_STRING:
                arg_string = arg
            pass_args.append(arg_string)
        # Format message
        return template.format(*pass_args)


# = Verb ======================================================================


class Verb:
    def __init__(self, key, behavior, **options):
        # Store in verbs by key for access by the parser
        global verbs
        verbs[key] = self
        # Set attributes from arguments
        self.key = key
        self.behavior = behavior

    def __call__(self, player, *args):
        return self.behavior(player, *args)


verbs = {}

Verb(COMMAND_MOVE, lambda player, *args: player.move(*args))
