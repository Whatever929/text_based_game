from typing import Tuple, Dict

from character.spellbook.mage_spell import mage_spell
from character.spellbook.warrior_spell import warrior_spell

class Character(object):
    # Generate characters based on arguments passed. Hero is only generated once, while monster will be
    # generated multiple times throughout the game. Location of the monsters is required to put the monster back
    # to the room should the character flees.
    def __init__(self, name: str, location:Tuple = (1,1)):
        self._name = name
        self._hp = 350
        self._original = {"atk": 10, "hp": 350}
        self._atk = 10
        self._hunger = 100
        self._location = location
        self._effect = []

    def change_hp(self, change: int) -> int:
        # If 1 is passed, it signals the game to end.
        self._hp += change
        if self._hp <= 0:
            return 1
        elif self._hp > self._original["hp"]:
            self._hp = self._original["hp"]
            return 2
        return 0

    def process_effect(self) -> None:
        for effect in self._effect:
            # Process all the effect in the character
            pass

    def remove_effect(self, effect:str) -> None:
        if effect in self._effect:
            self._effect.remove(effect)

    def add_effect(self, effect:str, stackable = False) -> int:
        # Return 1 to signal effect already exist.
        if effect in self._effect:
            if stackable == True:
                self._effect[effect].intensity = +1
                return 0
            else:
                return 1
        else:
            self._effect.append(effect)
            return 0
        
    def change_atk(self, change:int) -> int:
        self._atk += change
        self.negative_to_zero("_atk")
    
    def change_original(self, spec, change: int) -> int:
        self._original[spec] += change
        if self._original[spec]

    def negative_to_zero(self, attr:str) -> int:
        # Return 0 if no correction, 1 if there is correction.
        if getattr(self, attr) < 0:
            setattr(self, attr, 0)
            return 1
        else:
            return 0


if __name__ == "__main__":
    pass