import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    """
    Load expenses from JSON file.
    Returns an empty list if the file doesn't exist or is empty.
    """

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(expenses):
    """
    Save expenses to JSON file.
    """

    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)