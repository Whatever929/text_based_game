from actor.character import Character
from character.spellbook.mage_spell import mage_spell


class Mage(Character):
    def __init__(self, name: str, location:Tuple = (1,1)):
        super().__init__(name, location)
        self._mana = 150
        self._hp = 200
        self._spellbook = mage_spell
        self._spell = []