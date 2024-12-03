from Classes import Moves
from Types import *

ember = Moves("Ember", Fire, 40, 100, "Special")
fire_fang = Moves("Fire Fang", Fire, 65, 95, "Physical")
flamethrower = Moves("Flamethrower", Fire, 90, 100, "Special")
gust = Moves("Gust", Flying, 40, 100, "Special")
quick_attack = Moves("Quick Attack", Normal, 40, 100, "Physical")

# Lowering scratch's accuracy for testing, don't forget to change!
scratch = Moves("Scratch", Normal, 40, 100, "Physical")

tackle = Moves("Tackle", Normal, 40, 100, "Physical")
wing_attack = Moves("Wing Attack", Flying, 60, 100, "Physical")
harden = Moves("Harden", Normal, 0, 100, "Status", "Self", 1, "Defense")
growl = Moves("Growl", Normal, 0, 100, "Status", "Opponent", -1, "Attack")
nasty_plot = Moves("Nasty Plot", Normal, 0, 100, "Status", "Self", 2, "Spattack")
poison_sting = Moves("Poison Sting", Poison, 15, 100, "Physical")
pin_missile = Moves("Pin Missile", Bug, 25, 95, "Physical")
razor_leaf = Moves("Razor Leaf", Grass, 55, 95, "Physical")
solar_beam = Moves("Solar Beam", Grass, 120, 100, "Special")
surf = Moves("Surf", Water, 90, 100, "Special")
vine_whip = Moves("Vine Whip", Grass, 45, 100, "Physical")
water_gun = Moves("Water Gun", Water, 40, 100, "Special")
hydro_pump = Moves("Hydro Pump", Water, 110, 80, "Special")
fury_attack = Moves("Fury Attack", Normal, 15, 85, "Physical")
hyper_fang = Moves("Hyper Fang", Normal, 80, 90, "Physical")

stat_multipliers = { -6: .25, -5: .286, -4: .333, -3: .4, -2: .5, -1: .667,
                    0: 1, 1: 1.5, 2: 2, 3: 2.5, 4: 3, 5: 3.5, 6: 4}

global attackMult
global defenseMult
global spattackMult
global spdefenseMult
global speedMult
global oppAttackMult
global oppDefenseMult
global oppSpattackMult
global oppSpdefenseMult
global oppSpeedMult

attackMult = 0
defenseMult = 0
spattackMult = 0
spdefenseMult = 0
speedMult = 0
oppAttackMult = 0
oppDefenseMult = 0
oppSpattackMult = 0
oppSpdefenseMult = 0
oppSpeedMult = 0