import json
import os
from typing import Optional

class GameState:
    def __init__(self):
        self.filename = "savegame.json"
        self.state = {
            "player": None,
            "level": None,
            "enemies_defeated": 0,
        }

    def load_game(self) -> Optional[dict]:
        try:
            with open('savegame.json', 'r') as f:
                game_data = json.load(f)
            return game_data
        except FileNotFoundError:
            print("No saved game found. Starting a new game.")
            return None
        except Exception as e:
            print(f"Error loading game: {e}")
            return None

    def save_game(self, player, defeated_enemies, current_location):
        game_data = {
            'player': {
                'class': player.__class__.__name__,
                'health': player.health,
                'stamina': player.stamina,
            },
            'defeated_enemies': defeated_enemies,
            'current_location': current_location,
        }
        
        with open(self.filename, 'w') as f:
            json.dump(game_data, f)

    def reset_game(self):
        os.remove(self.filename)
        self.state = {
            "player": None,
            "level": None,
            "enemies_defeated": 0,
        }
