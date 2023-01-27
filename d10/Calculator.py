# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multify
def multify(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2

symbols = {
    "+": add,
    "-": subtract,
    "*": multify,
    "/": divide
}

def calculator():
    num1 = float(input("enter the first number\n"))
    for symbol in symbols:
        print(symbol)
    end_calculation = False

    while not end_calculation:
        operation = input("pick an operation\n")
        num2 = float(input("enter the next number\n"))
        calculation_function = symbols[operation]
        answer1 = calculation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer1}")

        if_continue = input(f"Type 'y' to continue calculation with {answer1}, or type 'n' to start a new calculation. ")
        if if_continue == "y":
            num1 = answer1
        elif if_continue == "n":
            end_calculation = True
            calculator()

calculator()