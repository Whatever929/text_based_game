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
        self._atk = 10
        self._hunger = 100
        self._location = location
        self._effect = []
        self._effect_book = []

    def take_damage(self, damage: int) -> int:
        # If 1 is passed, it signals the game to end.
        self._hp -= damage
        if self._hp <= 0:
            return 1
        return 0

    def process_effect(self) -> None:
        for effect in self._effect:
            # Process all the effect in the character
            pass

    def remove_effect(self, effect) -> None:
        if effect in self._effect:
            self._effect.remove(effect)

    def add_effect(self, effect) -> int:
        # Return 1 to signal effect already exist.
        if effect in self._effect:
            return 1
        else:
            self._effect.append(effect)
            return 0


if __name__ == "__main__":
    pass