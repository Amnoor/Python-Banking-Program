# **Python Banking Program**

A simple console-based banking system implemented in Python that allows users to perform basic financial operations including balance checks, deposits, and withdrawals.


### **Overview**

This project consists of two main components:
- Core Banking Module (library/banking_system.py): Handles the financial operations and business logic
- Interactive Console Program (Banking Program.py): Provides a user-friendly interface for interacting with the banking system


### **Features**

- **Balance Management:** Track and display current account balance
- **Deposit Functionality:** Add funds to your account with immediate balance updates
- **Withdrawal System:** Remove funds with validation for sufficient balance
- **User-Friendly Interface:** Simple text-based menu system
- **Input Validation:** Handles invalid inputs and provides helpful error messages
- **Help System:** Built-in documentation for all available functions


### **Usage**

1. Run the main program: 'python "Banking Program.py"'
2. Follow the on-screen prompts:
    - Type balance to check your current balance
    - Type deposit to add money to your account
    - Type withdraw to remove money from your account
    - Type e to exit the program
3. The program will guide you through each transaction with clear instructions


### **Requirements**

- Python 3.10 or higher (for match-case statement support)
- No external dependencies required


### **Technical Details**

The banking system uses a global balance variable and provides three main functions:

- deposit(amount): Adds specified amount to balance
- withdraw(amount): Subtracts amount if sufficient funds exist
- help(): Provides documentation for available functions

The interactive program features a continuous loop that processes user commands using modern match-case statements for clean control flow.

This project demonstrates core Python concepts including modules, functions, global variables, and user input handling while providing practical banking functionality.