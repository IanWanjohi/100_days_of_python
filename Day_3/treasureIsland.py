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


user_choice1 = input('You are at a crossroad. Where do you want to go? Type "left" or "right".\n')
choice1 = user_choice1.lower()


if choice1 == "left":
  user_choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  choice2 = user_choice2.lower()

  
  if choice2 == "wait":
    user_choice3 = input('You have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
    choice3 = user_choice3.lower()

    
    if choice3 == "red":
      print("It\'s a room full of fire. Game Over!!!")
    elif choice3 == "yellow":
      print("You have found the treasure. You Win!!!")
    elif choice3 == "blue":
      print("It\'s a room full of beasts. Game Over!!!'")
    else:
      print("Invalid option. Game Over!!!")

  
  elif choice2 == "swim":
    print("You got attacked by a shark. Game Over!!!")
  else:
    print("Invalid option. Game Over!!!")

  
elif choice1 == "right":
  print("You fell into a hole. Game Over!!!")
else:
  print("Invalid option. Game Over!!!")


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


#Write your code below this line 👇

