from random import randint
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

attempts = 0

## Function to check user's guess against the answer.
def check_answer(guess, answer, attempts):
  """Checks answer against guess. Returns no. of attempts remaining."""
  if guess > answer:
    print("Too high.")
    return attempts - 1
  elif guess < answer:
    print("Too low.")
    return attempts - 1
  else:
    print(f"You got it! The answer was {answer}")


## Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard':")
  if level == "easy":
    return EASY_LEVEL_ATTEMPTS
  else:
    return HARD_LEVEL_ATTEMPTS


def game():

  print(logo)
  
  ## Choosing a random no. btwn 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  
  attempts = set_difficulty()
  
  guess = 0
  
  ## Repeat guessing if answer is wrong.
  while guess != answer:
    print(f"You have {attempts} attempts remaining to guess the number.")
    ## Let user to make a guess.
    guess = int(input("Make a guess: "))
    
    attempts = check_answer(guess, answer, attempts)
    if attempts == 0:
      print("You have run out of guesses. You lose.")
      return
    elif guess != answer:
      print("Guess Again")

## Track no. of attempts and reduce by one is answer is wrong.

game()
 