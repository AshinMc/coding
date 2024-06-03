import time
import random

inputs = {}

def readInto(target, transformer, dependent):
    buffer = input();

    if callable(transformer):
        transformed = transformer(buffer)

        while transformed == None:
            print("Your input in invalid, enter again")
            transformed = transformer(input())

        inputs[target] = transformed
    else:
        inputs[target] = buffer

    if callable(dependent):
        dependent(inputs[target])

def display(messages):
    for (msg, action) in messages:
        print(msg, end='', flush=True)

        match action:
            case int() | float():
                time.sleep(action)
            case a if callable(a):
                a()
            case _:
                print(f"Unknown action {a}")

messages = [
    ("Hello\n", 1),
    ("Welcome to Rock", 0.3),
    (" Paper", 0.3),
    (" Scissor", 0.7),
    ("...\n", 1),
    ("Dear player, the fate of the world lies on your hands..\n", 1.8),
    ("May I know your name: ", lambda : readInto("name", None, lambda s: display([(f"{inputs['name']}, sounds like the name of a hero\n", 1)]))),
    ("My time is almost up...", 0.7),
    ("Do you know how to use the sacred technique of... ", 0.3),
    ("ROCK, PAPER, SCISSOR (Y OR N)?\n", lambda : readInto("accept", lambda s : True if s == "Y" else False if s == "N" else None, lambda b : print("Good.. Proceed and save the world!" if b else "These are the sacred rules, Rock beats Paper, Paper beats Rock and Scissor beats paper.\n Go ahead and save the world!" )))
]

display(messages)

computer = random.choice(["rock", "paper", "scissors"])

states = {
    "rock": {
        "rock": None,
        "paper": False,
        "scissors": True
    },
    "paper": {
        "rock": True,
        "paper": None,
        "scissors": False
    },
    "scissors": {
        "rock": False,
        "paper": True,
        "scissors": None
    },
}

display([("Enter a choice (rock, paper, scissors): ", lambda : readInto("choice", lambda s : s if s == "rock" or s == "paper" or s == "scissors" else None, lambda user : print(f"You chose {user}, antagonist chose {computer}, " + ("it's a draw!" if states[user][computer] is None else "you win!" if states[user][computer] else "you lose.") + "\nThe end.")))])
