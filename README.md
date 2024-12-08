# Pokemon Stadium Python Edition
#### Video Demo:  https://youtu.be/uLQTuiIT3JM
#### Description: 

## Humble Beginnings
Initially, I set out to follow up on a project I had started back when I first started learning Python. It was a Pokemon game where you walked around a grid of X's and would randomly encounter wild Pokemon. It was fun to make, and it was a mess. Like all good projects, my initial ambitions were much loftier than what ended up materializing as my final project.

## What Is It?
My final project is a Pokemon battle simulator, a la Pokemon Showdown, where the user picks a team from a sample of the Pokedex and battles an AI opponent. The user can select moves, switch active Pokemon, and get info on either their or their opponent's currently battling Pokemon. Unlike the main series of games, my game is based solely on battling; there are no wild encounters, nor levelling or any sort of progression. You pick a team, and you battle. I've always been the most fascinated by Pokemon mechanically, and thus my aim was primarily to recreate some of the battle mechanics while learning more about Python along the way.

## Deciding What To Include
Early on, I realized the task I had set out for myself, which had at one point included porting my entire project to PyGame, where I could use sprites and actual input buttons, was far larger than the scope of this project. Plus, I'm excited to continue my CS50 journey into the web design portion of the class, so I'm in a slight rush.

As I mentioned previously, I am most fascinated by Pokemon as an interlocking set of mechanics and interactions. Therefore, the Pokedex I included (courtesy of ChatGPT, once I defined the class) was meant as a placeholder to design the game around. The same goes for moves (also courtesy of ChatGPT), and the type interactions (say it again, courtesy of ChatGPT). I could ask it to write up a list of 100 more Pokemon, with unique moves to boot, but my interest was never in replicating Showdown to a tee. So I set out with a limited roster and built the game around it, that way I could add a whole bunch more Pokemon and moves relatively quickly, once the bedrock was there. Maybe I'll do so after submitting my project.

My game is not balanced, nor are there a wide variety of Pokemon types and moves to choose from. I see it as more of a tech demo, and now that the tech is there, it would be easy to fill in more diverse Pokemon types and moves in a single afternoon.

## Get Into The Tech!
As I quickly discovered, things like Pokemon, types, and moves lend themselves very easily to Object Oriented Programming. Therefore, most all of the "things" in the game are objects. These interact with the functions I defined that stage the battles. The player themselves as well as the opponent are objects with their names and teams being attributes, and the current_pokemon attribute being a quick and easy way to track the active Pokemon. 

I defined several functions for the basic actions of the game, like the opponent making a move, the player switching Pokemon, a Pokemon fainting, etc. Lots of these actions require checks, like a verification of which Pokemon moves first, or if a Pokemon's hp has fallen to zero, which means it will faint. These checks are also their own functions. Once I got the classes and objects down (which took several iterations), it became a fairly simple game of passing objects around, modifying them throughout the battle, and telling them to do things. Thus, the final game and its code are fairly self-explanatory.

I had originally considered making a more complicated AI for the opponent, but decided this too was outside of the scope of the project, hence the unneccesarily separated OpponentAI file with just one function. I used dictionaries to easily store bits of information like type offensive and defensive properties and the stat multipliers associated with different stages of stats being raised and lowering. I also made separate, individual stats for each Pokemon object so that I could modify, say, the speed without encountering oddities when the opponent has the same Pokemon out as the player. Each turn, the stats are re-calculated and applied based on the current multipliers applied to each Pokemon

## File Overview
### Classes.py
Fairly self explanatory, I defined all the classes I used in my project. Not sure if this is typical for programming, but I found it useful
### MainGame.py
You'll never guess, it's the main game loop itself. I debated moving some functions out of this file, but then I discovered that you can shrink a function and fold it up in VSCode and navigating my code became a thousand times easier
### Moves.py
All the move objects for each Pokemon. Plus the stat modifiers. Not really sure why they're in there. Guess I was messing with them at the same time I was making stat-modifying moves.
### OldStuff.py
I like to have a file to save functions I like in case my replacements break and I want to go back to the old stuff
### OpponentAI.py
The ill-fated opponent AI I was at one point contemplating writing. Left as is for posterity
### Pokedex.py
All the Pokemon I used, the first twenty in the Pokedex. Also added them to the array pokedex to easily access them for choosing a team
### README.md
See README.md
### scope.txt
Something for me to keep track of what would and wouldn't be in my project
### Types.py
All the type objects and their effectivenesses against each other stored in a dictionary

## Thanks For Reading!