import math

def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    """This function returns the modulus of two numbers"""
    return x % y

def exponentiate(x, y):
    """This function raises x to the power of y"""
    return x ** y

def square_root(x):
    """This function returns the square root of a number"""
    if x < 0:
        return "Error! Square root of a negative number."
    return math.sqrt(x)

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Square Root")

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4/5/6/7): ")

        # Check if the choice is one of the seven options
        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            if choice == '7':
                num = float(input("Enter number: "))
                print(f"Square root of {num} = {square_root(num)}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")

                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")

                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")

                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")

                elif choice == '5':
                    print(f"{num1} % {num2} = {modulus(num1, num2)}")

                elif choice == '6':
                    print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")
            
            # Ask if the user wants to do another calculation
            # Break the while loop if answer is no
            next_calculation = input("Do you want to do another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

calculator()
