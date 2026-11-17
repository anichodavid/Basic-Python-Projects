# Define the four functions
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return None
    return a / b


#Create a smal function to display options
def show_menu():
    print("\n ---Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")



while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Goodbye! 👋")
        break

    if choice not in ("1", "2", "3", "4"):
        print("⚠️ Invalid choice. Try again.")
        continue



#try/except catches cases where users type letters-prevents a crash
#continue restarts the loop
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("⚠️ Please enter valid numbers.")
        continue

    if choice == "1":
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == "4":
        result = divide(num1, num2)
        if result is None:
            print("⚠️ Cannot divide by zero.")
        else:
            print(f"Result: {num1} ÷ {num2} = {result}")


