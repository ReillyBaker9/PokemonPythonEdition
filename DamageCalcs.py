from random import randint
from Types import type_effectiveness


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
        if move.moveType == "Special":
            if Attacker.current_pokemon.spattack > Attacker.current_pokemon.battleSpattack:
                attacking_stat = Attacker.current_pokemon.spattack
            else:
                attacking_stat = Attacker.current_pokemon.battleSpattack
            # if the effective defending stat is higher than the base, use the base
            if Defender.current_pokemon.spdefense < Defender.current_pokemon.battleSpdefense:
                defending_stat = Defender.current_pokemon.spdefense
            else:
                defending_stat = Defender.current_pokemon.battleSpdefense
        else:
            if Attacker.current_pokemon.attack > Attacker.current_pokemon.battleAttack:
                attacking_stat = Attacker.current_pokemon.attack
            else:
                attacking_stat = Attacker.current_pokemon.battleAttack
            if Defender.current_pokemon.defense < Defender.current_pokemon.battleDefense:
                defending_stat = Defender.current_pokemon.defense
            else:
                defending_stat = Defender.current_pokemon.battleDefense
    # stats used/impacted change depending on the move type
    if move.moveType == "Special":
        attacking_stat = Attacker.current_pokemon.battleSpattack
        defending_stat = Defender.current_pokemon.battleSpdefense
    else:
        attacking_stat = Attacker.current_pokemon.battleAttack
        defending_stat = Defender.current_pokemon.battleDefense
    # based on Pokemon wiki
    level_const = 42
    # all equations are from wiki
    base_damage = ((level_const * move.power * (attacking_stat / defending_stat)) / 50) + 2
    # adding Same Type Attack Bonus if attack type matches user's
    if move.type in Attacker.current_pokemon.type:
        stab_mult = 1.5
    else:
        stab_mult = 1.0
    # all attacks include a random bounded multiplier
    random_factor = (randint(85, 100)) / 100
    # the type multiplier changes based on the effectiveness of the move
    # supereffective moves have higher multipliers, not very effective less
    type_mult = 1.0
    for defender_type in Defender.current_pokemon.type:
        if defender_type in type_effectiveness.get(move.type, {}):
            type_mult *= type_effectiveness[move.type][defender_type]
    # Print effectiveness message, if present
    if type_mult > 1:
        print("It's super effective!")
    elif type_mult < 1:
        print("It's not very effective...")

    damage = int(base_damage * stab_mult * random_factor * type_mult * critMult)
    # updating the hp based on the total damage value
    Defender.current_pokemon.battleHp = int(Defender.current_pokemon.battleHp - damage)
    return