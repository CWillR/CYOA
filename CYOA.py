import os
import random
import time


martini = 0.9
beer = 0.6
pina = 2.6
margarita = 1.25
daq = 1.2
wine = 3.25




class Player:
   # Player Stats
   def __init__(self, name, weight):
       self.name = name
       self.weight = weight
       self.money = 1000.0
       self.BAC = 0.0
       self.fun = 0




def inventory(self):
   print("Name: ", self.name, "\nWeight: ", self.weight, "\nMoney: $", self.money, "\nFun: ", self.fun)




def noOption():
   print("\nPlease choose one of the choices given.\n")




# Introduction to the initial game laying out the typical usage of the game to the user
print(
   "Welcome to our Choose Your Own Vacation Game\nIn our game you'll have the option to choose various choices that'll affect the outcome of your adventure.\n\n")
choice = input("1) Press '1' and press enter to begin\n")
while choice != "1":
   noOption()
   choice = input("Press '1' and press enter to begin\n")
os.system('cls')


# Customizing your character and updating the player class with user inputs/random inputs
print("Character Creator\n")
name = input("Enter a name: ")
# Choice for auto-weight or entering your own weight
choices = ["1", "2"]
choice = input(
   "\nWould you like to enter a weight of your choice or have us choose for you? (random number 100-300)\n1) I'll Enter a custom weight.\n2) Choose for me.\n")
while choice not in choices:
   noOption()
   choice = input(
       "\nWould you like to enter a weight of your choice or have us choose for you? (random number 100-300)\n1) I'll Enter a custom weight.\n2) Choose for me.\n")
if (choice == "1"):
   weight = int(input("Enter your custom weight: "))
elif (choice == "2"):
   weight = random.randint(100, 300)
character = Player(name, weight)  # Saves the custom character information
os.system('cls')


# Day 1
# Decision 1
print("After a long week at work, you are excited to finally go on a vacation you have planned for months.\nYou are about to land at the Maui airport when the child behind you starts kicking and screaming, can this plane land any faster?\n")
choice = input(
   "\n1) Explore the airport.\n2) Leave the airport.\n")
while choice not in choices:
   noOption()
   choice = input(
       "\n1) Pick up your luggage and leave the airport.\n2) Leave your luggage behind and leave the airport.\n")
if (choice == "1"):
   print("you remember to get your luggage")
if (choice == "2"):
   print("you forgot your luggage so you now have nothing to wear")
   character.luggage = 0
time.sleep(3)
os.system('cls')
# Decision 2
print("you go to your hotel, take a nap, after which you decide what you'll do today")
choices = ["1", "2", "3"]
choice = input("\n1) stay in the hotel\n2) go to the beach\n3) go to the casino\n")
while choice not in choices:
   noOption()
   choice = input("\n1) stay in the hotel\n2) go to the beach\n3) go to the casino\n")
if (choice == "1"):
   print("you decide to stay in your hotel room")
   # Decision 3
   time.sleep(3)
   os.system('cls')
   print("After waking up you decide to watch some TV. A new episode of your favorite show comes on in 20 minutes, so there is really no time to go out.\nA new character is introduced, a funny lawyer with low budget commercials and a bad haircut. Seems like the protagonist needs some legal advice,\nbut the smart talking attorney is uncooperative. A very tense desert scene occurs where the lawyer is held at gunpoint by the main characters\nbut uses his wits and charisma to get out of the situation.\n""As the episode ends, a slight grin appears on your face. This new character is so captivating, so intriguing, so… riveting.\nAt that moment, you realize that this vacation is going to be all good, man.")
   time.sleep(15)
   os.system('cls')
   # End of this path and continues at Day 2
