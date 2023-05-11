import random
from enemy_classes import Yeti, Sandman, Mothman
from character_classes import Warrior, Ranger, Wizard
from loadnsave import GameState
import sys


class GameStatus:
    def __init__(self):
        self.game_state = GameState()
        self.player = None
        self.defeated_enemies = 0
        self.current_location = None

    def start(self):
        loaded_game_data = self.greet_player(wait_for_input=True)
        if loaded_game_data:
            self.load_saved_game(loaded_game_data)
        else:
            self.choose_character()
            self.choose_location()
        self.game_loop()

    def greet_player(self, wait_for_input=True):
        print()
        print("Welcome to the game!")
        print()
        if wait_for_input:
            choice = input(
                "Press 'L' to load a saved game or 'N' to start a new game: ").upper()
            if choice == 'L':
                return self.game_state.load_game()
            elif choice == 'N':
                pass
            else:
                print("Invalid choice, please try again.")
                return self.greet_player()
            input("Press 'Enter' to continue...")

    def choose_character(self):
        while True:
            print("Choose your character:")
            print("1. Warrior\n2. Ranger\n3. Wizard")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                self.player = Warrior()
            elif choice == "2":
                self.player = Ranger()
            elif choice == "3":
                self.player = Wizard()
            else:
                print("Invalid choice, please try again.")
                continue

            print(f"You've chosen: {self.player}")
            confirm = input("Confirm your choice? (y/n): ")
            if confirm.lower() == "y":
                break

    def choose_location(self):
        while True:
            print("Choose a location:")
            print("1. Mountains\n2. Desert\n3. Forest")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                self.current_location = "mountains"
            elif choice == "2":
                self.current_location = "desert"
            elif choice == "3":
                self.current_location = "forest"
            else:
                print("Invalid choice, please try again.")
                continue

            print(f"You've chosen: {self.current_location}")
            confirm = input("Confirm your choice? (y/n): ")
            if confirm.lower() == "y":
                break

    def game_loop(self):
        # Set the number of enemies the player needs to defeat to win the game
        max_enemies_to_defeat = 3

        while True:  # Keep the game loop running until an exit condition is met
            if self.defeated_enemies < max_enemies_to_defeat:
                self.encounter()
            else:
                self.player_win()
                break

            if self.player.health <= 0:  # Check if the player is defeated after each encounter
                self.player_defeated()
                break

    def encounter(self):
        # Enemy encounter
        enemy = self._generate_enemy()
        print()
        print(f"An enemy {enemy.__class__.__name__} appeared!")
        print("------------------------------")

        # Run the combat sequence
        while self.player.health > 0 and enemy.health > 0:
            # Player's turn
            print(f"Your health: {self.player.health}")
            print(f"Enemy {enemy.__class__.__name__} health: {enemy.health}")
            print("------------------------------")
            print("Choose your action:")
            print(f"A) Attack (Inflict {self.player.attack_damage} damage)")
            print(f"B) Block (Reduce incoming damage by 75%)")
            print(f"C) Quit game")
            player_action = input("Enter the letter of your choice: ").upper()

            if player_action == "A":
                player_damage = self.player.attack(enemy)
                if player_damage > 0:
                    print(
                        f"\nYour attack was successful! You dealt {player_damage} damage to the {enemy.__class__.__name__}.")
                else:
                    print("\nYour attack missed!")

                # Enemy's turn
                enemy_damage = enemy.attack(self.player)
                # Reduce the player's health by the enemy's damage
                self.player.health -= enemy_damage
                if enemy_damage > 0:
                    print(
                        f"The {enemy.__class__.__name__} dealt {enemy_damage} damage to you!")
                    print("------------------------------")
                else:
                    print(f"The {enemy.__class__.__name__}'s attack missed!")
                    print("------------------------------")
            elif player_action == "B":
                blocked_damage, actual_damage = self.player.block(enemy)
                if actual_damage == 0:
                    print("\nThe enemy missed their attack!")
                else:
                    print(
                        f"\nYou blocked {blocked_damage} damage and took {actual_damage} damage.")

            elif player_action == "C":
                player_choice = input(
                    "\nWould you like to save your game? (y/n):)")
                if player_choice == "y":
                    self.game_state.save_game(
                        self.player, self.defeated_enemies, self.current_location)
                    print("Game saved!")
                    sys.exit()
                else:
                    print("Thanks for playing :)")
                    sys.exit()
            else:
                print("\nInvalid choice, please try again.")
                continue

        if enemy.health <= 0:
            print(f"\nYou defeated the {enemy.__class__.__name__}!")
            self.increment_defeated_enemies()
            # Reset the player's health after each encounter
            self.player.health = self.player.max_health

        print(
            f"Enemy health: {enemy.health}, Your health: {self.player.health}")

    def _generate_enemy(self):
        enemy_class = random.choice([Yeti, Mothman, Sandman])
        return enemy_class()

    def increment_defeated_enemies(self):
        self.defeated_enemies += 1

    def reset_game(self):
        self.player.health = self.player.max_health
        self.player.stamina = self.player.max_stamina
        self.defeated_enemies = 0

    def load_saved_game(self, game_data):
        character_class = game_data['player']['class']
        if character_class == 'Warrior':
            self.player = Warrior()
        elif character_class == 'Ranger':
            self.player = Ranger()
        elif character_class == 'Wizard':
            self.player = Wizard()

        self.player.health = game_data['player']['health']
        self.player.stamina = game_data['player']['stamina']
        self.defeated_enemies = game_data['defeated_enemies']
        self.current_location = game_data['current_location']

    def player_defeated(self):
        while True:
            print()
            print("You have been defeated :(")
            print()
            choice = input(
                "What would you like to do?\n1. Restart\n2. Quit\n\nEnter the number of your choice: ")

            if choice == "1":
                self.reset_game()
                self.start()
                break
            elif choice == "2":
                print("Thanks for playing! Goodbye.")
                sys.exit()
            else:
                print("Invalid choice, please try again.")

    def player_win(self):
        print("Congratulations, you won!")
        print("Thanks for playing! Goodbye.")
        sys.exit()
