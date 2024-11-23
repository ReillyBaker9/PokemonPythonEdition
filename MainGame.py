from Classes import *
from Pokedex import *
from random import randint
import copy

def initializeGame():
    global Player
    # Player.name = input("What is your name? ")
    Player.name = "Reilly"
    Player.team = []
    Player.x = 0
    Player.y = 0

    # temporarily set team to three starter evos
    Mon1 = copy.copy(Venusaur)
    Mon2 = copy.copy(Charizard)
    Mon3 = copy.copy(Blastoise)
    Player.team.append(Mon1)
    Player.team.append(Mon2)
    Player.team.append(Mon3)

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
    OppMon1 = copy.copy(Venusaur)
    OppMon2 = copy.copy(Pidgey)
    OppMon3 = copy.copy(Caterpie)
    OppMon4 = copy.copy(Charmander)
    opponent = Opponent("Gary", [OppMon1, OppMon2, OppMon3, OppMon4])
    print("You are challenged by " + opponent.name + "!")
    print("Opponent's team: ")
    for i in range(len(opponent.team)):
        print(opponent.team[i].name)
    # global PlayerMon
    PlayerMon = Player.team[0]
    # global OpponentMon
    OpponentMon = opponent.team[0]
    print("Go! " + PlayerMon.name + "!")
    print("Opponent sent out " + OpponentMon.name + "!")
    return PlayerMon, OpponentMon

def Turn(PlayerMon, OpponentMon):
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
            attackingStat = Attacker.spattack
            defendingStat = Defender.spdefense
        else:
            attackingStat = Attacker.attack
            defendingStat = Defender.defense
        levelConst = 42
        baseDamage = ((levelConst * move.power * (attackingStat/defendingStat))/50) + 2
        if move.type in Attacker.type:
            stabMult = 1.5
        else:
            stabMult = 1.0
        randomFactor = (randint(85, 100))/100
        typeMod = checkType(move, Defender)
        damage = int(baseDamage * stabMult * randomFactor * typeMod)
        Defender.hp = int(Defender.hp - damage)
        print("The HP of " + Defender.name + " is now: " + str(Defender.hp))
        return str(damage)

    def checkType(move, Defender):
        typeMod = 1
        for defender_type in Defender.type:
            if defender_type in move.type.strong_against:
                typeMod *= 2
            elif defender_type in move.type.weak_against:
                typeMod *= 0.5
            elif defender_type in move.type.no_effect_against:
                typeMod *= 0
        if typeMod > 1:
            print("It's super effective!")
        elif typeMod < 1:
            print("It's not very effective")
        elif typeMod == 0:
            print("The move had no effect.")
        return typeMod


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

    def playerSwitch(PlayerMon):
        for k in range(len(Player.team)):
            print(str(k + 1) + ". " + Player.team[k].name)
        mon = int(input("Which Pokemon will you switch to? ")) - 1
        if Player.team[mon] == PlayerMon:
            print("Can't switch to the Pokemon already out!")
            return playerSwitch(PlayerMon)
        else:
            PlayerMon = Player.team[mon]
            print("Switched to " + PlayerMon.name)
            return PlayerMon
    
    def setStats(Attacker, Defender, operation):
        return
    
    def opponentTurn(PlayerMon):
        move = randint(0, (len(OpponentMon.moves)-1))
        chosenMove = OpponentMon.moves[move]
        if checkAccuracy(chosenMove) == 1:
            print("Opponent's " + OpponentMon.name + " attacked for " + calcDamage(chosenMove, OpponentMon, PlayerMon) + " damage!")
        return PlayerMon
     
    # leave it as 0 for now
    statChange = 0
    if statChange == 1:
        setStats()
    print("What will you do?")
    print("1. Fight")
    print("2. Switch Pokemon")
    print("3. Bag")
    battleChoice = input("Choice: ")
    if battleChoice == "1":
        print("Use which move?")
        for i in range(len(PlayerMon.moves)): 
            print(str(i+1) + ". " + str(PlayerMon.moves[i].name))
        moveIndex = int(input("Select move: ")) - 1
        # If opponent is faster:
        if calcPriority(PlayerMon.moves[moveIndex], PlayerMon.speed, OpponentMon.speed) == 1:
            opponentTurn(PlayerMon)
            if checkAccuracy(PlayerMon.moves[moveIndex]) == 1:
                calcDamage(PlayerMon.moves[moveIndex], PlayerMon, OpponentMon)
            Turn(PlayerMon, OpponentMon)
        # If player is faster
        else:
            if checkAccuracy(PlayerMon.moves[moveIndex]) == 1:
                calcDamage(PlayerMon.moves[moveIndex], PlayerMon, OpponentMon)
            opponentTurn(PlayerMon)
            Turn(PlayerMon, OpponentMon)
        

    if battleChoice == "2":
        Turn(opponentTurn(playerSwitch(PlayerMon)), OpponentMon)

def main():
    print("Welcome to Pokemon!")
    initializeGame()
    PlayerMon, OpponentMon = startBattle()
    Turn(PlayerMon, OpponentMon)

main()