from typing import Dict, Tuple

class Boss(object):
    def __init__(self, name: str, location: Tuple, engaged:bool = False, flee:bool = False) -> None:
        self._name = name
        self._engaged = engaged
        self._location = location
        self._flee = flee
