from Classes import *
from Moves import *
from Types import *

Bulbasaur = Pokemon("Bulbasaur", 1, [Grass, Poison], 45, 49, 49, 65, 65, 45, [tackle, vine_whip, razor_leaf, solar_beam])
Ivysaur = Pokemon("Ivysaur", 2, [Grass, Poison], 60, 62, 63, 80, 80, 60, [tackle, vine_whip, razor_leaf, solar_beam])
Venusaur = Pokemon("Venusaur", 3, [Grass, Poison], 80, 82, 83, 100, 100, 80, [tackle, vine_whip, razor_leaf, solar_beam])
Charmander = Pokemon("Charmander", 4, Fire, 39, 52, 43, 60, 50, 65, [scratch, ember, fire_fang, flamethrower])
Charmeleon = Pokemon("Charmeleon", 5, Fire, 58, 64, 58, 80, 65, 80, [scratch, ember, fire_fang, flamethrower])
Charizard = Pokemon("Charizard", 6, [Fire, Flying], 78, 84, 78, 109, 85, 100, [scratch, ember, fire_fang, flamethrower])
Squirtle = Pokemon("Squirtle", 7, Water, 44, 48, 65, 50, 64, 43, [tackle, water_gun, hydro_pump, surf])
Wartortle = Pokemon("Wartortle", 8, Water, 59, 63, 80, 65, 80, 58, [tackle, water_gun, hydro_pump, surf])
Blastoise = Pokemon("Blastoise", 9, Water, 79, 83, 100, 85, 105, 78, [tackle, water_gun, hydro_pump, surf])
Caterpie = Pokemon("Caterpie", 10, Bug, 45, 30, 35, 20, 20, 45, [tackle])
Metapod = Pokemon("Metapod", 11, Bug, 50, 20, 55, 25, 25, 30, [harden])
Butterfree = Pokemon("Butterfree", 12, [Bug, Flying], 60, 45, 50, 90, 80, 70, [tackle, gust, quick_attack, wing_attack])
Weedle = Pokemon("Weedle", 13, [Bug, Poison], 40, 35, 30, 20, 20, 50, [poison_sting])
Kakuna = Pokemon("Kakuna", 14, [Bug, Poison], 45, 25, 50, 25, 25, 35, [harden])
Beedrill = Pokemon("Beedrill", 15, [Bug, Poison], 65, 90, 40, 45, 80, 75, [tackle, poison_sting, fury_attack, pin_missile])
Pidgey = Pokemon("Pidgey", 16, [Normal, Flying], 40, 45, 40, 35, 35, 56, [tackle, gust, quick_attack, wing_attack])
Pidgeotto = Pokemon("Pidgeotto", 17, [Normal, Flying], 63, 60, 55, 50, 50, 71, [tackle, gust, quick_attack, wing_attack])
Pidgeot = Pokemon("Pidgeot", 18, [Normal, Flying], 83, 80, 75, 70, 70, 91, [tackle, gust, quick_attack, wing_attack])
Rattata = Pokemon("Rattata", 19, Normal, 30, 56, 35, 25, 35, 72, [tackle, quick_attack])
Raticate = Pokemon("Raticate", 20, Normal, 55, 81, 60, 50, 70, 97, [tackle, quick_attack, hyper_fang])

Pokedex = [Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise, Caterpie, Metapod, Butterfree, Weedle, Kakuna, Beedrill, Pidgey, Pidgeotto, Pidgeot, Rattata, Raticate]