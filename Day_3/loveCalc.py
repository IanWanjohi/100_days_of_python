# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lowerCase_name = combined_names.lower()

# using .count() produces numbers as INTEGERS not STRINGS

t = lowerCase_name.count("t")
r = lowerCase_name.count("r")
u = lowerCase_name.count("u")
e = lowerCase_name.count("e")

true = t + r + u + e

l = lowerCase_name.count("l")
o = lowerCase_name.count("o")
v = lowerCase_name.count("v")
e = lowerCase_name.count("e")

love = l + o + v + e

loveScore = int( str(true) + str(love) )        

print (loveScore)

if (loveScore < 10) or (loveScore > 90):
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (loveScore < 10) or (loveScore > 90):
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}")