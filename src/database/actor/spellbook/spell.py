from typing import Callable
from game_object import GameObject

class Spell(GameObject):
    def __init__(self, name:str, level:int = 1, description:str = "A custom spell.", function:Callable = lambda _:print("Custom spell is triggered")) -> None:
        super().__init__(name, description, function)
        self._level = level

    def trigger(self, target) -> int:
        return self._function(target, self._level)
    
    @property
    def level(self) -> str:
        return self._level

    @level.setter
    def level(self, value:int) -> None:
        if value > 3 or value < 0:
            raise ValueError("Effect level must be only 1, 2 or 3; 0 being not applicable")
        self._level = value