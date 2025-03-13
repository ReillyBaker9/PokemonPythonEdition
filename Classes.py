class Pokemon:
    def __init__(self, name, pokedex, types, pokeStats, moves):
        # battle stats start as the same as base stats and are modified in battle
        self.name = name
        self.pokedex = pokedex
        self.type = types
        self.pokeStats = pokeStats
        self.battleStats = self.pokeStats.copy()
        self.moves = moves


    def reset_health(self):
        self.battleStats = self.pokeStats.copy()


class Moves:
    def __init__(self, name, move_type, accuracy, effect_chance, priority, power, damage_class, target, effect_category,
                 stat_modifier, stat):
        # target, modifier, and stat only have values if move is a status move
        self.name = name
        self.move_type = move_type
        self.accuracy = accuracy
        self.effect_chance = effect_chance
        self.priority = priority
        self.power = power
        self.damage_class = damage_class
        self.target = target
        self.effect_category = effect_category
        self.stat_modifier = stat_modifier
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
        