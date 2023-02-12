import os

print("Welcome to our Choose Your Own Adventure Game\nIn our game you'll have various options (life choices) that change the outcome of your adventure.\n\n")
user_input = input("Press '1' and press enter to begin\n")
if user_input == "1":
    os.system('cls')
    print("Prelude:")
elif user_input != "1":
    print("you gotta type 1 and only 1 to begin bro")