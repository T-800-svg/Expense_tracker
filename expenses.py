from datetime import datetime
from storage import save_data


def read_amount(prompt):
    """Keep asking until the user enters a positive number."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value > 0:
                return value
        except ValueError:
            pass
        print("Amount must be a positive number.")


def read_date(prompt):
    """Keep asking until the user enters a valid YYYY-MM-DD date (blank = today)."""
    while True:
        raw = input(prompt + " (YYYY-MM-DD, blank for today): ").strip()
        if raw == "":
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(raw, "%Y-%m-%d")
            return raw
        except ValueError:
            print("Invalid date. Use the format YYYY-MM-DD.")


def next_id(expenses):
    """Return the next unused expense ID."""
    return max((e["id"] for e in expenses), default=0) + 1


def find_expense(expenses, expense_id):
    """Return the expense with the given ID, or None."""
    for e in expenses:
        if e["id"] == expense_id:
            return e
    return None


def add_expense(expenses):
    """Ask for expense details, validate them, and save."""
    amount = read_amount("Amount: ")
    category = input("Category: ").strip().title() or "Other"
    date = read_date("Date")
    description = input("Description: ").strip()

    expense = {
        "id": next_id(expenses),
        "amount": amount,
        "category": category,
        "date": date,
        "description": description,
    }
    expenses.append(expense)
    save_data(expenses)
    print(f"[OK] Added expense #{expense['id']}")


def edit_expense(expenses, expense_id):
    """Edit an expense. Press Enter on any field to keep its current value."""
    expense = find_expense(expenses, expense_id)
    if expense is None:
        print("No expense found with that ID.")
        return

    print("Press Enter to keep the current value.")

    raw = input(f"Amount [{expense['amount']}]: ").strip()
    if raw:
        try:
            value = float(raw)
            if value > 0:
                expense["amount"] = value
            else:
                print("Amount must be positive - keeping old value.")
        except ValueError:
            print("Invalid number - keeping old value.")

    raw = input(f"Category [{expense['category']}]: ").strip()
    if raw:
        expense["category"] = raw.title()

    raw = input(f"Date [{expense['date']}]: ").strip()
    if raw:
        try:
            datetime.strptime(raw, "%Y-%m-%d")
            expense["date"] = raw
        except ValueError:
            print("Invalid date - keeping old value.")

    raw = input(f"Description [{expense['description']}]: ").strip()
    if raw:
        expense["description"] = raw

    save_data(expenses)
    print("[OK] Expense updated.")


def delete_expense(expenses, expense_id):
    """Delete an expense by ID after confirmation."""
    expense = find_expense(expenses, expense_id)
    if expense is None:
        print("No expense found with that ID.")
        return
    print(f"#{expense['id']} | Rs.{expense['amount']:,.0f} | {expense['category']} | {expense['date']} | {expense['description']}")
    if input("Delete this expense? (y/n): ").strip().lower() == "y":
        expenses.remove(expense)
        save_data(expenses)
        print("[OK] Expense deleted.")
    else:
        print("Cancelled.")