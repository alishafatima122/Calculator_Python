# ============================================
# Project: Calculator with File Handling
# Language: Python
# ============================================

history = []


# Load previous history
try:
    with open("history.txt", "r") as file:
        for line in file:
            history.append(line.strip())

except FileNotFoundError:
    with open("history.txt", "w"):
        pass


# Save history to file
def save_history(operation):

    with open("history.txt", "a") as file:
        file.write(operation + "\n")


# View history
def display_history():

    if history:
        print("\nCalculation History:")

        for entry in history:
            print(entry)

    else:
        print("No history available.")


# Addition
def add_numbers(a, b):

    result = a + b

    operation = f"{a} + {b} = {result}"

    history.append(operation)
    save_history(operation)

    return result


# Subtraction
def subtract_numbers(a, b):

    result = a - b

    operation = f"{a} - {b} = {result}"

    history.append(operation)
    save_history(operation)

    return result


# Multiplication
def multiply_numbers(a, b):

    result = a * b

    operation = f"{a} * {b} = {result}"

    history.append(operation)
    save_history(operation)

    return result


# Division
def divide_numbers(a, b):

    if b == 0:
        return "Error: Division by zero is not allowed."

    result = a / b

    operation = f"{a} / {b} = {result}"

    history.append(operation)
    save_history(operation)

    return result


# Main Program
while True:

    print("\n================ Calculator ================")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")


    try:
        choice = int(input("Enter choice (1-7): "))

    except ValueError:
        print("Invalid input!")
        continue


    if choice == 7:
        print("Thank you for using Calculator!")
        break


    elif choice == 5:
        display_history()


    elif choice == 6:

        history.clear()

        with open("history.txt", "w"):
            pass

        print("History cleared!")


    elif choice in (1, 2, 3, 4):

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        except ValueError:
            print("Please enter valid numbers.")
            continue


        if choice == 1:
            result = add_numbers(num1, num2)

        elif choice == 2:
            result = subtract_numbers(num1, num2)

        elif choice == 3:
            result = multiply_numbers(num1, num2)

        elif choice == 4:
            result = divide_numbers(num1, num2)


        print("Result:", result)


    else:
        print("Invalid choice!")