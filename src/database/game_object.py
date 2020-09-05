from typing import Callable

class GameObject(object):
    def __init__(self, name, description:str = "A custom game object", function:Callable = lambda _:print("Game object is triggered")):
        self._name = name
        self._description = description
        self._function:Callable = function
        
    def trigger(self, target):
        self._function(target)

    @property
    def description(self) -> str:
        return self._description

    @property
    def function(self) -> str:
        return self.function

    @property
    def name(self) -> str:
        self._name.replace('_', ' ')
        return self._name.capitalize()

    @description.setter
    def description(self, explanation: str) -> None:
        self._description = explanation
    
    @function.setter
    def function(self, function_description: Callable):
        self._function = function_description