#=============================================================
# Simple Calculator
# language: Python
#==========================================================
while True: 
  print("======== Simple Calculator ========")

  try:

    num1 = float(input("Enter first number: "))
 
    operator = input("Enter operator (+, -, *, /): ")

    num2 = float(input("Enter second number: "))


    if operator == '+':
        result = num1 + num2

    elif operator == '-':
        result = num1 - num2

    elif operator == '*':
        result = num1 * num2

    elif operator == '/':

        if num2 != 0:
            result = num1 / num2

        else:
            result = "Error! Division by zero."

    else:
        result = "Invalid operator!"


    print("Result:", result)


  except ValueError:
    print("Invalid input! Please enter numbers.")