if (choice == "2"):
   # Decision 3
   print("you go to the beach")
   time.sleep(3)
   os.system('cls')
   print("after arriving at the beach you decide what you would like to do here")
   choices = ["1", "2"]
   choice = input("\n1) Go to the tiki bar\n2) Go surfing\n")
   if (choice == "1"):
       print("you arrive at the tiki bar")
       time.sleep(3)
       os.system('cls')
       # Decision 4
       choice = input(
           "\n1) Do you buy an alcoholic drink?\n2) Do you decide to make small talk with the other guests?\n")
       if (choice == "1"):
           # Decision 5
           choice = input("\n1) Margarita ($15)\n2) Pina Colada ($20)\n")
           if (choice == "1"):
               character.BAC = 7.16 * martini / character.weight
               character.money = character.money - 15
               print('Your BAC is', format(character.BAC,'.3f'))
               print("\nAfter your margarita you feel out of it and head to bed and sleep until the next day")
               # End of this path and continues at Day 2
           if (choice == "2"):
               character.BAC = 7.16 * pina / character.weight
               character.money = character.money - 20
               print('Your BAC is', format(character.BAC,'.3f'))
               choice = "4"
               print("\nAfter your pina colada you feel out of it and head to bed and sleep until the next day")
               # End of this path and continues at Day 2
       if (choice == "2"):
           print("\nYou talk with the other guests\n")
           print(
               "\nAfter talking with the guests for a while you get tired and head back to bed and sleep until the next day")
           # End of this path and continues at Day 2
   if (choice == "2"):
       print("you decide to go surfing ($80)\n")
       character.money = character.money - 80
       num = random.randint(1, 4)
       if (num == 2):
           print("SHARK ATTACK!\nYOU DIED, Death did you a favor, CONTINUE ON DAY 2")
           # End of this path and continues at Day 2
       else:
           print("After surfing you found some cool seashells")
           print("\nSeashells have been added to your inventory")
           character.fun = character.fun + 1
           print("\nAfter surfing you are tired and head to bed in your hotel, and sleep until the next day")
           # End of this path and continues at Day 2
