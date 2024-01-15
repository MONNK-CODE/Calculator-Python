#!/usr/bin/env python
# coding: utf-8

# In[1]:


exit_loop = False

while not exit_loop:
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator...")
        exit_loop = True
    elif choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == '1':
            result = num1 + num2
            operation = 'Addition'
            symbol = '+'
        elif choice == '2':
            result = num1 - num2
            operation = 'Subtraction'
            symbol = '-'
        elif choice == '3':
            result = num1 * num2
            operation = 'Multiplication'
            symbol = '*'
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                operation = 'Division'
                symbol = '/'
            else:
                print("Error: Cannot divide by zero!")
                continue

        print(f"{operation} Result: {num1} {symbol} {num2} = {result:.2f}")

        while True:
            continue_option = input("Do you want to continue using the calculator? (yes/no): ")
            if continue_option == 'yes':
                break
            elif continue_option == 'no':
                print("Exiting the calculator...")
                exit_loop = True
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
    else:
        print("Invalid choice. Please select a valid option (1-5).")


# 
