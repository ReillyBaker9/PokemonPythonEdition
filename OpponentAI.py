from Classes import *
from Moves import oppAttackMult, oppDefenseMult, oppSpattackMult, oppSpdefenseMult, oppSpeedMult
from random import randint

def switch_on_faint(opponent):
    global oppAttackMult, oppDefenseMult, oppSpattackMult, oppSpdefenseMult, oppSpeedMult
    for mon in opponent.team:
        if mon.hp > 0:
            print(f"{opponent.name} sent out {mon.name}!")
            oppAttackMult = oppDefenseMult = oppSpattackMult = oppSpdefenseMult = oppSpeedMult = 0
            return mon 
    print(f"{opponent.name} has no Pokemon remaining!")
    return None