if (choice == "3"):
   # Decision 3
   print("you go to the casino")
   time.sleep(3)
   os.system('cls')
   choices = ["1", "2"]
   choice = input("\n1) Go gambling\n2) Go for a drink at the bar\n")
   if (choice == "1"):
       print("\nYou go to a gambling minigame\n")
       ITEMS = ["CHERRY", "PLUM", "BAR"]
       firstWheel = None
       secondWheel = None
       thirdWheel = None
       stake = character.money
       def play():
           global stake, firstWheel, secondWheel, thirdWheel
           playQuestion = askPlayer()
           while (stake != 0 and playQuestion == True):
               firstWheel = spinWheel()
               secondWheel = spinWheel()
               thirdWheel = spinWheel()
               printScore()
               playQuestion = askPlayer()
       def askPlayer():
           global stake
           while (True):
               answer = input("You have $" + str(stake) + " Are you ready to gamble? \n 1) for yes \n 2) for no \n")
               if (answer == "1"):
                   return True
               elif (answer == "2"):
                   print("You were one game away from hitting the jackpot")
                   return False
               else:
                   print("Please choose one of the choices given")
       def spinWheel():
           randomNumber = random.randint(0, 2)
           return ITEMS[randomNumber]
       def printScore():
           global stake, firstWheel, secondWheel, thirdWheel
           if ((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
               win = 5
           elif ((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "PLUM") or (
                   firstWheel == "PlUM")):
               win = 5
           elif ((firstWheel == "PLUM") and (secondWheel == "PLUM") and (thirdWheel == "CHERRY") or (
                   firstWheel == "CHERRY")):
               win = 5
           elif ((firstWheel == "PLUM") and (secondWheel == "PLUM") and (thirdWheel == "PLUM")):
               win = 5
           elif ((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
               win = 100
           else:
               win = -25
           stake += win
           character.money = stake
           if (win > 0):
               print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + '\t' + ' - You hit the jackpot!')
           else:
               print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' - Better spin again!')
       play()
       print(
           "After gambling, despite you winning or losing, you decide to head back to bed in your hotel and sleep until the next day")
       time.sleep(3)
       # End of this path and continues at Day 2
   if (choice == "2"):
       choice = input("\n1) Buy a martini ($12)\n2) Buy beer ($8)\n")
       if (choice == "1"):
           character.money = character.money - 12
           character.BAC = 7.16 * martini / character.weight
           print('Your BAC is', format(character.BAC,'.3f'))
           print("\nAfter drinking the martini, you head back to your hotel and sleep until the next day")
           # End of this path and continues at Day 2
       if (choice == "2"):
           character.money = character.money - 8
           character.BAC = 7.16 * beer / character.weight
           print('Your BAC is', format(character.BAC,'.3f'))
           print("\nAfter drinking your beer, you head back to your hotel room and sleep until next day")
           # End of this path and continues at Day 2


# Day 2
os.system('cls')
inventory(character)
choices = ["1", "2", "3", "4"]
choice = input(
   "After waking up the next day, you decide to...\n1) Stay in the hotel room\n2) Go to the beach\n3) Visit the volcano, Haleakala\n")
if (character.BAC > 0):
   choice == "4"
if (choice == "1"):
   print("You decide to stay in your hotel and watch tv until it is time for you to board your flight back home\n")
   print("GAME OVER")
   # Game End Scenario
if (choice == "2"):
   print("\nYou make your way to the beach.\n")
   # Decision 2
   choices = ["1", "2"]
   choice = input("\n1) Rent a boat ($450)\n2) Go buy a drink\n")
   if (choice == "1"):
       character.money = character.money - 450
       print("You rent a boat and decide to practice your sailing skills")
       time.sleep(3)
       os.system('cls')
       # Decision 3
       choice = input(
           "\n1) You come across a mermaid that offers you a seashell\n2) You meet some Pirates and you decide to talk to them\n")
       if (choice == "1"):
           character.fun = character.fun + 1
           print("After accepting the shell, you return to shore in time to catch your flight back home\n GAME OVER")
           # Game End Scenario
       if (choice == "2"):
           print(
               "\nThe Pirates threaten you and force you to help them find some treasure, find it or suffer the consequences!\n")
           from random import randint
           Hidden_Treasure = [[' '] * 3 for x in range(3)]
           Guess_Treasure = [[' '] * 3 for x in range(3)]
           let_to_num = {'A': 0, 'B': 1, 'C': 2}
           def print_board(board):
               print('  A B C')
               row_num = 1
               for row in board:
                   print("%d^%s^" % (row_num, "^".join(row)))
                   row_num += 1
           def Treasure_location():
               row = input('Enter a row 1-3 ').upper()
               while row not in '123':
                   print("Not a row ")
                   row = input('Enter a row 1-3 ')
               column = input('Enter a column A-C ').upper()
               while column not in 'ABC':
                   print("Not a column ")
                   column = input('Enter a column A-C ')
               return int(row) - 1, let_to_num[column]
           def create_Treasure(board):
               for Chest in range(3):
                   Chest_r, Chest_cl = randint(0, 2), randint(0, 2)
                   while board[Chest_r][Chest_cl] == 'X':
                       Chest_r, Chest_cl = randint(0, 2), randint(0, 2)
                   board[Chest_r][Chest_cl] = 'X'
           def Treasurefound(board):
               count = 0
               for row in board:
                   for column in row:
                       if column == 'X':
                           count += 1
               return count
           create_Treasure(Hidden_Treasure)
           turns = 4
           while turns > 0:
               print('Find the buried treasure lad')
               print_board(Guess_Treasure)
               row, column = Treasure_location()
               if Guess_Treasure[row][column] == 'o':
                   print(' Arghh you already looked there ')
               elif Hidden_Treasure[row][column] == 'X':
                   print(' You found the treasure matey! ')
                   print('The pirates thank you for the help, and drop you off')
                   Guess_Treasure[row][column] = 'X'
                   turns -= 1
               else:
                   print('Not there sailor')
                   Guess_Treasure[row][column] = 'o'
                   turns -= 1
               if Treasurefound(Guess_Treasure) == 1:
                   break
               print(' Only ' + str(turns) + ' tries ramaining')
               if turns == 0:
                   print('Dead men tell no tales ')
                   print('The Pirates shoot you out of a cannon onto shore, you stumble toward the bar.')
                   break
           # if you lose, thats the end of the whole game cause you die
           # if you win, you get another fun point and go home and the game ends
   if (choice == "2"):
       print("\nYou decide to go to the bar to buy a drink")
       time.sleep(3)
       os.system('cls')
       # Decision 3
       choice = input("\n1) Buy a daiquiri ($13)\n2) Buy some wine ($8) \n")
       if (choice == "1"):
           character.money = character.money - 13
           character.BAC = 7.16 * daq / character.weight
           print('Your BAC is', format(character.BAC,'.3f'))
           print("\nAfter sitting at the bar, drinking your daquiri for a bit, you realize its time to head home\n")
           print("GAME OVER")
           # Game End Scenario
       if (choice == "2"):
           character.money = character.money - 8
           character.BAC = 7.16 * wine / character.weight
           print('Your BAC is', format(character.BAC,'.3f'))
           print("\nAfter sitting at the bar, drinking your wine for a bit, you realize its time to head home\n")
           print("GAME OVER")
           # Game End Scenario
if (choice == "3"):
   num = random.randint(1, 20)
   if (1 <= num <= 3):
       print("\nYou fell into the volcano and died")
       print("\nGAME OVER")
       # Game Ending Scenario
   else:
       print("\nAfter visiting the volcano you realize it's time to go home")
       print("\nGAME OVER")
       # Game Ending Scenario
if (choice == "4"):
   print("\nUnfortunately, due to the alcohol you drank yesterday, you are too hungover to do anything today.")
   print("\nSo you sleep most of the day away and by the time you wake up, it's time to leave the island and go home.")
   print("\nGAME OVER")
   # Game Ending Scenario
   # Print inventory at end of game
