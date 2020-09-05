from actor.spellbook.effect import Effect

def burning(target):
    target.change_hp(-10)

def shrink(target):
    target.change_atk(-5)

def enraged(target):
    target.change_atk(10)

def replenish(target):
    target.change_hp(15)

effect_list = [
    Effect("burning", 3, "Ignite the enemy on fire, inflicting damage over time.", burning),
    Effect("shrink", 3, "Make enemy as small as a gnome. Enemies's DPS reduced", shrink),
    Effect("enraged", 3, "Utilize 1% more of your potential. Increase DPS.", enraged),
    Effect("replenish", 2, "Heal yourself over time.", enraged),
    ]
