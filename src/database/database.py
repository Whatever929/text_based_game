from character.character_generator import character_generator
from room import Room
from typing import Tuple

class Database(object):
    def __init__(self, hero_info:Tuple, boss_type, room_size: Tuple, difficulty:int = 1, turn = 0) -> None:
        # Hero_info is expected to be name and class.
        self._room = Room(room_size)
        self._hero = character_generator(name=hero_info[0], character_class=hero_info[1])
        self._monster_list = []
        self._boss = None
        self._difficulty = difficulty
        self._turn = turn

