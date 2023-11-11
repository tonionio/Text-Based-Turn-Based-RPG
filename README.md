# MyPyGame

Choose a character (Warrior, Ranger, Wizard) and location (Mountains, Desert, Forest) in this text-based adventure game. Engage in turn-based encounters to defeat enemies, aiming to conquer a set number of foes. Win by defeating all enemies, or lose when your character's health reaches zero. Restart or quit at any time.

Running the game For Python users If you have Python installed, you can run the game by executing the player_start.py file in the root directory:
bash Copy code "python player_start2.py"

For non-Python users If you do not have Python installed, you can still play the game by downloading and running the standalone executable. Here's how:
Download the player_start2 executable from the dist directory.
Run the player_start2 executable to start the game.

High-level overview for a new user/player: This is a text-based adventure game where you choose a character class (Warrior, Ranger, or Wizard) and then select a location (Mountains, Desert, or Forest) to battle various enemies. The game consists of a series of encounters where you can either attack or block to defeat your opponents. The game continues until you have defeated a set number of enemies, at which point you win, or your character's health reaches zero, at which point you lose. You can restart the game if you are defeated or quit at any time.

Low-level overview for a software developer: The game is structured into multiple Python modules, each focusing on specific aspects of the game:
- character_classes.py: This module contains the base Character class and three subclasses for each character class (Warrior, Ranger, and
 Wizard). Each class has attributes such as health, stamina, and actions, as well as methods for attacking and blocking.

- enemy_classes.py: This module contains the base Enemy class and three subclasses for each enemy type (Yeti, Mothman, and Sandman). Each class has attributes such as health, stamina, and actions, as well as methods for attacking.

- game_status.py: This module contains the GameStatus class, which is responsible for managing the game state and controlling the game flow. It contains methods for starting the game, choosing a character and location, running the main game loop (with encounter and combat logic), handling player defeat and victory, and resetting the game state.

- level_classes.py: This module contains the base Level class and three subclasses for each location (Mountains, Desert, and Forest). Each class has a name and description.

- loadnsave.py: This module contains the GameState class for saving, loading, and resetting the game state using JSON serialization.

- main_drivers.py: This module is currently empty but can be used to add additional game drivers if needed.

- player_start2.py: This is the entry point of the game, where the GameStatus class is instantiated, and the game is started.

The game uses object-oriented programming principles with inheritance for the character and enemy classes. It utilizes a while loop for the main game loop and employs conditional statements for handling user input and game logic. Randomness is introduced through the random module for hit chances and enemy generation.

I'm deeply grateful for your interest in this initial venture of mine. It's truly encouraging to see you've journeyed this far into the project. My vision for this game extends beyond a solo endeavor, envisioning a vibrant community enriching it with creative ideas and diverse perspectives. Your thoughts, suggestions, and innovative insights are not just welcome, but eagerly anticipated. Whether it's a unique twist in the narrative, a compelling game mechanic, or any other enhancement that could augment the gameplay, I invite you to contribute and help shape this project. Looking forward to exploring this text adventure together.
