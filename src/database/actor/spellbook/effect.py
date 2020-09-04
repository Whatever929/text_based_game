from typing import Callable

class Effect(object):
    def __init__(self, name:str, duration:int, level:int = 1) -> None:
        # An math.inf value will be passed as duration for permanent effect.
        self._name = name
        self._duration:int = duration
        self._level:int = 1
        self._intensity = 1
        self._description = "A custom effect"
        self._trigger:Callable = None

    def trigger(self, target):
        self._trigger(target, self._level, self._intensity)
        self._duration -= 1

    @intensity.setter
    def intensity(self, change:int):
        # Change can be negative or positive value
        self._intensity += change

    @description.setter
    def description(self, explanation: str) -> None:
        self._description = explanation

    @level.setter
    def level(self, value:int) -> None:
        if value > 3 or value < 1:
            raise ValueError("Effect level must be only 1, 2 or 3")
        self._level = value

