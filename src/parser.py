# This module takes user input after prompt.py failed to process the input.
# The module will return a tuple of instruction, a tuple of None if failed.
from typing import Tuple
import re

def parser(user_input: str) -> Tuple:
    user_input = user_input.lower()
    if re.match(r'move', user_input):
        if re.fullmatch(r'move\s+(right|east)', user_input):
            return ("move", "right")
        elif re.fullmatch(r'move\s+(left|west)', user_input):
            return ("move", "left")
        elif re.fullmatch(r'move\s+(up|north)', user_input):
            return ("move", "up")
        elif re.fullmatch(r'move\s+(down|south)', user_input):
            return ("move","down")
        else:
            return ("Invalid", )
    elif re.fullmatch(r'right|east', user_input):
        return ("move","right")
    elif re.fullmatch(r'left|west', user_input):
        return ("move","left")
    elif re.fullmatch(r'up|north', user_input):
        return ("move","up")
    elif re.fullmatch(r'left|south', user_input):
        return ("move","down")
    elif re.fullmatch(r'((inspect|check)\s+)?(hero|character)', user_input):
        return ("inspect","character")
    elif re.fullmatch(r'((open|look|inspect|check)\s+)?(bag|inventory)', user_input):
        return ("inspect","bag")
    elif re.fullmatch(r'(attack|kill|hit)', user_input):
        return ("action", "attack")
    elif re.fullmatch(r'(run\s+away|run|flee)', user_input):
        return ("action", "flee")
    elif re.fullmatch(r'objective|goal|mission', user_input):
        return ("system","objective")
    elif re.fullmatch(r'\?+|help', user_input):
        return ("system", "help")
    elif re.fullmatch(r'backup|save', user_input):
        return ("system", "save")
    elif re.fullmatch(r'location|map|where', user_input):
        return ("system", "map")
    else:
        return ("Invalid",)
