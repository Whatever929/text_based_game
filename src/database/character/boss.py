from typing import Dict, Tuple, List

class Boss(object):
    def __init__(self, name: str, location: Tuple, engaged:bool = False, flee:bool = False) -> None:
        self._name = name
        self._engaged = engaged
        self._location = location
        self._flee = flee
    
    def idle_move(self):
        # Pass in a list of abilities and spell.
        return ["regenerate"]

    def engaged_move(self) -> List:
        # Pass in a list of abilities and spell.
        return ["calling for help"]