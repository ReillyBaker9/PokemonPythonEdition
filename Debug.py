from Pokedex import *
from Classes import *
import copy


def debugInit(opponent):
    # global pokeList
    Player.team = []
    pokeList = [Pokedex[2], Pokedex[5], Pokedex[8]]
    for guy in pokeList:
        team_member = copy.copy(guy)
        # reset health and stat values in case player is restarting
        team_member.reset_health()
        Player.team.append(team_member)
    oppList = [Venusaur, Pidgeot, Beedrill]
    for each in oppList:
        opponent.team.append(copy.copy(each))
    Player.current_pokemon = Player.team[0]
    opponent.current_pokemon = opponent.team[0]
