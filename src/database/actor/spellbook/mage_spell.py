from actor.spellbook.effect_list import effect_list
from actor.spellbook.spell import Spell

def fireball(target, level):
    target.change_hp(-40)

def scorch(target):
    target.change_hp(-10)
    target.add_effect("burning")

def freeze(target):
    target.add_effect("freeze")

def fire_orb(ally):
    ally.add_effect("fire_orb", stackable = True)
    ally.change_atk(+5)

def arcane_orb(ally):
    ally.add_effect("arcane_orb", stackable = True)
    ally.change_mana(+20)

def frost_orb(ally):
    # Slow down enemy attack speed, ie: increase chances of character to gain 1 more turn.
    ally.add_effect("frost_orb", stackable = True)

mage_spell = [
    Spell("fireball", 1, "Cast a fireball that deals large amount of damage to enemy."),
    Spell("freeze", 1, "Freeze the target, granting you extra turn."),
    Spell("fire_orb", 0, "Summon fire orb that grants you DPS. Max fire orbs: 3"),
    Spell("arcane_orb", 0, "Summon fire orb that grants you extra mana. Max arcane orbs: 3"),
    Spell("frost_orb", 0, "Summon frost orb that slows down enemies when they attacked you. Max frost orbs: 3"),
]