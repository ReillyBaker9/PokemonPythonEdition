from Classes import *
from Pokedex import *
from random import randint
from OpponentAI import *
from Types import *
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
    # opp_mon3 = copy.deepcopy(Caterpie)
    # opp_mon4 = copy.deepcopy(Charmander)
    global opponent 
    opponent = Opponent("Gary", [opp_mon1, opp_mon2])
    # opponent = Opponent("Gary", [opp_mon1, opp_mon2, opp_mon3, opp_mon4])
    print("You are challenged by " + opponent.name + "!")
    print("Opponent's team: ")
    for i in range(len(opponent.team)):
        print(opponent.team[i].name)
    player_mon = Player.team[0]
    opponent_mon = opponent.team[0]
    print("Go! " + player_mon.name + "!")
    print("Opponent sent out " + opponent_mon.name + "!")
    return player_mon, opponent_mon


def calcPriority(mySpeed, oppSpeed):
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
            attacking_stat = Attacker.battleSpattack
            defending_stat = Defender.battleSpdefense
        else:
            attacking_stat = Attacker.battleAttack
            defending_stat = Defender.battleDefense
        level_const = 42
        base_damage = ((level_const * move.power * (attacking_stat / defending_stat)) / 50) + 2
        if move.type in Attacker.type:
            stab_mult = 1.5
        else:
            stab_mult = 1.0
        random_factor = (randint(85, 100)) / 100
        type_mult = 1.0
        for defender_type in Defender.type:
            if defender_type in type_effectiveness.get(move.type, {}):
                type_mult *= type_effectiveness[move.type][defender_type]
        # Print effectiveness message
        if type_mult > 1:
            print("It's super effective!")
        elif type_mult < 1:
            print("It's not very effective...")
         
        damage = int(base_damage * stab_mult * random_factor * type_mult)
        Defender.hp = int(Defender.hp - damage)
        print("The HP of " + Defender.name + " is now: " + str(Defender.hp))
        return str(damage)


def checkAccuracy(move, player_mon, opponent_mon, user):
        check = randint(1, 100)
        if check > move.accuracy:
            print(move.name + " missed!")
            return
        else:
            if move.moveType == "Status":
                changeStats(move, player_mon, opponent_mon, user)
                return
            else:
                return 1

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
        attackMult, defenseMult, spattackMult, spdefenseMult, speedMult = 0
        return player_mon

def changeStats(move, player_mon, opponent_mon, user):
    global attackMult, defenseMult, spattackMult, spdefenseMult, speedMult
    global oppAttackMult, oppDefenseMult, oppSpattackMult, oppSpdefenseMult, oppSpeedMult
    if (user == 1 and move.target == "Opponent") or (user == 0 and move.target == "Self"):
        stat = move.stat
        match stat:
            case "Attack":
                attackMult = attackMult + move.modifier
                print(f"{Player.name}'s {player_mon.name}'s {stat} is now at stage: {attackMult}")
            case "Defense":
                defenseMult = defenseMult + move.modifier
                print(f"{Player.name}'s {player_mon.name}'s {stat} is now at stage: {defenseMult}")
            case "Spattack":
                spattackMult = spattackMult + move.modifier
                print(f"{Player.name}'s {player_mon.name}'s {stat} is now at stage: {spattackMult}")
            case "Spdefense":
                spdefenseMult = spdefenseMult + move.modifier
                print(f"{Player.name}'s {player_mon.name}'s {stat} is now at stage: {spdefenseMult}")
            case "Speed":
                speedMult = speedMult + move.modifier
                print(f"{Player.name}'s {player_mon.name}'s {stat} is now at stage: {speedMult}")
    else:
        stat = move.stat
        match stat:
            case "Attack":
                oppAttackMult = oppAttackMult + move.modifier
                print(f"{opponent.name}'s {opponent_mon.name}'s {stat} is now at stage: {oppAttackMult}")
            case "Defense":
                oppDefenseMult = oppDefenseMult + move.modifier
                print(f"{opponent.name}'s {opponent_mon.name}'s {stat} is now at stage: {oppDefenseMult}")
            case "Spattack":
                oppSpattackMult = oppSpattackMult + move.modifier
                print(f"{opponent.name}'s {opponent_mon.name}'s {stat} is now at stage: {oppSpattackMult}")
            case "Spdefense":
                oppSpdefenseMult = oppSpdefenseMult + move.modifier
                print(f"{opponent.name}'s {opponent_mon.name}'s {stat} is now at stage: {oppSpdefenseMult}")
            case "Speed":
                oppSpeedMult = oppSpeedMult + move.modifier
                print(f"{opponent.name}'s {opponent_mon.name}'s {stat} is now at stage: {oppSpeedMult}")
    return

