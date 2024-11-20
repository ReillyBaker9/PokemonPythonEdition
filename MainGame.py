from Classes import *
from Pokedex import *
from random import randint

def initializeGame():
    global Player
    # Player.name = input("What is your name? ")
    Player.name = "Reilly"
    Player.team = []
    Player.x = 0
    Player.y = 0

    # temporarily set team to three starter evos
    Player.team.append(Pokedex[2])
    Player.team.append(Pokedex[5])
    Player.team.append(Pokedex[8])

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
    opponent = Opponent("Gary", [Venusaur, Pidgey, Caterpie, Charmander])
    print("You are challenged by " + opponent.name + "!")
    print("Opponent's team: ")
    for i in range(len(opponent.team)):
        print(opponent.team[i].name)
    # global PlayerMon
    PlayerMon = Player.team[0]
    tempHP = PlayerMon.hp
    tempAtk = PlayerMon.attack
    tempDefense = PlayerMon.defense
    tempSpAtk = PlayerMon.spattack
    tempSpDef = PlayerMon.spdefense
    tempSpeed = PlayerMon.speed
    # global OpponentMon
    OpponentMon = opponent.team[0]
    oppHP = OpponentMon.hp
    oppAtk = OpponentMon.attack
    oppDefense = OpponentMon.defense
    oppSpAtk = OpponentMon.spattack
    oppSpDef = OpponentMon.spdefense
    oppSpeed = OpponentMon.speed
    print("Go! " + PlayerMon.name + "!")
    print("Opponent sent out " + OpponentMon.name + "!")
    playerTurn(PlayerMon, OpponentMon)

def playerTurn(PlayerMon, OpponentMon):
    def calcPriority(move, tempSpeed, oppSpeed):
        speedTie = randint(1, 2)
        if tempSpeed < oppSpeed:
            return 1
        if tempSpeed == oppSpeed:
            if speedTie == 1:
                return 1
            else:
                return 2
        else:
            return 2

    def calcDamage(move, Attacker, Defender):
        # comes from damage calc page, stays same for level 100
        print("The defender's hp is: " + str(Defender.hp))
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
        damage = baseDamage * stabMult * randomFactor * typeMod
        Defender.hp = int(Defender.hp - damage)
        print("The defender's new HP is: " + str(Defender.hp))
        return

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
                calcDamage(move, PlayerMon, OpponentMon)

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
        print("Opponent's " + OpponentMon.name + " attacked for 10 damage!")
        PlayerMon.hp = PlayerMon.hp - 10
        print("Your " + PlayerMon.name + " is now at " + str(PlayerMon.hp) + " hp!")
        return PlayerMon
    
    # leave it as 0 for now
    statChange = 0
    if statChange == 1:
        setStats()
    else:
        tempHP = PlayerMon.hp
        tempAtk = PlayerMon.attack
        tempDefense = PlayerMon.defense
        tempSpAtk = PlayerMon.spattack
        tempSpDef = PlayerMon.spdefense
        tempSpeed = PlayerMon.speed
        oppHP = OpponentMon.hp
        oppAtk = OpponentMon.attack
        oppDefense = OpponentMon.defense
        oppSpAtk = OpponentMon.spattack
        oppSpDef = OpponentMon.spdefense
        oppSpeed = OpponentMon.speed
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
        if calcPriority(PlayerMon.moves[moveIndex], tempSpeed, oppSpeed) == 1:
            opponentTurn(PlayerMon)
            checkAccuracy(PlayerMon.moves[moveIndex])
            playerTurn(PlayerMon, OpponentMon)
        else:
            checkAccuracy(PlayerMon.moves[moveIndex])
            opponentTurn(PlayerMon)
            playerTurn(PlayerMon, OpponentMon)
        

    if battleChoice == "2":
        playerTurn(opponentTurn(playerSwitch(PlayerMon)), OpponentMon)

def main():
    print("Welcome to Pokemon!")
    initializeGame()
    startBattle()

main()