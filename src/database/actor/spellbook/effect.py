from typing import Callable
from game_object import GameObject

class Effect(GameObject):
    def __init__(self, name:str, duration:int, description:str = "A custom effect", 
    function:Callable = lambda _:print("Custom effect is triggered"), level:int = 1) -> None:
        # An math.inf value will be passed as duration for permanent effect.
        super().__init__(name, description, function)
        self._duration:int = duration
        self._level:int = 1
        self._intensity = 1

    def trigger(self, target):
        self._trigger(target, self._level, self._intensity)
        self._duration -= 1

    @property
    def intensity(self) -> str:
        return self._intensity

    @property
    def level(self) -> str:
        return self._level
    
    @intensity.setter
    def intensity(self, change:int):
        # Change can be negative or positive value
        self._intensity += change

    @level.setter
    def level(self, value:int) -> None:
        if value > 3 or value < 1:
            raise ValueError("Effect level must be only 1, 2 or 3")
        self._level = value


