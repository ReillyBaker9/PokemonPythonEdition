class Pokemon:
    def __init__(self, name, pokedex, types, hp, attack, defense, spattack, spdefense, speed, moves):
        # battle stats start as the same as base stats and are modified in battle
        self.name = name
        self.pokedex = pokedex
        self.type = types
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spattack = spattack
        self.spdefense = spdefense
        self.speed = speed
        self.moves = moves
        self.battleHp = hp
        self.battleAttack = attack
        self.battleDefense = defense
        self.battleSpattack = spattack
        self.battleSpdefense = spdefense
        self.battleSpeed = speed
    
    # suggested by CoPilot as a way to reset 
    # health after restarting the battle
    def reset_health(self):
        self.battleHp = self.hp
        self.battleAttack = self.attack
        self.battleDefense = self.defense
        self.battleSpattack = self.spattack
        self.battleSpdefense = self.spdefense
        self.battleSpeed = self.speed


class Moves:
    def __init__(self, name, type, power, accuracy, moveType, target=None, modifier=None, stat=None):
        # target, modifier, and stat only have values if move is a status move
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.moveType = moveType
        self.target = target
        self.modifier = modifier
        self.stat = stat


class Types:
    def __init__(self, name):
        # Just need a name lol
        self.name = name


class Player:
    def __init__(self, name, team):
        # Starts with None as current pokemon and is assigned at beginning of battle
        self.name = name
        self.team = team
        self.current_pokemon = None
        


class Opponent:
    def __init__(self, name, team):
        # Same as player
        self.name = name
        self.team = team
        self.current_pokemon = None
        