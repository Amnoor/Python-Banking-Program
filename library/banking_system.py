# Simple Banking System Module
# This module provides basic banking functionalities such as checking balance,
# depositing money, and withdrawing money.
# First I will define a variable to hold the balance.
balance = 0.00
# Next I will define functions for deposit.
def deposit(amount):
#   This function adds the specified amount to the balance.
    global balance
    balance += amount
# Next I will define a function for withdraw.
def withdraw(amount):
#   This function subtracts the specified amount from the balance if sufficient funds exist then prints the new balance, otherwise it prints "Insufficient funds".
    global balance
    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print(f"Withdrew ${amount:,.2f}")
        print(f"New balance is: ${balance:,.2f}")
# Next I will define a help function to explain the functions and variable in this module.
def help(*functions):
    for function in functions:
        print(f"{function.capitalize()}:")
        match function.lower():
            case "balance":
                print("Variable to hold the current balance.")
            case "deposit":
                print("Function to deposit an amount to the balance.")
            case "withdraw":
                print("Function to withdraw an amount from the balance.")
            case _:
                print("No help available for this Function/Variable.")
# Finally I will add a conditional to run the help function if this module is run directly.
match __name__:
    case "__main__":
        help("balance", "deposit", "withdraw")