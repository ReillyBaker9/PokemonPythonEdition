class Pokemon:
    def __init__(self, name, pokedex, types, hp, attack, defense, spattack, spdefense, speed, moves):
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


class Moves:
    def __init__(self, name, type, power, accuracy, moveType):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.moveType = moveType


class Types:
    def __init__(self, name):
        self.name = name


class Player:
    def __init__(self, name, team, x, y):
        self.name = name
        self.team = team
        self.x = x
        self.y = y


class Opponent:
    def __init__(self, name, team):
        self.name = name
        self.team = team