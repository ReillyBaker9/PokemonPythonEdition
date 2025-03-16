from Classes import Pokemon, Moves
from Types import type_mapping
import random
import requests
import json

POKE_LEVEL=100


def get_pokemon_data(pokemon_name):
    if isinstance(pokemon_name, str):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)
    if response.status_code == 200:
        types = []
        moves = []
        pokeStats = {}
        data = response.json()
        pokedex = data["id"]
        pokemon_name = data["name"].capitalize()
        for type in data["types"]:
            types.append(type_mapping[type["type"]["name"].capitalize()])
        for stat in data["stats"]:
            pokeStats[stat["stat"]["name"]] = int(stat["base_stat"])
        # Get all available moves from API
        all_moves = [move_data["move"]["name"] for move_data in data["moves"]]

        # Pick 4 random moves (if there are at least 4)
        selected_moves = random.sample(all_moves, min(4, len(all_moves)))

        # Fetch move details
        for move_name in selected_moves:
            move = get_move_data(move_name)
            if move:  # Ensure move data is valid
                moves.append(move)
                print(f"Added {move.name}")
        EV = 0
        IV = 0
        Nature = 1
        pokeStats['hp'] = (((2 * pokeStats['hp'] + IV + (EV / 4)) * POKE_LEVEL) / 100) + POKE_LEVEL + 10
        pokeStats['attack'] = ((((2 * pokeStats['attack'] + IV + (
                    EV / 4)) * POKE_LEVEL) / 100) + 5) * Nature
        pokeStats['defense'] = ((((2 * pokeStats['defense'] + IV + (
                    EV / 4)) * POKE_LEVEL) / 100) + 5) * Nature
        pokeStats['special-attack'] = ((((2 * pokeStats['special-attack'] + IV + (
                    EV / 4)) * POKE_LEVEL) / 100) + 5) * Nature
        pokeStats['special-defense'] = ((((2 * pokeStats['special-defense'] + IV + (
                    EV / 4)) * POKE_LEVEL) / 100) + 5) * Nature
        pokeStats['speed'] = ((((2 * pokeStats['speed'] + IV + (
                    EV / 4)) * POKE_LEVEL) / 100) + 5) * Nature
        pokemon = Pokemon(pokemon_name, pokedex, types, pokeStats, moves)
        return pokemon
    else:
        return None


def get_move_data(move_name):
    url = f"https://pokeapi.co/api/v2/move/{move_name}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stat_modifier = []
        stat = []
        name = move_name
        move_type = data["type"]["name"].capitalize()
        accuracy = data["accuracy"]
        effect_chance = data["effect_chance"]
        priority = data["priority"]
        if data["power"] is None: power = 0
        else: power = data["power"]
        damage_class = data["damage_class"]["name"]
        target = data["target"]["name"]
        effect_category = data.get("meta", {})
        if effect_category is None:
            effect_category = "Unknown"
        else:
            effect_category = effect_category.get("category", {}).get("name", "Unknown")
        for num in data["stat_changes"]:
            stat_modifier.append(num["change"])
            stat.append(num["stat"]["name"])
        move = Moves(name, move_type, accuracy, effect_chance, priority, power, damage_class, target, effect_category,
                     stat_modifier, stat)
        return move
