from random import randint
from Types import type_effectiveness, type_mapping


def calcDamage(move, Attacker, Defender):
    # comes from damage calc page on pokemon wiki, stays same for level 100
    print(f"{Attacker.name}'s {Attacker.current_pokemon.name} used {move.name}!")
    critMult = 1
    # attack reductions and defense boosts are ignored if crit happens
    crit = randint(1, 24)
    if crit == 1:
        critMult = 1.5
        print("Critical hit!")
        # if the effective attacking stat is lower than the base, use the base
        if move.damage_class == "Special":
            if Attacker.current_pokemon.pokeStats['special-attack'] > Attacker.current_pokemon.battleStats['special-attack']:
                attacking_stat = Attacker.current_pokemon.pokeStats['special-attack']
            else:
                attacking_stat = Attacker.current_pokemon.battleStats['special-attack']
            # if the effective defending stat is higher than the base, use the base
            if Defender.current_pokemon.pokeStats['special-defense'] < Defender.current_pokemon.battleStats['special-defense']:
                defending_stat = Defender.current_pokemon.pokeStats['special-defense']
            else:
                defending_stat = Defender.current_pokemon.battleStats['special-defense']
        else:
            if Attacker.current_pokemon.pokeStats['attack'] > Attacker.current_pokemon.battleStats['attack']:
                attacking_stat = Attacker.current_pokemon.pokeStats['attack']
            else:
                attacking_stat = Attacker.current_pokemon.battleStats['attack']
            if Defender.current_pokemon.pokeStats['defense'] < Defender.current_pokemon.battleStats['defense']:
                defending_stat = Defender.current_pokemon.pokeStats['defense']
            else:
                defending_stat = Defender.current_pokemon.battleStats['defense']
    # stats used/impacted change depending on the move type
    if move.damage_class == "Special":
        attacking_stat = Attacker.current_pokemon.battleStats['special-attack']
        defending_stat = Defender.current_pokemon.battleStats['special-defense']
    else:
        attacking_stat = Attacker.current_pokemon.battleStats['attack']
        defending_stat = Defender.current_pokemon.battleStats['defense']
    # based on Pokemon wiki
    level_const = 42
    # all equations are from wiki
    base_damage = ((level_const * move.power * (attacking_stat / defending_stat)) / 50) + 2
    # adding Same Type Attack Bonus if attack type matches user's
    if move.move_type in Attacker.current_pokemon.type:
        stab_mult = 1.5
    else:
        stab_mult = 1.0
    # all attacks include a random bounded multiplier
    random_factor = (randint(85, 100)) / 100
    # the type multiplier changes based on the effectiveness of the move
    # supereffective moves have higher multipliers, not very effective less
    type_mult = 1.0
    for defender_type in Defender.current_pokemon.type:
        print(move.move_type + " against " + defender_type.name)
        if defender_type.name in type_effectiveness.get(move.move_type, {}):
            type_mult *= type_effectiveness[move.move_type][defender_type.name]
    # Print effectiveness message, if present
    print(type_mult)
    if type_mult > 1:
        print("It's super effective!")
    elif type_mult < 1:
        print("It's not very effective...")

    damage = int(base_damage * stab_mult * random_factor * type_mult * critMult)
    # updating the hp based on the total damage value
    print("Did " + str(damage) + " damage!")
    Defender.current_pokemon.battleStats['hp'] = int(Defender.current_pokemon.battleStats['hp'] - damage)
    return