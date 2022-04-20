# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
  print("Small Pizza: $15")
elif size == "M":
  bill += 20
  print("Medium Pizza: $20")
elif size == "L":
  bill += 25
  print("Large Pizza: $25")
else:
  print("Invalid option chosen!!")


if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  elif size == "M":
    bill += 3
  elif size == "L":
    bill += 3
  else:
    bill += 0
    print("Invalid option chosen!!")
elif add_pepperoni == "N":
  bill += 0
else:
  print("Invalid option chosen!!")


if extra_cheese == "Y":
  bill += 1
elif extra_cheese == "N":
  bill += 0
else:
  print("Invalid option chosen!!")

print(f"Your bill is {bill}")
    
