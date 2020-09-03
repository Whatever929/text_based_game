from typing import Tuple
import random

def generate_boss_name(boss_type: str) -> str:
    if boss_type == "beast":
        return random.choice(["Whitetooth, Infernopaw, Bloodfang"])
    else:
        return "Custom Boss"