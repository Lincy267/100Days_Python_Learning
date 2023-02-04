import data

coffee_machine_off = False
total_coins = 0
total_revenue = 0
change = 0
coffee_resources = 0

def receive_coins():
    print("Please insert coins.")
    quarters_inserted = float(input("how many quarters? ")) * 0.25
    dimes_inserted = float(input("how many dimes? ")) * 0.1
    nickles_inserted = float(input("how many nickles? ")) * 0.05
    pennies_inserted = float(input("how many pennies? ")) * 0.01
    coins_inserted = [quarters_inserted, dimes_inserted, nickles_inserted, pennies_inserted]
    total_coins = round(sum(coins_inserted),2)
    return total_coins

def get_cost():
    if coffee_type in data.MENU:
        cost_of_coffee = float(data.MENU[coffee_type]["cost"])
        return cost_of_coffee



def report():
    print(f"Water: {resources_left['water']}ml")
    print(f"Milk: {resources_left['milk']}ml")
    print(f"Coffee: {resources_left['coffee']}g")
    print(f"Money: ${total_revenue}")


def transactions(cost_of_coffee, total_coins, total_revenue):
    if cost_of_coffee > total_coins:
        print("Sorry that's not enough money. Money refunded.")
        return total_revenue
    else:
        resources_left = make_coffee(coffee_type, coffee_resources)
        change = round(total_coins - cost_of_coffee, 2)
        print(f"${total_coins} received.\nHere is ${change} in change.\nHere is your {coffee_type}. Enjoy!")
        revenue = total_coins - change
        total_revenue += revenue
        return total_revenue


def make_coffee(coffee_type, coffee_resources):
    ingredients = data.MENU[coffee_type]["ingredients"]
    enough_resources = True
    for ingredient, amount in ingredients.items():
        if resources_left[ingredient] < amount:
            print(f"Sorry, we don't have enough {ingredient} to make a {coffee_type}. ")
            enough_resources = False
            return enough_resources
        else:
            resources_left[ingredient] -= amount
    return enough_resources


while not coffee_machine_off:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    resources_left = data.resources
    if coffee_type in data.MENU:
        flag = False
        while not flag:
            if not make_coffee(coffee_type, coffee_resources):
                coffee_type = input(
                    "What would you like? (espresso/latte/cappuccino): ").lower()
            else:
                flag = True
                total_coins = receive_coins()
                cost_of_coffee = get_cost()
                total_revenue = transactions(cost_of_coffee, total_coins, total_revenue)

    elif coffee_type == "report":
            report()
    else:
            print("INVALID INPUT")
            coffee_machine_off = True

# TODO: bug: make_coffee run twice

