class Pokemon:
    def __init__(self, name, pokedex, type, hp, attack, defense, spattack, spdefense, speed, moves):
        self.name = name
        self.pokedex = pokedex
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spattack = spattack
        self.spdefense = spdefense
        self.speed = speed
        self.moves = moves

class Moves:
    def __init__(self, name, type, power, accuracy):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy

class Types:
    def __init__(self, name, strong_against=None, weak_against=None, no_effect_against=None):
        self.name = name
        self.strong_against = strong_against if strong_against is not None else []
        self.weak_against = weak_against if weak_against is not None else []
        self.no_effect_against = no_effect_against if no_effect_against is not None else []

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