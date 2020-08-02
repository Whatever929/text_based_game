# This module takes user input after prompt.py failed to process the input.
# The module will return a tuple of instruction, a tuple of None if failed.
from typing import Tuple
import re

def parser(user_input: str) -> Tuple:
    if user_input == "Move right":
        return ("move", "right")