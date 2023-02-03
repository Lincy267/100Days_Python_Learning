import data
import decimal


def receive_coins():
    print("Please insert coins.")
    quarters_inserted = float(input("how many quarters? ")) * 0.25
    dimes_inserted = float(input("how many dimes? ")) * 0.1
    nickles_inserted = float(input("how many nickles? ")) * 0.05
    pennies_inserted = float(input("how many pennies? ")) * 0.01
    coins_inserted = [quarters_inserted, dimes_inserted, nickles_inserted, pennies_inserted]
    total_coins = sum(coins_inserted)
    return total_coins

def get_cost(total_coins):
    if choice == "espresso":
        cost_of_coffee = float(data.MENU["espresso"]["cost"])
        return cost_of_coffee
    elif choice == "latte":
        cost_of_coffee = float(data.MENU["latte"]["cost"])
        return cost_of_coffee
    elif choice == "cappuccino":
        cost_of_coffee = float(data.MENU["cappuccino"]["cost"])
        return cost_of_coffee

def report():
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g")
    print(f"Money: ${total_coins}")

def transactions(cost_of_coffee, total_coins):

    if cost_of_coffee > total_coins:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(total_coins - cost_of_coffee, 2)
        print(f"Here is ${change} in change.\nHere is your {choice}. Enjoy!")



# TODO 1:  WHILE LOOP
total_coins = 0
choice = input("costs:\nespresso: 1.5\nlatte: 2.5\ncappuccino: 3\nWhat would you like? (espresso/latte/cappuccino): ")
if choice != "report":
    total_coins = receive_coins()
    cost_of_coffee = get_cost(total_coins)
    transactions(cost_of_coffee, total_coins)
else:
    report()

# TODO 2: UPDATE DATA AFTER TRANSACTIONS ARE MADE
