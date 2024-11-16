class Pokemon:
    def __init__(self, name, type, hp, attack, defense, spattack, spdefense, speed, moves):
        self.name = name
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