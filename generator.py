# RPG Character Generator
def main():
print("--- Welcome to the Character Generator ---")
# Components will be combined here
name = "Hero"
print(f"\nCharacter {name} has been successfully created!")
if __name__ == "__main__":
main()

def choose_class():

classes = ["Warrior", "Mage", "Rogue"]

print("Available Classes:", ", ".join(classes))
choice = input("Choose your class: ").capitalize()

return choice if choice in classes else "Adventurer"
