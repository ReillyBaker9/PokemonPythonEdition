# from Pokedex import *
from APIConnect import get_pokemon_data, Pokemon
from Classes import *
import copy


def debugInit(opponent):
    # global pokeList
    Player.team = []
    pokeList = [get_pokemon_data(3), get_pokemon_data(6), get_pokemon_data(9)]
    for guy in pokeList:
        team_member = copy.copy(guy)
        # reset health and stat values in case player is restarting
        team_member.reset_health()
        Player.team.append(team_member)
    oppList = [get_pokemon_data(900), get_pokemon_data(1000), get_pokemon_data(100)]
    for each in oppList:
        opponent.team.append(copy.copy(each))
    Player.current_pokemon = Player.team[0]
    opponent.current_pokemon = opponent.team[0]
