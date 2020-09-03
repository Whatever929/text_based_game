from typing import Tuple

from character.boss import Boss
from character.random.name_generator import generate_boss_name


class Beast(Boss):
    def __init__(self, location:Tuple, name: str = "Unnamed", engaged: bool = False, flee: bool = False) -> None:
        if name == "Unnamed":
            name = generate_boss_name("beast")
        super().__init__(name, location, engaged, flee)

    def idle_move(self):
        # Beast-specific spell when idle.
        return ['hunt']

    def engaged_move(self):
        return ['bloodthirst']
