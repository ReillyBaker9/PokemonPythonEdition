from Classes import *
from random import randint

def switch_on_faint(opponent):
    for mon in opponent.team:
        if mon.hp > 0:
            print(f"{opponent.name} sent out {mon.name}!")
            return mon 
    print(f"{opponent.name} has no Pokemon remaining!")
    return None