

# = Command Parsing ===========================================================

# - Dependencies ---------------------------------
# Language Modules
from inspect import signature
# Game Modules
from config import *
from language import languages


# = Parser ====================================================================

class Parser:
    """
    Command parser for accepting input from the player, and executing commands.
    This is the main point of contact between the player and the game,
    providing most input and output.
    """
    def __init__(self, player):
        self.player = player
        # Set language
        self.language = LANGUAGE_DEFAULT

    # - Input / Output -------------------------------
    def input(self):
        """Queries the system for player input, then parses it."""
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
        """Outputs to the console the result of parsed commands."""
        for line in message:
            print(line)
        print('\n')

    # - Command Parsing ------------------------------
    def parse(self, command):
        """
        Parses command text for Verb Aliases and Object References.
        The first word of a command is interpreted as a verb alias.
        Subsequent words are interpreted as references to game objects or basic
        game concepts (i.g. directions).
        The verb is then executed, passing said references as parameters.
        The result is then output as text to the client.
        """
        # Split command into words
        words = command.lower().split(' ')
        verb_alias = words.pop(0)
        # Retrieve verb by alias
        aliases = languages[self.language][LANG_ALIASES]
        try:
            verb_code = aliases[verb_alias]
        except KeyError:
            return [self.get_string(MESSAGE_ALIAS_UNKNOWN, verb_alias)]
        command_verb = verbs[verb_code]
        # Check if arguments match verb signature
        needed_args = len(signature(command_verb).parameters) - 1  # player
        if(needed_args < len(words)):
            return [self.get_string(MESSAGE_ARGUMENTS_MANY, verb_alias)]
        elif(needed_args > len(words)):
            return [self.get_string(MESSAGE_ARGUMENTS_FEW, verb_alias)]
        # Execute command
        try:
            references = [self.resolve_reference(word) for word in words]
            result = command_verb(self.player, *references)
        except GAME_PROBLEM as problem:
            return [self.get_string(problem.problem_type, *problem.data)]
        # Parse Result
        room_data = result["room"]
        lines = [
            self.get_string(room_data["name"]),
            self.get_string(room_data["description"]),
        ]
        for content in room_data["contents"]:
            lines.append(self.get_string(content["name"]))
        return lines

    def resolve_reference(self, token):
        """
        Returns a game object or simple game concept (i.g. direction)
        corresponding to the provided token. Raises an exception if no such
        game object can be found.
        """
        language = languages[self.language]
        # Attempt to get reference from language constant (like directions)
        reference = None
        try:
            reference = language[LANG_CONSTANTS][token]
        except KeyError:
            pass
        if(reference):
            # Parse language constant
            if(reference is REFERENCE_SELF):
                return self.player
            return reference
        # Attempt to get reference from environment
        # Raise an exception if token cannot be referenced
        raise GAME_PROBLEM(MESSAGE_REFERENCE_UNKNOWN, token)

    # - String Formatting ----------------------------
    def get_string(self, string_code, *args):
        """
        Translates the provided code and data into a string in the client's
        language.
        """
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
    """A command the player can execute by typing an Alias."""
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

Verb(COMMAND_MOVE, lambda player, direction: player.move(direction))
Verb(COMMAND_MOVE_NORTH, lambda player: player.move(DIR_NORTH))
Verb(COMMAND_MOVE_SOUTH, lambda player: player.move(DIR_SOUTH))
Verb(COMMAND_MOVE_EAST, lambda player: player.move(DIR_EAST))
Verb(COMMAND_MOVE_WEST, lambda player: player.move(DIR_WEST))
Verb(COMMAND_MOVE_UP, lambda player: player.move(DIR_UP))
Verb(COMMAND_MOVE_DOWN, lambda player: player.move(DIR_DOWN))
