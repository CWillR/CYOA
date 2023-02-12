import os
import random

class Player:
    #Player Stats
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.money = 1000.0
        self.BAC = 0.0
        self.fun = 0     

#Display player's current stats 
def inventory(self):
    print("Name: ",self.name,"\nWeight: ",self.weight,"\nMoney: $",self.money)

#Prevent player from choosing a nonexistent  
def noOption(numberOfChoices, choice):
    if numberOfChoices == "1":
        if choice == "1":
            return choice
        else:
            choice = input("\nYou must choose '1' in order to continue\n")
            noOption(numberOfChoices, choice)
    if numberOfChoices == "2":
        choices = ["1", "2"]
        if choice in choices:
            return choice
        elif choice not in choices:
            choice = input("\nYou must choose '1' or '2' in order to continue\n")
            noOption(numberOfChoices, choice)

#Introduction to the initial game laying out the typical usage of the game to the user
print("Welcome to our Choose Your Own Vacation Game\nIn our game you'll have the option to choose various choices that'll affect the outcome of your adventure.\n\n")
choice = input("1) Type '1' and press enter to begin\n")
choice = noOption("1", choice)
os.system('cls')

#Customizing your character and updating the player class with user inputs/random inputs
print("Character Creator\n")
name = input("Enter a name: ")
choice = input("\nWould you like to enter a weight of your choice or have us choose for you? (random number 100-300)\n1) I'll Enter a custom weight.\n2) Choose for me.\n")
choice = noOption("2", choice)
weight = 0
if(choice == "1"):
    weight = int(input("Enter your custom weight: "))
elif(choice == "2"):
    weight = random.randint(100,300)
character = Player(name, weight) #Saves the custom character information
os.system('cls')

#Beginning of Day 1
print("dialogue about your plane landing and you now being in the airport...\n\n1) Pick up your luggage and leave the airport.\n2) Leave your luggage behind and leave the airport.")