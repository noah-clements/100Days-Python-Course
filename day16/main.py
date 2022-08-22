from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
register = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    action = input(f"What would you like? ({menu.get_items()}):")
    if action.lower() == "off":
        is_on = False
    elif action.lower() == "report":
        maker.report()
        register.report()
    else:
        drink = menu.find_drink(action)
        if maker.is_resource_sufficient(drink):
            print(f"That will be ${drink.cost}.")
            if register.make_payment(drink.cost):
                maker.make_coffee(drink)
        else:
            print(f"Sorry, we can't make {drink.name}s right now.")
