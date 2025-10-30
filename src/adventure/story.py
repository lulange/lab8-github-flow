from adventure.utils import read_events_from_file
import random
from rich.console import Console

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return default_message

def left_path(event):
    return "[grey37]You walk left. " + event + "[/grey37]"

def right_path(event):
    return "[grey37]You walk right. " + event + "[/grey37]"

if __name__ == "__main__":
    console = Console()
    events = read_events_from_file('events.txt')

    console.print("[grey37]You wake up in a dark forest. You can go left or right.[/grey37]")
    while True:
        choice = console.input("[bold][gold3]Which direction do you choose?[/gold3][/bold] [plum2](left/right/exit):[/plum2] ")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        console.print(step(choice, events))
