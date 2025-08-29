"""
Personal Expense Tracker
-------------------------
This program allows users to log daily expenses, view summaries, and track spending.
It demonstrates use of:
- Data Structures (list of dictionaries)
- File Handling (JSON)
- Basic Data Analysis (summaries by category/date)
"""

import json
from datetime import datetime

# -----------------------------
# File name for saving data
FILE_NAME = "expenses.json"

# -----------------------------
# Load expenses from file
def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []   # if no file exists yet, return empty list
    except json.JSONDecodeError:
        return []   # if file is empty or corrupted

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

# -----------------------------
# Add a new expense
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food/Transport/Entertainment/etc.): ").title()
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

        # Default: today’s date
        date = date_input if date_input else datetime.now().strftime("%Y-%m-%d")

        # Create dictionary for expense
        expense = {"amount": amount, "category": category, "date": date}

        # Append to list
        expenses.append(expense)
        save_expenses(expenses)  # persist data immediately
        print("✅ Expense added successfully!\n")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.\n")

# -----------------------------
# View total overall spending
def total_spending(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Overall Spending: {total:.2f}")

# View spending by category
def spending_by_category(expenses):
    category = input("Enter category to check: ").title()
    total = sum(exp["amount"] for exp in expenses if exp["category"] == category)
    print(f"📊 Total spending on {category}: {total:.2f}")

# View spending by date
def spending_by_date(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    total = sum(exp["amount"] for exp in expenses if exp["date"] == date)
    print(f"📅 Total spending on {date}: {total:.2f}")

# View all summaries
def view_summary(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return
    
    # Overall total
    total_spending(expenses)

    # Per-category breakdown
    print("\n📊 Spending by Category:")
    category_summary = {}
    for exp in expenses:
        category_summary[exp["category"]] = category_summary.get(exp["category"], 0) + exp["amount"]
    for cat, amt in category_summary.items():
        print(f"- {cat}: {amt:.2f}")

    # Per-date breakdown
    print("\n📅 Spending by Date:")
    daily_summary = {}
    for exp in expenses:
        daily_summary[exp["date"]] = daily_summary.get(exp["date"], 0) + exp["amount"]
    for dt, amt in daily_summary.items():
        print(f"- {dt}: {amt:.2f}")

# -----------------------------
# Main menu
def main():
    expenses = load_expenses()   # Load existing data at start

    while True:
        print("\n==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. View Spending by Category")
        print("4. View Spending by Date")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            spending_by_category(expenses)
        elif choice == "4":
            spending_by_date(expenses)
        elif choice == "5":
            print("Exiting... Data saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# -----------------------------
if __name__ == "__main__":
    main()