def setStats(player_mon, opponent_mon):
    global attackMult, defenseMult, spattackMult, spdefenseMult, speedMult
    global oppAttackMult, oppDefenseMult, oppSpattackMult, oppSpdefenseMult, oppSpeedMult
    mults = [attackMult, defenseMult, spattackMult, spdefenseMult, speedMult,
             oppAttackMult, oppDefenseMult, oppSpattackMult, oppSpdefenseMult, oppSpeedMult]
    for i in range(len(mults)):
        if mults[i] > 6:
            mults[i] = 6
        elif mults[i] < -6:
            mults[i] = -6
    attackMult, defenseMult, spattackMult, spdefenseMult, speedMult = mults[:5]
    oppAttackMult, oppDefenseMult, oppSpattackMult, oppSpdefenseMult, oppSpeedMult = mults[5:]
    player_mon.battleAttack = player_mon.attack * stat_multipliers[attackMult]
    player_mon.battleDefense = player_mon.defense * stat_multipliers[defenseMult]
    player_mon.battleSpattack = player_mon.spattack * stat_multipliers[spattackMult]
    player_mon.battleSpdefense = player_mon.spdefense * stat_multipliers[spdefenseMult]
    player_mon.battleSpeed = player_mon.speed * stat_multipliers[speedMult]
    
    opponent_mon.battleAttack = opponent_mon.attack * stat_multipliers[oppAttackMult]
    opponent_mon.battleDefense = opponent_mon.defense * stat_multipliers[oppDefenseMult]
    opponent_mon.battleSpattack = opponent_mon.spattack * stat_multipliers[oppSpattackMult]
    opponent_mon.battleSpdefense = opponent_mon.spdefense * stat_multipliers[oppSpdefenseMult]
    opponent_mon.battleSpeed = opponent_mon.speed * stat_multipliers[oppSpeedMult]
    return

def playerHealthCheck(player_mon, opponent_mon):
    if player_mon.hp <= 0:
        print(Player.name + "'s " + player_mon.name + " fainted!")
        Turn(playerSwitch(player_mon), opponent_mon)
        return

def opponentTurn(player_mon, opponent_mon):
        move = randint(0, (len(opponent_mon.moves) - 1))
        chosen_move = opponent_mon.moves[move]
        if checkAccuracy(chosen_move, player_mon, opponent_mon, 1) == 1:
            print("Opponent's " + opponent_mon.name + " attacked for " + calcDamage(chosen_move, opponent_mon,
                                                                                    player_mon) + " damage!")
        return player_mon
    
       
def Turn(player_mon, opponent_mon):
    global attackMult, defenseMult, spattackMult, spdefenseMult, speedMult
    global oppAttackMult, oppDefenseMult, oppSpattackMult, oppSpdefenseMult, oppSpeedMult
    while player_mon.hp > 0 and opponent_mon.hp > 0:
        setStats(player_mon, opponent_mon)
        print("What will you do?")
        print("1. Fight")
        print("2. Switch Pokemon")
        print("3. Bag")
        acceptable_inputs = ["1", "2", "3"]
        battle_choice = input("Choice: ")
        while battle_choice not in acceptable_inputs:
            print("Invalid selection.")
            battle_choice = input("Choice: ")
        if battle_choice == "2":
            Turn(opponentTurn(playerSwitch(player_mon), player_mon), opponent_mon)
            
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
            if calcPriority(player_mon.battleSpeed, opponent_mon.battleSpeed) == 1:
                opponentTurn(player_mon, opponent_mon)
                playerHealthCheck(player_mon, opponent_mon)
                if checkAccuracy(player_mon.moves[move_index], player_mon, opponent_mon, 0) == 1:
                    calcDamage(player_mon.moves[move_index], player_mon, opponent_mon)
                if opponent_mon.hp <= 0:
                    opponent_mon = switch_on_faint(opponent)
                    oppAttackMult, oppDefenseMult, oppSpattackMult, oppSpdefenseMult, oppSpeedMult = 0
                    if opponent_mon is None:
                        # define end battle
                        print("Battle should be over")
                        return
                
            # If player is faster
            else:
                if checkAccuracy(player_mon.moves[move_index], player_mon, opponent_mon, 0) == 1:
                    calcDamage(player_mon.moves[move_index], player_mon, opponent_mon)
                if opponent_mon.hp <= 0:
                    opponent_mon = switch_on_faint(opponent)
                    if opponent_mon is None:
                        # define end battle
                        print("Battle should be over")
                        return
                    else:
                        continue  # Move to the next iteration of the loop if opponent switches Pokemon
                    
                opponentTurn(player_mon, opponent_mon)
                playerHealthCheck(player_mon, opponent_mon)
    print("Battle ended.")
        


def main():
    print("Welcome to Pokemon!")
    initializeGame()
    player_mon, opponent_mon = startBattle()
    Turn(player_mon, opponent_mon)


main()
