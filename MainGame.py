from Classes import *
from Pokedex import *
from random import randint
import copy


def initializeGame():
    # define the player as a global variable to add a team to
    global Player
    # Player.name = input("What is your name? ")
    Player.name = "Reilly"
    Player.team = []
    Player.x = 0
    Player.y = 0
    # temporarily set team to three starter evos
    mon1 = copy.copy(Venusaur)
    mon2 = copy.copy(Charizard)
    mon3 = copy.copy(Blastoise)
    Player.team.append(mon1)
    Player.team.append(mon2)
    Player.team.append(mon3)

    # print the team name for reference
    for k in range(len(Player.team)):
        print(Player.team[k].name)

    # for i in range(3):
    # for listing the available options. Leaving disabled
    # print("Choose a Pokemon:")
    # for j in range(len(Pokedex)):
    #     print(str(j + 1) + ". " + Pokedex[j].name)

    # for choosing a Pokemon. Auto assigning for now
    # choice = int(input("Enter the number of the Pokemon you want: ")) - 1
    # Player.team.append(Pokedex[choice])
    # print("You chose " + Pokedex[choice].name + "!")
    # print("Your team so far: ")


def startBattle():
    # arbitrarily assign opponent team
    opp_mon1 = copy.copy(Venusaur)
    opp_mon2 = copy.copy(Pidgey)
    opp_mon3 = copy.copy(Caterpie)
    opp_mon4 = copy.copy(Charmander)
    opponent = Opponent("Gary", [opp_mon1, opp_mon2, opp_mon3, opp_mon4])
    print("You are challenged by " + opponent.name + "!")
    print("Opponent's team: ")
    for i in range(len(opponent.team)):
        print(opponent.team[i].name)
    player_mon = Player.team[0]
    opponent_mon = opponent.team[0]
    print("Go! " + player_mon.name + "!")
    print("Opponent sent out " + opponent_mon.name + "!")
    return player_mon, opponent_mon

def calcPriority(move, mySpeed, oppSpeed):
        speedTie = randint(1, 2)
        if mySpeed < oppSpeed:
            return 1
        if mySpeed == oppSpeed:
            if speedTie == 1:
                return 1
            else:
                return 2
        else:
            return 2


def calcDamage(move, Attacker, Defender):
        # comes from damage calc page, stays same for level 100
        print("The HP of " + Defender.name + " is: " + str(Defender.hp))
        print(Attacker.name + " used " + move.name + "!")
        if move.moveType == "Special":
            attacking_stat = Attacker.spattack
            defending_stat = Defender.spdefense
        else:
            attacking_stat = Attacker.attack
            defending_stat = Defender.defense
        level_const = 42
        base_damage = ((level_const * move.power * (attacking_stat / defending_stat)) / 50) + 2
        if move.type in Attacker.type:
            stab_mult = 1.5
        else:
            stab_mult = 1.0
        random_factor = (randint(85, 100)) / 100
        type_mod = checkType(move, Defender)
        damage = int(base_damage * stab_mult * random_factor * type_mod)
        Defender.hp = int(Defender.hp - damage)
        print("The HP of " + Defender.name + " is now: " + str(Defender.hp))
        return str(damage)


def checkType(move, defender):
        type_mod = 1
        for defender_type in defender.type:
            if defender_type in move.type.strong_against:
                type_mod *= 2
            elif defender_type in move.type.weak_against:
                type_mod *= 0.5
            elif defender_type in move.type.no_effect_against:
                type_mod *= 0
        if type_mod > 1:
            print("It's super effective!")
        elif type_mod < 1:
            print("It's not very effective")
        elif type_mod == 0:
            print("The move had no effect.")
        return type_mod


def checkAccuracy(move):
        check = randint(1, 100)
        if check > move.accuracy:
            print(move.name + " missed!")
            return
        else:
            if move.moveType == "Status":
                # setStats()
                return
            else:
                return 1
                # calcDamage(move, PlayerMon, OpponentMon)

def playerSwitch(player_mon):
    for k in range(len(Player.team)):
        print(str(k + 1) + ". " + Player.team[k].name)
    mon = int(input("Which Pokemon will you switch to? ")) - 1
    if Player.team[mon] == player_mon or Player.team[mon].hp <= 0:
        print("Can't switch to that Pokemon!")
        return playerSwitch(player_mon)
    else:
        player_mon = Player.team[mon]
        print("Switched to " + player_mon.name)
        return player_mon

def setStats(Attacker, Defender, operation):
    return

def playerHealthCheck(player_mon, opponent_mon):
    if player_mon.hp <= 0:
        print(Player.name + "'s " + player_mon.name + " fainted!")
        Turn(playerSwitch(player_mon), opponent_mon)
        return

def opponentTurn(player_mon, opponent_mon):
        move = randint(0, (len(opponent_mon.moves) - 1))
        chosen_move = opponent_mon.moves[move]
        if checkAccuracy(chosen_move) == 1:
            print("Opponent's " + opponent_mon.name + " attacked for " + calcDamage(chosen_move, opponent_mon,
                                                                                    player_mon) + " damage!")
        return player_mon
    
       
def Turn(player_mon, opponent_mon):
    # leave it as 0 for now
    stat_change = 0
    # if stat_change == 1:
    #     setStats()
    print("What will you do?")
    print("1. Fight")
    print("2. Switch Pokemon")
    print("3. Bag")
    acceptable_inputs = ["1", "2", "3"]
    battle_choice = input("Choice: ")
    while battle_choice not in acceptable_inputs:
        print("Invalid selection.")
        battle_choice = input("Choice: ")
    if battle_choice == "1":
        print("Use which move?")
        for i in range(len(player_mon.moves)):
            print(str(i + 1) + ". " + str(player_mon.moves[i].name))
        try:
            move_index = int(input("Select move: ")) - 1
        except ValueError:
            move_index = -1
        while move_index not in [0, 1, 2, 3]:
            print("Invalid selection.")
            try:
                move_index = int(input("Select move: ")) - 1
            except ValueError:
                move_index = -1
        # If opponent is faster:
        if calcPriority(player_mon.moves[move_index], player_mon.speed, opponent_mon.speed) == 1:
            opponentTurn(player_mon, opponent_mon)
            playerHealthCheck(player_mon, opponent_mon)
            if checkAccuracy(player_mon.moves[move_index]) == 1:
                calcDamage(player_mon.moves[move_index], player_mon, opponent_mon)
            Turn(player_mon, opponent_mon)
        # If player is faster
        else:
            if checkAccuracy(player_mon.moves[move_index]) == 1:
                calcDamage(player_mon.moves[move_index], player_mon, opponent_mon)
            opponentTurn(player_mon, opponent_mon)
            playerHealthCheck(player_mon, opponent_mon)
            Turn(player_mon, opponent_mon)

    if battle_choice == "2":
        Turn(opponentTurn(playerSwitch(player_mon), player_mon), opponent_mon)


def main():
    print("Welcome to Pokemon!")
    initializeGame()
    player_mon, opponent_mon = startBattle()
    Turn(player_mon, opponent_mon)


main()
