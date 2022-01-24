#treasure island word game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 



direction = input("You finally arrive on shore, exhausted from the long journey. You notice rum to your left and food to your right. Which way would you like to go? Type \"left\" or \"right\".\n").lower()

if direction == "left":
  water = input("Before you get to the rum, you notice that your path is actually blocked by a stream of lava. Would you like to swim through the lava or wait? Type \"swim\" or \"wait\".\n").lower()
  if water == "wait":
    door = input("You finally arrive to the rum only to find out it was a mirage the whole time. But all is not lost. After looking around a moment, you happen upon a hut with 3 doors, red, yellow and blue. Which door would you like to open? Type \"red\", \"yellow\", or \"blue\".\n").lower()
    if door == "red":
      print("You open the door to a room full of molten lava. You instantly catch fire and melt to your doom. Game Over.")
    elif door == "blue":
      print("You open the door and find a jaguar who eats you. Game Over.")
    elif door == "yellow":
      print("You have found Captain Jack Sparrow's treasure! You Win!")
    else:
      print("That wasn't an option! Game Over.")
  else:
    print("You bilge rat! You're now dead. It's lava, what did you expect?! \nGame Over.")
else:
  print("You should always go for the rum! Game over.")