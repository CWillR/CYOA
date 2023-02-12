import os
import random
import time

class Player:
    #Player Stats
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.money = 1000.0
        self.BAC = 0.0
<<<<<<< Updated upstream
        self.fun = 0     

#Display player's current stats 
=======
        self.fun = 0  
         
    
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
#Beginning of Day 1
print("dialogue about your plane landing and you now being in the airport...\n\n1) Pick up your luggage and leave the airport.\n2) Leave your luggage behind and leave the airport.")
=======
#Day 1
#Decision 1
print("dialogue about your plane landing and you now being in the airport...\n")
choice = input("\n1) Pick up your luggage and leave the airport.\n2) Leave your luggage behind and leave the airport.\n")
while choice not in choices:
    noOption()
    choice = input("\n1) Pick up your luggage and leave the airport.\n2) Leave your luggage behind and leave the airport.\n")
if(choice == "1"):
    print("you got your luggage")
if(choice == "2"):
    print("you left your luggage")
    character.luggage = 0
time.sleep(3)
os.system('cls')
#Decision 2
print("you go to your hotel, take a nap, after which you decide what you'll do today")
choices = ["1", "2", "3"]
choice = input("\n1) stay in hotel\n2) go to beach\n3) go to casino\n")
while choice not in choices:
    noOption()
    choice = input("\n1) stay in hotel\n2) go to beach\n3) go to casino\n")
if(choice == "1"):
    print("you stay in your hotel")
    #Decision 3
    time.sleep(3)
    os.system('cls')
    print("After waking up you decide to watch an interesting movie until the next day.")
    time.sleep(10)
    os.system('cls')
    #End of this path and continues at Day 2
if(choice == "2"):
    #Decision 3
    print("you go to the beach")
    time.sleep(3)
    os.system('cls')
    print("after arriving at the beach you decide what you would like to do here")
    choices = ["1", "2"]
    choice = input("\n1) Go to the tiki bar\n2) Go surfing\n")
    if(choice == "1"):
        print("you arrive at the tiki bar")
        time.sleep(3)
        os.system('cls')
        #Decision 4
        choice = input("\n1) Do you buy an alcoholic drink?\n2) Do you decide to make small talk with the other guests?\n")
        if(choice == "1"):
            #Decision 5
            choice = input("\n1) Margarita\n2) Pina Colada\n")
            if(choice == "1"):
                character.BAC = character.BAC + 1 #get actual value
                print("\nAfter your margarita you feel out of it and head to bed and sleep until day 2")
                #End of this path and continues at Day 2
            if(choice == "2"):
                character.BAC = character.BAC + 2 #get actual value
                print("\nAfter your pina colada you feel out of it and head to bed and sleep until day 2")
                #End of this path and continues at Day 2
        if(choice == "2"):
            print("\nYou talk with the other guests\n")
            print("\nAfter talking with the guests for a while you get tired and head back to bed and sleep until Day 2")
            #End of this path and continues at Day 2
    if(choice == "2"):
        print("you decide to go surfing\n")
        num = random.randint(1,4)
        if(num == 2):
            print("shark got you and you died\nYOU DIED, CONTINUE ON DAY 2")
            #End of this path and continues at Day 2
        else:
            print("After surfing you found some cool seashells")
            print("\nSeashells have been added to your inventory")
            character.fun = character.fun + 1
            print("\nAfter surfing you are tired and head to bed in your hotel, and sleep until Day 2")
            #End of this path and continues at Day 2    
if (choice == "3"):
    #Decision 3
    print("you go to the casino")
    time.sleep(3)
    os.system('cls')
    choices = ["1", "2"]
    choice = input("\n1) Go gambling\n2) Go for a drink at the bar\n")
    if(choice == "1"):
        print("\nYou go to a gambling minigame")
        #add gambling minigame here
        print("After gambling, despite you winning or losing, you decide to head back to bed in your hotel and sleep until Day 2")
        #End of this path and continues at Day 2
    if(choice == "2"):
        choice = input("\n1) Buy a martini\n2) Buy beer\n")
        if(choice == "1"):
            print("\nAfter drinking the martini, you head back to your hotel and sleep to Day 2")
            #End of this path and continues at Day 2
        if(choice == "2"):
            print("\nAfter drinking your beer, you head back to your hotel room and sleep to Day 2")
            #End of this path and continues at Day 2

#Day 2
>>>>>>> Stashed changes
