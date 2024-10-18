from subprocess import call

def close_game(process):
        call(["python", "GameStates/State_1.py"])
        process.terminate()  # Terminate the process
        process.wait()       # Wait for the process to close