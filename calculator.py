def sum(a, b):
    return a + b

def realDivi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: division by zero"

def sub(a, b):
    return a - b

def pow(a, b):
    return a ** b


def menu():
    print("Choose an operation:")
    print("1. sum(a, b)")
    print("2. realDivi(a, b)")
    print("3. sub(a, b)")
    print("4. pow(a, b)")

    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("Result:", sum(a, b))
    elif choice == 2:
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator (non-zero): "))
        print("Result:", realDivi(a, b))
    elif choice == 3:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("Result:", sub(a, b))
    elif choice == 4:
        a = float(input("Enter the base: "))
        b = float(input("Enter the exponent: "))
        print("Result:", pow(a, b))
    else:
        print("Invalid choice")

menu()