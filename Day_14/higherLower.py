from art import logo, vs
from game_data import data
import random
from replit import clear


## Function for displaying people's data.
def person_data(person):
  """Print out person's data."""
  name = person["name"]
  description = person["description"]
  country = person["country"]
  return f"{name}, a {description}, from {country}."


## Function for checking if guess is correct.
def check_answer(guess, followers1, followers2):
  """Takes user's guess, both persons' follower count and returns if user's guess is correct."""
  if followers1 > followers2:
    return guess == "A"
  else:
    return guess == "B"


## Display Logo
print(logo)
score = 0

person2 = random.choice(data)
game_continue = True


## Game to loop as long as guess is correct.
while game_continue:
  ## Generate a random person's data from game_data
  person1 = person2
  person2 = random.choice(data)
  if person1 == person2:
    person2 = random.choice(data)
  
  ## Print comparisons of both.
  print(f"Compare A: {person_data(person1)}")
  print(vs)
  print(f"Against B: {person_data(person2)}")
  
  
  ## Input guess from user
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()

  
  ## Check if user's guess is correct.
  # Get follower counts of both persons.
  person1_followers = person1["follower_count"]
  person2_followers = person2["follower_count"]
  
  guess_check = check_answer(guess, person1_followers, person2_followers)

  ## Clear screen and print logo
  clear()
  print(logo)

  
  # Give user feedback and scores.
  if guess_check:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    game_continue = False
    print(f"Sorry, that's wrong. Final score: {score}.")
 