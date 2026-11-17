import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero."
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#Calculator Memory
memory = 0
history = []

def memory_add(value):
    global memory
    memory += value
    return memory

def memory_subtract(value):
    global memory
    memory -= value
    return memory

def memory_recall():
    return memory

def memory_clear():
    global memory
    memory = 0
    return memory

def calculator():
    global memory
    print(art.logo)
    should_accumulate = True

    try:
        num1 = float(input("What is the first number?: "))
    except ValueError:
        print("Invalid input, please enter a number.")
        calculator()
        return


    while should_accumulate:
        for symbol in operations:
            print(symbol)

        print("M+ : Add current number to memory")
        print("M- : Subtract current number from memory")
        print("MR : Recall memory")
        print("MC : Clear memory")
        print("H : View calculation history")
        print("CH : Clear calculation history")
        operation_symbol = input("Pick an operation: ")

        if operation_symbol == "M+":
            memory_add(num1)
            print("Memory:", memory)
            continue

        elif operation_symbol == "M-":
            memory_subtract(num1)
            print("Memory:", memory)
            continue

        elif operation_symbol == "MR":
            num1 = memory_recall()
            print("Memory recalled:", num1)
            continue

        elif operation_symbol == "MC":
            memory_clear()
            print("Memory cleared")
            continue

        elif operation_symbol == "H":
            if history:
                print("\nCalculation History:")
                for calculation in history:
                    print(calculation)
            else:
                print("No calculation history available.")
            continue

        elif operation_symbol == "CH":
            history.clear()
            print("Calculation history cleared ")
            continue

        if operation_symbol not in operations:
            print("Invalid input, please enter a valid operation")
            continue
        try:
            num2 = float(input("What is the next number?: "))
        except ValueError:
            print("Invalid input, please enter a number")
            continue
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if isinstance(answer, (int, float)):
            history.append(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'q' to quit: ").lower()

        if choice == "y":
            if isinstance(answer, (int, float)):
                num1 = answer
            else:
                print("Please start a new calculation.")

        elif choice == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()

        elif choice == "q":
            print("Thank you for using the calculator.")
            return

        else:
            print("Invalid input, please enter y, n or q.")


calculator()



