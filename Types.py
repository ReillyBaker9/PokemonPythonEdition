from Classes import Types

Fire = Types("Fire", [], [], [])
Grass = Types("Grass", [], [], [])
Water = Types("Water", [], [], [])
Normal = Types("Normal", [], [], [])
Bug = Types("Bug", [], [], [])
Flying = Types("Flying", [], [], [])
Poison = Types("Poison", [], [], [])
Electric = Types("Electric", [], [], [])
Ground = Types("Ground", [], [], [])
Fighting = Types("Fighting", [], [], [])
Psychic = Types("Psychic", [], [], [])
Rock = Types("Rock", [], [], [])
Ghost = Types("Ghost", [], [], [])
Ice = Types("Ice", [], [], [])
Dragon = Types("Dragon", [], [], [])
Steel = Types("Steel", [], [], [])
Fairy = Types("Fairy", [], [], [])
Dark = Types("Dark", [], [], [])

Fire.strong_against = [Grass, Bug, Ice, Steel]
Fire.weak_against = [Fire, Water, Rock, Dragon]
Grass.strong_against = [Water, Ground, Rock]
Grass.weak_against = [Fire, Grass, Poison, Flying, Bug, Dragon, Steel]
Water.strong_against = [Fire, Ground, Rock]
Water.weak_against = [Water, Grass, Dragon]
Normal.weak_against = [Rock, Steel]
Normal.no_effect_against = [Ghost]
Bug.strong_against = [Grass, Psychic, Dark]
Bug.weak_against = [Fire, Fighting, Poison, Flying, Ghost, Steel, Fairy]
Flying.strong_against = [Grass, Fighting, Bug]
Flying.weak_against = [Electric, Rock, Steel]
Poison.strong_against = [Grass, Fairy]
Poison.weak_against = [Poison, Ground, Rock, Ghost]
Poison.no_effect_against = [Steel]
Electric.strong_against = [Water, Flying]
Electric.weak_against = [Electric, Ground, Dragon]
Electric.no_effect_against = [Ground]
Ground.strong_against = [Fire, Electric, Poison, Rock, Steel]
Ground.weak_against = [Grass, Ice, Water]
Ground.no_effect_against = [Flying]
Fighting.strong_against = [Normal, Ice, Rock, Dark, Steel]
Fighting.weak_against = [Poison, Flying, Psychic, Bug, Fairy]
Fighting.no_effect_against = [Ghost]
Psychic.strong_against = [Fighting, Poison]
Psychic.weak_against = [Psychic, Steel]
Psychic.no_effect_against = [Dark]
Rock.strong_against = [Fire, Ice, Flying, Bug]
Rock.weak_against = [Fighting, Ground, Steel]
Ghost.strong_against = [Psychic, Ghost]
Ghost.weak_against = [Dark]
Ghost.no_effect_against = [Normal]
Ice.strong_against = [Grass, Ground, Flying, Dragon]
Ice.weak_against = [Fire, Water, Ice, Steel]
Dragon.strong_against = [Dragon]
Dragon.weak_against = [Steel]
Steel.strong_against = [Ice, Rock, Fairy]
Steel.weak_against = [Fire, Water, Electric, Steel]
Fairy.strong_against = [Fighting, Dragon, Dark]
Fairy.weak_against = [Poison, Steel]
Dark.strong_against = [Psychic, Ghost]
Dark.weak_against = [Fighting, Dark, Fairy]