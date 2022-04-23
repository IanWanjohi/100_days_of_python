import random

random_integer = random.randint(1, 100)
print(random_integer)

# Print floating point  numbers btwn 0.0 and 1.0
random_float = random.random()
print(random_float)

# Print floating point  numbers btwn 0.0 and 10.0
random_float10 = random.random() * 10
print(random_float10)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")