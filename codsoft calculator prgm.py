def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero is not allowed.")
    else:
        print("Invalid choice. Please choose a valid operation.")

def main():
    calculator()
    while True:
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() == "yes":
            calculator()
        elif cont.lower() == "no":
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
