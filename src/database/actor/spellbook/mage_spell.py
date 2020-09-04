from actor.spellbook.effect_list import effect_list

mage_spell = {}

def fireball(target, multiplier = 1):
    target.take_damage(40 * multiplier)

def burning_scorch(target):
    target.take_damage(20)
    target.add_effect