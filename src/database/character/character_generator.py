from typing import Tuple, Dict

def character_generator(name: str, character_class: str, location:Tuple = (1,1), difficulty:int = 1) -> Dict:
    # Generate characters based on arguments passed. Hero is only generated once, while monster will be
    # generated multiple times throughout the game. Location of the monsters is required to put the monster back
    # to the room should the character flees.
    character = {"name": name, "character_class": character_class, "location": location, "effect": []}

    if character_class == "Mage":
        character["hp"] = 400
        character["spell"] = []
        character["atk"] = 20
        character["mana"] = 100
        character["inventory"] = ["Breadstix"]
        character["hunger"] = 100


    elif character_class == "Warrior":
        character["hp"] = 650
        character["spell"] = []
        character["atk"] = 35
        character["rage"] = 0
        character["inventory"] = ["Breadstix"]
        character["hunger"] = 100

    # In future update, we will add classes to different monsters.
    elif character_class == "Monster":
        character["hp"] = 300 * difficulty
        character["atk"] = 20 * difficulty
        character["spell"] = ["Calling for help"]
    
    return character

if __name__ == "__main__":
    hero = character_generator(name = "James", character_class = "Mage")
    for i, v in hero.items():
        print(i, v)