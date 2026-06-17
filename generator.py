
# RPG Character Generator

import random

def roll_attributes():
    return {
        "Strength": random.randint(5, 20),
        "Agility": random.randint(5, 20),
        "Intellect": random.randint(5, 20)
    }

def main():
print("--- Welcome to the Character Generator ---")
# Components will be combined here
name = "Hero"
print(f"\nCharacter {name} has been successfully created!")
if __name__ == "__main__":
main()
