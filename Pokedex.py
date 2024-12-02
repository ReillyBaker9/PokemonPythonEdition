from Classes import *
from Moves import *
from Types import *

Bulbasaur = Pokemon("Bulbasaur", 1, [Grass, Poison], 294, 197, 197, 240, 240, 197, [tackle, vine_whip, razor_leaf, solar_beam])
Ivysaur = Pokemon("Ivysaur", 2, [Grass, Poison], 364, 236, 236, 284, 284, 236, [tackle, vine_whip, razor_leaf, solar_beam])
Venusaur = Pokemon("Venusaur", 3, [Grass, Poison], 364, 236, 236, 284, 284, 236, [tackle, vine_whip, razor_leaf, solar_beam])
Charmander = Pokemon("Charmander", 4, [Fire], 282, 203, 178, 240, 218, 251, [scratch, ember, fire_fang, flamethrower])
Charmeleon = Pokemon("Charmeleon", 5, [Fire], 320, 223, 202, 284, 240, 284, [scratch, ember, fire_fang, flamethrower])
# Charizard = Pokemon("Charizard", 6, [Fire, Flying], 360, 267, 236, 328, 251, 328, [scratch, ember, fire_fang, flamethrower])
# Giving Charizard Nasty Plot to check stat changes
Charizard = Pokemon("Charizard", 6, [Fire, Flying], 360, 267, 236, 328, 251, 328, [scratch, nasty_plot, fire_fang, flamethrower])
Squirtle = Pokemon("Squirtle", 7, [Water], 292, 197, 251, 218, 251, 197, [tackle, water_gun, hydro_pump, surf])
Wartortle = Pokemon("Wartortle", 8, [Water], 324, 223, 284, 240, 284, 223, [tackle, water_gun, hydro_pump, surf])
# temporarily changing types for checking effectiveness to add 4x weakness to water
Blastoise = Pokemon("Blastoise", 9, [Water], 362, 267, 328, 284, 328, 267, [tackle, water_gun, hydro_pump, surf])
Caterpie = Pokemon("Caterpie", 10, [Bug], 294, 157, 178, 140, 140, 197, [tackle])
Metapod = Pokemon("Metapod", 11, [Bug], 304, 140, 229, 162, 162, 162, [harden])
Butterfree = Pokemon("Butterfree", 12, [Bug, Flying], 324, 178, 202, 306, 284, 251, [tackle, gust, quick_attack, wing_attack])
Weedle = Pokemon("Weedle", 13, [Bug, Poison], 284, 157, 178, 140, 140, 229, [poison_sting])
Kakuna = Pokemon("Kakuna", 14, [Bug, Poison], 294, 140, 229, 162, 162, 162, [harden])
Beedrill = Pokemon("Beedrill", 15, [Bug, Poison], 324, 284, 178, 196, 284, 251, [tackle, poison_sting, fury_attack, pin_missile])
Pidgey = Pokemon("Pidgey", 16, [Normal, Flying], 284, 178, 178, 162, 162, 262, [tackle, gust, quick_attack, wing_attack])
Pidgeotto = Pokemon("Pidgeotto", 17, [Normal, Flying], 344, 202, 202, 196, 196, 284, [tackle, gust, quick_attack, wing_attack])
Pidgeot = Pokemon("Pidgeot", 18, [Normal, Flying], 384, 240, 229, 240, 240, 328, [tackle, gust, quick_attack, wing_attack])
Rattata = Pokemon("Rattata", 19, [Normal], 244, 229, 178, 162, 178, 306, [tackle, quick_attack])
Raticate = Pokemon("Raticate", 20, [Normal], 314, 284, 229, 196, 262, 328, [tackle, quick_attack, hyper_fang])

Pokedex = [Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise, Caterpie, Metapod, Butterfree, Weedle, Kakuna, Beedrill, Pidgey, Pidgeotto, Pidgeot, Rattata, Raticate]