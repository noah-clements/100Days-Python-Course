from decimal import Decimal

TWOPLACES = Decimal(10) ** -2

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

COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}


register = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0
}


# Print report of coffee machine resources
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']} g")
    print("Money: $" + str(calculate_money(register)))
    print(register)


# coffee
def make_coffee(type):
    coffee = MENU.get(type)
    # print (coffee.get('ingredients'))
    try:
        check_resources(coffee.get("ingredients"))
    except Exception as err:
        if isinstance(err, AttributeError):
            print("We don't have " + type + ". Please try again.")
        else:
            print(str(err))
        return

    print("Cost = $" + str(coffee.get('cost')))

    coins = insert_coins()
    money = calculate_money(coins)
    cost = coffee.get("cost")
    if money < cost:
        print(f"​Sorry that's not enough. You only inserted ${money}.")
        print(f"A {type} costs ${cost}. Money refunded.​")
    else:
        if money > cost:
            coins = make_change(coins, money - Decimal(cost))
        add_to_register(coins)
        brew(coffee.get("ingredients"))
        print(f"Here is your {type}. Enjoy!")

    return


# check resources
def check_resources(ingredients):
    for i in ingredients:
        needed = ingredients.get(i)
        have = resources.get(i)
        if have < needed:
            raise Exception("Sorry there is not enough " + i)


def brew(ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]


def insert_coins():
    print("Please insert your coins.")
    coins = {}
    for i in register.keys():
        for x in range(10):
            try:
                c = int(input("How many " + i.title() + "? "))
                if c < 0:
                    raise ValueError
                coins[i] = c
            except ValueError:
                print("Enter a positive integer")
            else:
                break
        else:
            print("We will assume you are inserting 0 " + i.title())

    return coins


def calculate_money(coins):
    money = 0.0
    for k, v in coins.items():
        money += v * COIN_VALUES[k]

    # money = (coins.get("quarters", 0) * 0.25)
    # money += (coins.get("dimes", 0) * 0.1)
    # money += (coins.get("nickels", 0) * 0.05)
    # money += (coins.get("pennies", 0) * 0.01)
    return Decimal(money).quantize(TWOPLACES)


def add_to_register(coins):
    for i in coins:
        register[i] += coins.get(i)


# take refund amount out of inserted coins before adding to register.
# Start with pennies? No - should not care.
def make_change(coins, overpay):
    print(f"You have inserted too much money. Here is ${overpay} in change.")
    refund = overpay
    for k, v in coins.items():
        amount = calculate_money({k: v})
        print({k: v})
        if amount < refund:
            refund -= amount
            coins[k] = 0
            print("Amount still to refund: " + str(refund))
        else:
            coin_value = COIN_VALUES[k]

            # change = amount - refund
            # print ("Making change: " + str(change))
            num_coins = int(refund / Decimal(coin_value).quantize(TWOPLACES))
            # num_coins = int (change / Decimal(coin_value))
            print("Refunding " + str(num_coins) + " " + str(k))
            refund -= Decimal(num_coins * coin_value).quantize(TWOPLACES)

            remain = refund % amount
            print("Making change: " + str(refund))
            print("Amount still to refund: " + str(remain))
            coins[k] -= num_coins
    print(coins)
    return coins


is_on = True

while is_on:
    action = input("What would you like? (espresso/latte/cappuccino):")
    if action.lower() == "off":
        is_on = False
    elif action.lower() == "report":
        report()
    else:
        make_coffee(action)

