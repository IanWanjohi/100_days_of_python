# Functions

def greet():
  print("Hello World.")
  print("It's sunny innit?")

greet()

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How are you doing {name}?")

greet_with_name("Vitaliy")

####  Parameters and Arguements

# Functions with more than 1 input
##   Positional & Keyword Arguements

def greet_me(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

## Positional Arguements
greet_me("Ruslan", "Kyiev")

## Keyword Arguements
greet_me(name = "Ruslan", location = "Kyiev")

