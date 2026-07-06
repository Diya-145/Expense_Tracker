from colorama import Fore, init

from storage import load_expenses

from expense_manager import (
    add_expense,
    view_expenses,
    delete_expense,
    search_expense,
    show_statistics,
    export_csv
)

# Initialize Colorama
init(autoreset=True)

# Load saved expenses
expenses = load_expenses()

while True:

    print(Fore.CYAN + "\n" + "=" * 45)
    print(Fore.GREEN + "         EXPENSE TRACKER")
    print(Fore.CYAN + "=" * 45)

    print(Fore.YELLOW + "1. Add Expense")
    print(Fore.YELLOW + "2. View Expenses")
    print(Fore.YELLOW + "3. Search Expense")
    print(Fore.YELLOW + "4. Delete Expense")
    print(Fore.YELLOW + "5. Statistics")
    print(Fore.YELLOW + "6. Export CSV")
    print(Fore.YELLOW + "7. Exit")

    print(Fore.CYAN + "=" * 45)

    choice = input(Fore.WHITE + "Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        search_expense(expenses)

    elif choice == "4":
        delete_expense(expenses)

    elif choice == "5":
        show_statistics(expenses)

    elif choice == "6":
        export_csv(expenses)

    elif choice == "7":
        print(Fore.MAGENTA + "\n👋 Thank you for using Expense Tracker!")
        break

    else:
        print(Fore.RED + "\n❌ Invalid Choice! Please try again.")