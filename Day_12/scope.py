################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2  ## This is actually a newly defined variable.
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


## Global Scope
player_health = 100   ## Global Variable  available anywhere.

def drink_potion():
  potion_strength = 2    ## Local Variable available within the function only. Does not apply with if, for, while loops.
  print(player_health)
  print(potion_strength)

## There is no Block Scope

  
## Modifying Global Scope // not advisable!!
enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

## Global Constants should be in uppercase, to remind urself they shouldn't be redefined.
PI = 3.14159
print(PI)