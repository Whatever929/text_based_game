import random

from actor.character import Character
from character.spellbook.mage_spell import mage_spell


class Mage(Character):
    def __init__(self, name: str, location:Tuple = (1,1)):
        super().__init__(name, location)
        self._level = 1
        self._mana = 150
        self._hp = 200
        self._original = {"atk": 10, "hp": 200, "mana": 150}
        self._spellbook = mage_spell
        self._spell = []

    @property
    def mana(self):
        return self._mana

    def change_mana(self, change:int) -> int:
        self._mana += change
        self.negative_to_zero("_mana")

    def level_up(self) -> int:
        self._original["atk"] += 10
        self._original["hp"] += 50
        self._original["mana"] += 35
        self.choose_abilities()
        self.restore()        

    def choose_abilities(self) -> int:
        random_3 = random.sample(self._spellbook)
        print("Please select a skill: \n")
        for i, s in random_3:
            print("{}. {}:{}".format(i + 1, s.name, s.description))
        selection = input("Enter the index of the skill:")
        while (type(selection) != int or not 0 < selection < 3):
            print("Please enter a valid index")
            selection = input("Enter the index of the skill:")
        self._spell.append(random_3[selection - 1])
        return 0

    def restore(self) -> int:
        # Set everything to original, if attribute is applicable.
        for i, n in self._original.items():
            setattr(self, "_" + i, n)
        return 0


        