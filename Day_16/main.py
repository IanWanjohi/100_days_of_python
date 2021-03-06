from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True


while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? ({options})")
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    drink_cost = drink.cost
    resource_sufficient = coffee_maker.is_resource_sufficient(drink)
    payment_made = money_machine.make_payment(drink_cost)
    if resource_sufficient and payment_made:
      coffee_maker.make_coffee(drink)

 