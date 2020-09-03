from typing import Tuple
import sys

from character.character_generator import character_generator
from map_resources.room import Room
from character.beast import Beast
from character.boss import Boss


class Database(object):
    def __init__(self, hero_info:Tuple, boss_type, room_size: Tuple, difficulty:int = 1, turn = 0) -> None:
        # Hero_info is expected to be name and class.
        self._room = Room(room_size)
        self._hero = character_generator(name=hero_info[0], character_class=hero_info[1])
        self._monster_list = []
        if boss_type == "beast":
            self._boss = Beast(location = (1,1))
        self._difficulty = difficulty
        self._turn = turn
    
    @property
    def room(self):
        return self._room.show_map()

    @property
    def hero(self):
        return "All information about hero goes here."

if __name__ == "__main__":
    database = Database(hero_info = ("Madin", "Mage"), boss_type = "beast", room_size = (5,5))
    print(database.room)