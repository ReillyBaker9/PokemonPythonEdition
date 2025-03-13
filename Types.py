from Classes import Types

# defining all the types and giving them names
# had copilot go down the list after the first few
Fire = Types("Fire")
Grass = Types("Grass")
Water = Types("Water")
Normal = Types("Normal")
Bug = Types("Bug")
Flying = Types("Flying")
Poison = Types("Poison")
Electric = Types("Electric")
Ground = Types("Ground")
Fighting = Types("Fighting")
Psychic = Types("Psychic")
Rock = Types("Rock")
Ghost = Types("Ghost")
Ice = Types("Ice")
Dragon = Types("Dragon")
Steel = Types("Steel")
Fairy = Types("Fairy")
Dark = Types("Dark")

type_mapping = {
    "fire": Fire,
    "grass": Grass,
    "water": Water,
    "normal": Normal,
    "bug": Bug,
    "flying": Flying,
    "poison": Poison,
    "electric": Electric,
    "ground": Ground,
    "fighting": Fighting,
    "psychic": Psychic,
    "rock": Rock,
    "ghost": Ghost,
    "ice": Ice,
    "dragon": Dragon,
    "steel": Steel,
    "fairy": Fairy,
    "dark": Dark,
}

# defining all the type multipliers for damage calculations
# generation courtesy of Copilot
type_effectiveness = {
    Normal: {Rock: 0.5, Ghost: 0, Steel: 0.5},
    Fire: {Fire: 0.5, Water: 0.5, Grass: 2, Ice: 2, Bug: 2, Rock: 0.5, Dragon: 0.5, Steel: 2},
    Water: {Fire: 2, Water: 0.5, Grass: 0.5, Ground: 2, Rock: 2, Dragon: 0.5},
    Electric: {Water: 2, Electric: 0.5, Grass: 0.5, Ground: 0, Flying: 2, Dragon: 0.5},
    Grass: {Fire: 0.5, Water: 2, Grass: 0.5, Poison: 0.5, Ground: 2, Flying: 0.5, Bug: 0.5, Rock: 2, Dragon: 0.5,
            Steel: 0.5},
    Ice: {Fire: 0.5, Water: 0.5, Grass: 2, Ice: 0.5, Ground: 2, Flying: 2, Dragon: 2, Steel: 0.5},
    Fighting: {Normal: 2, Ice: 2, Poison: 0.5, Flying: 0.5, Psychic: 0.5, Bug: 0.5, Rock: 2, Ghost: 0, Dark: 2,
               Steel: 2, Fairy: 0.5},
    Poison: {Grass: 2, Poison: 0.5, Ground: 0.5, Rock: 0.5, Ghost: 0.5, Steel: 0, Fairy: 2},
    Ground: {Fire: 2, Electric: 2, Grass: 0.5, Poison: 2, Flying: 0, Bug: 0.5, Rock: 2, Steel: 2},
    Flying: {Electric: 0.5, Grass: 2, Fighting: 2, Bug: 2, Rock: 0.5, Steel: 0.5},
    Psychic: {Fighting: 2, Poison: 2, Psychic: 0.5, Dark: 0, Steel: 0.5},
    Bug: {Fire: 0.5, Grass: 2, Fighting: 0.5, Poison: 0.5, Flying: 0.5, Psychic: 2, Ghost: 0.5, Dark: 2, Steel: 0.5,
          Fairy: 0.5},
    Rock: {Fire: 2, Ice: 2, Fighting: 0.5, Ground: 0.5, Flying: 2, Bug: 2, Steel: 0.5},
    Ghost: {Normal: 0, Psychic: 2, Ghost: 2, Dark: 0.5},
    Dragon: {Dragon: 2, Steel: 0.5, Fairy: 0},
    Dark: {Fighting: 0.5, Psychic: 2, Ghost: 2, Dark: 0.5, Fairy: 0.5},
    Steel: {Fire: 0.5, Water: 0.5, Electric: 0.5, Ice: 2, Rock: 2, Steel: 0.5, Fairy: 2},
    Fairy: {Fire: 0.5, Fighting: 2, Poison: 0.5, Dragon: 2, Dark: 2, Steel: 0.5},
}
