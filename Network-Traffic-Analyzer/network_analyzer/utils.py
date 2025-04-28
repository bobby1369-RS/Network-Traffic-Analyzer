import time

def log_action(action):
    # Logs the action with a timestamp
    with open("logs/actions.log", "a") as file:
        file.write(f"{time.ctime()}: {action}\n")

