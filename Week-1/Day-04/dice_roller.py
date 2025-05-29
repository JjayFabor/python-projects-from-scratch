'''
Simulate the rolling of a dice. When the user presses a key,
the program shows a random number between 1 and 6.
'''
import time
import random

# ASCII art for dice faces
dice_faces = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ]
}

def display_dice(value):
    for line in dice_faces[value]:
        print(line)

def roll_dice():
    print("\nWelcome to Roll the dice simulation.\n\n    ")
    user_input = input("Press Enter to roll the dice...")

    print("\nThe dice is rolling...")
    for _ in range(5):
        time.sleep(0.5)
        print("\nRolling...")
        display_dice(random.randint(1, 6))

    dice_value = random.randint(1, 6)
    print("\nFinal result:")
    display_dice(dice_value)

    return f'\nThe dice value is {dice_value}.\n'

print(roll_dice())
