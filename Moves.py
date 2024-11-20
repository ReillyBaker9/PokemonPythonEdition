from Classes import Moves
from Types import *

ember = Moves("Ember", Fire, 40, 100, "Special")
fire_fang = Moves("Fire Fang", Fire, 65, 95, "Physical")
flamethrower = Moves("Flamethrower", Fire, 90, 100, "Special")
gust = Moves("Gust", Flying, 40, 100, "Special")
quick_attack = Moves("Quick Attack", Normal, 40, 100, "Physical")

# Lowering scratch's accuracy for testing, don't forget to change!
scratch = Moves("Scratch", Normal, 40, 20, "Physical")

tackle = Moves("Tackle", Normal, 40, 100, "Physical")
wing_attack = Moves("Wing Attack", Flying, 60, 100, "Physical")
harden = Moves("Harden", Normal, 0, 100, "Status")
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
