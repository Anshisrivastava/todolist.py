def add(a,b):
    return a+b
def subtract(a,b):
    return(a-b)
def multipy(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)
def calculator():
    print("Welcome to the Calculator App!")

    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice =='2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multipy(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the scond number: "))
            if num2 == 0:
                print("Error : Division bt zero")
            else:
                result = divide(num1, num2) 
                print(f"Result : {num1} / {num2} = {result}")
        elif choice == '5':
            print("Thank you for using the Calculator App!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

        if __name__ == "__main__":
            calculator()