MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


on_state = True
profit = 0


def enough_resources(ingredients):
    """Returns True if order can be made."""
    for item in ingredients:
        if resources[item] <= ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def coin_count():
    """Returns total value of coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.5
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


def transaction_success(amount_paid, drink_cost):
    """Return True if payment is accepted, False if it's insufficient."""
    global profit
    if amount_paid >= drink_cost:
        profit += drink_cost
        change = round(amount_paid - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    """Deduct the used up ingredients from resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}.")


while on_state:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        on_state = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = coin_count()
            if transaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

 