import data
import decimal

coffee_machine_off = False
total_coins = 0
total_revenue = 0
change = 0

def receive_coins():
    print("Please insert coins.")
    quarters_inserted = float(input("how many quarters? ")) * 0.25
    dimes_inserted = float(input("how many dimes? ")) * 0.1
    nickles_inserted = float(input("how many nickles? ")) * 0.05
    pennies_inserted = float(input("how many pennies? ")) * 0.01
    coins_inserted = [quarters_inserted, dimes_inserted, nickles_inserted, pennies_inserted]
    total_coins = round(sum(coins_inserted),2)
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
    print(f"Money: ${total_revenue}")


def transactions(cost_of_coffee, total_coins, total_revenue):

    if cost_of_coffee > total_coins:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(total_coins - cost_of_coffee, 2)
        print(f"${total_coins} received.\nHere is ${change} in change.\nHere is your {choice}. Enjoy!")
        revenue = total_coins - change
        total_revenue += revenue
        return total_revenue


while not coffee_machine_off:
    choice = input("costs:\nespresso: 1.5\nlatte: 2.5\ncappuccino: 3\nWhat would you like? (espresso/latte/cappuccino): ")
    if choice != "report":
        total_coins = receive_coins()
        cost_of_coffee = get_cost(total_coins)
        total_revenue = transactions(cost_of_coffee, total_coins, total_revenue)
    else:
        report()

# TODO: UPDATE DATA AFTER TRANSACTIONS ARE MADE
