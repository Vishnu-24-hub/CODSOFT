while True:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    print("Choose operation:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    op = input("Enter your choice: ")
    if op == "+":
        res = n1 + n2
    elif op == "-":
        res = n1 - n2
    elif op == "*":
        res = n1 * n2
    elif op == "/":
        if n2 == 0:
            print("Cannot divide by zero")
            res = None
        else:
            res = n1 / n2
    else:
        print("Invalid operation")
        res = None
    if res is not None:
        print("Answer is:", res)
    choice = input("Do you want to calculate more? (yes/no): ")
    if choice.lower() != "yes":
        print("Calculator stopped")
        break
