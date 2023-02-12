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
    
def inventory(self):
    print("Name: ",self.name,"\nWeight: ",self.weight,"\nMoney: $",self.money)
        

#Introduction to the initial game laying out the typical usage of the game to the user
print("Welcome to our Choose Your Own Vacation Game\nIn our game you'll have the option to choose various choices that'll affect the outcome of your adventure.\n\n")
choice = input("1) Press '1' and press enter to begin\n")
while choice != "1":
    print("you gotta type 1 and only 1 to begin bro\n")
    choice = input("Press '1' and press enter to begin\n")
os.system('cls')

#Customizing your character and updating the player class with user inputs/random inputs
print("Character Creator\n")
name = input("Enter a name: ")
#Choice for auto-weight or entering your own weight
choice = input("\nWould you like to enter a weight of your choice or have us choose for you? (random number 100-300)\n1) I'll Enter a custom weight.\n2) Choose for me.\n")
if(choice == "1"):
    weight = int(input("Enter your custom weight: "))
elif(choice == "2"):
    weight = random.randint(100,300)
character = Player(name, weight) #Saves the custom character information

os.system('cls')
inventory(character)
