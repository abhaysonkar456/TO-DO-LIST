import math
history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error: division by zero"
    return a / b

def square(a):
    return a ** 2

def square_root(a):
    if a < 0:
        return "error : value is negetive"
    return math.sqrt(a)

def show_history():
    if not history:
        print("no operation performed yet")
    else:
        print("opreation history")
        for item in history:
            print(item)

def get_number(prompt):
    while True:
        try:
         return float(input(prompt))
        except ValueError:
            print("invalid input, please enter a valid number")

def calculator():
    while True:
        print("\nChoose opreation")
        print("1. Add(+)")
        print("2. subtract(-)")
        print("3. multiply(*)")
        print("4. divide(/)")
        print("5. square(a²)")
        print("6. square root")
        print("7. show history")
        print("8. exit")
        choice = input("enter operation(1 to 8: )")

        if choice == '1':
            a = get_number("enter first number: ")
            b = get_number("enter second number: ")
            result = a + b
            history.append(f"{a} + {b} = {result}")
            print("result: ", result)

        elif choice == '2':
            a = get_number("enter first number: ")
            b = get_number("enter second number: ")
            result = a - b
            history.append(f"{a} - {b} = {result}")
            print("result: ", result)

        elif choice == '3':
            a = get_number("enter first number: ")
            b = get_number("enter second number: ")
            result = a * b
            history.append(f"{a} * {b } = {result}")
            print("result: ", result)

        elif choice == '4':
            a = get_number("enter first number: ")
            b = get_number("enter second number: ")
            result = a / b
            history.append(f"{a} / {b}= {result}")
            print("result: ", result)

        elif choice == '5':
            a = get_number("enter a number: ")
            result = square(a)
            history.append(f"{a}²= {result}")
            print("result: ", result)

        elif choice == '6':
            a = get_number("enter a number: ")
            result = square_root(a)
            history.append(f"√{a} = {result}")
            print("result: ", result)

        elif choice == '7':
            show_history()

        elif choice == '8':
            print("Goodbye")
            break

        else:
            print("invalid choice! please enter a number between 1 - 8")

calculator()