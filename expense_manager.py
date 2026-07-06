from storage import save_expenses
from colorama import Fore
import csv


def add_expense(expenses):

    description = input("Enter Description: ").strip()

    if description == "":
        print(Fore.RED + "Description cannot be empty!")
        return

    print("\nSelect Category")
    print("1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Bills")
    print("5. Others")

    choice = input("Choose Category: ")

    category = {
        "1": "Food",
        "2": "Travel",
        "3": "Shopping",
        "4": "Bills",
        "5": "Others"
    }.get(choice, "Others")

    while True:
        try:
            amount = float(input("Enter Amount (₹): "))

            if amount <= 0:
                print(Fore.RED + "Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print(Fore.RED + "Please enter a valid amount.")

    date = input("Enter Date (DD/MM/YYYY): ")

    expenses.append({
        "description": description,
        "category": category,
        "amount": amount,
        "date": date
    })

    save_expenses(expenses)

    print(Fore.GREEN + "\n✅ Expense Added Successfully!")


def view_expenses(expenses):

    if not expenses:
        print(Fore.RED + "\nNo Expenses Found.")
        return

    print(Fore.CYAN + "\n" + "=" * 80)
    print(f"{'ID':<5}{'Category':<15}{'Amount':<12}{'Date':<15}Description")
    print(Fore.CYAN + "=" * 80)

    for i, expense in enumerate(expenses, start=1):

        print(
            f"{i:<5}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:<11.2f}"
            f"{expense['date']:<15}"
            f"{expense['description']}"
        )

    print(Fore.CYAN + "=" * 80)


def delete_expense(expenses):

    if not expenses:
        print(Fore.RED + "\nNo Expenses Available.")
        return

    view_expenses(expenses)

    try:

        num = int(input("\nEnter Expense ID to Delete: "))

        if 1 <= num <= len(expenses):

            removed = expenses.pop(num - 1)

            save_expenses(expenses)

            print(
                Fore.GREEN +
                f"\nDeleted: {removed['description']}"
            )

        else:

            print(Fore.RED + "Invalid Expense ID.")

    except ValueError:

        print(Fore.RED + "Enter a valid number.")


def search_expense(expenses):

    keyword = input("\nEnter keyword: ").lower()

    found = False

    for i, expense in enumerate(expenses, start=1):

        if keyword in expense["description"].lower():

            print(
                f"{i}. "
                f"{expense['category']} | "
                f"₹{expense['amount']:.2f} | "
                f"{expense['date']} | "
                f"{expense['description']}"
            )

            found = True

    if not found:
        print(Fore.RED + "No matching expense found.")


def show_statistics(expenses):

    if not expenses:
        print(Fore.RED + "\nNo Expenses Found.")
        return

    total = sum(expense["amount"] for expense in expenses)

    highest = max(expense["amount"] for expense in expenses)

    lowest = min(expense["amount"] for expense in expenses)

    average = total / len(expenses)

    print(Fore.CYAN + "\n" + "=" * 35)
    print(Fore.GREEN + "      EXPENSE SUMMARY")
    print(Fore.CYAN + "=" * 35)

    print(Fore.YELLOW + f"Total Expenses : {len(expenses)}")
    print(Fore.YELLOW + f"Total Amount   : ₹{total:.2f}")
    print(Fore.GREEN + f"Highest Expense: ₹{highest:.2f}")
    print(Fore.RED + f"Lowest Expense : ₹{lowest:.2f}")
    print(Fore.CYAN + f"Average Expense: ₹{average:.2f}")

    print(Fore.CYAN + "=" * 35)


def export_csv(expenses):

    with open("expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Description",
            "Category",
            "Amount",
            "Date"
        ])

        for expense in expenses:

            writer.writerow([
                expense["description"],
                expense["category"],
                expense["amount"],
                expense["date"]
            ])

    print(Fore.GREEN + "\n✅ Expenses exported to expenses.csv")