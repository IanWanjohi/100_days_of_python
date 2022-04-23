import random

test_seed = int( input("Enter a seed number : ") )
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Get the total number of items in the list
no_of_items = len(names)
x = no_of_items - 1

# Generate random int numbers btwn 0 and last name
random_pick = random.randint(0, x)

who_is_paying = names[random_pick]
#who_is_paying = random.choice(names)


print(who_is_paying + " is going to buy the meal today.")
