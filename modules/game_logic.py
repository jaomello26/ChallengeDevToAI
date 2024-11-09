# modules/game_logic.py
from modules.ai_utils import generate_response
from modules.database import save_interaction

def start_game():
    initial_prompt = "Welcome to the game! What do you want to do?"
    response = generate_response(initial_prompt)
    save_interaction(initial_prompt, response)
    return response

def process_player_input(player_input):
    response = generate_response(player_input)
    save_interaction(player_input, response)
    return response
