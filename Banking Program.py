# Banking Program
# This program allows users to check their balance, deposit money, and withdraw money using the banking
# functionalities provided in the banking_system module.
# First I will import the banking_system module.
import library.banking_system as system
# Next I will create a simple user interface to interact with the banking system.
print("Welcome to our Banking Program!")
# Next I will create a loop to continuously prompt the user for input until they choose to exit.
is_running = True
while is_running:
#   Prompt the user for input, and handle the input using .strip() and .lower() to standardize it.
    user_input = input("Enter either balance, deposit, or withdraw (e to exit): ").strip().lower()
#   Use a match-case statement to handle the different user inputs.
    match user_input:
#       if the user inputs "balance", print the current balance.
        case "balance":
            print(f"Your current balance is: ${system.balance:,.2f}")
#       if the user inputs "deposit", prompt for an amount to deposit, call the deposit function, and print the new balance.
        case "deposit":
            amount = float(input("Enter the amount to deposit: $"))
            system.deposit(amount)
            print(f"Deposited ${amount:,.2f}")
            print(f"New balance is: ${system.balance:,.2f}")
#       if the user inputs "withdraw", prompt for an amount to withdraw, call the withdraw function.
        case "withdraw":
            amount = float(input("Enter the amount to withdraw: $"))
            system.withdraw(amount)
#       if the user inputs "e", print a goodbye message and set is_running to False to exit the loop.
        case "e":
            print("Thank you for using our Banking Program. Goodbye!")
            is_running = False
#       for any other input, print an error message and prompt again.
        case _:
            print("Invalid input. Please try again.")