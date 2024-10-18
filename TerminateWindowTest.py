import subprocess
import time
import sys

def open_game():
    try:
        # Start the game script as a subprocess
        process = subprocess.Popen(["python", "GameStates/State_1.py"])
        return process
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def close_game(process):
    try:
        process.terminate()  # Terminate the subprocess
        process.wait()       # Wait for the process to finish
    except Exception as e:
        print(f"Error closing the game: {e}")

# Open the game
game_process = open_game()

# Simulate doing something in the main script
time.sleep(1)  # Keep the main script running for 10 seconds

# Close the game after the delay
close_game(game_process)
print("Game closed.")