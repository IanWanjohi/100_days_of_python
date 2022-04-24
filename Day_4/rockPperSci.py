import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice = int(input("What do you pick? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n"))

comp_choice = random.randint(0, 2)

game_img = [rock, paper, scissors]

print("You chose: ")
print(game_img[user_choice])

print("Comp chose: ")
print(game_img[comp_choice])


if user_choice < 0 or user_choice >= 3:
  print("Your number is invalid! You lose!!")
  
elif user_choice == 0 and comp_choice == 2:
  print("You win!!")
elif user_choice == 2 and comp_choice == 0:
  print("You lose!!")
  
elif user_choice > comp_choice:
  print("You win!!")
elif user_choice < comp_choice:
  print("You lose!!")
  
elif user_choice == comp_choice:
  print("You draw!!")
