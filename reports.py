from datetime import datetime


def print_table(rows):
    """Print expenses as an aligned table with a total."""
    if not rows:
        print("No expenses found.")
        return
    print(f"\n{'ID':<5}{'Date':<12}{'Category':<14}{'Amount':>12}  Description")
    print("-" * 62)
    for e in rows:
        print(f"{e['id']:<5}{e['date']:<12}{e['category']:<14}{e['amount']:>12,.2f}  {e['description']}")
    print("-" * 62)
    total = sum(e["amount"] for e in rows)
    print(f"{len(rows)} expense(s) | Total: Rs.{total:,.2f}")


def view_expenses(expenses):
    """Show all expenses, newest first."""
    print_table(sorted(expenses, key=lambda e: e["date"], reverse=True))


def ask_float(prompt):
    """Return a float, or None if left blank or invalid."""
    raw = input(prompt).strip()
    if raw == "":
        return None
    try:
        return float(raw)
    except ValueError:
        print("Ignored: not a number.")
        return None


def ask_date(prompt):
    """Return a YYYY-MM-DD string, or None if left blank or invalid."""
    raw = input(prompt + " (YYYY-MM-DD, blank to skip): ").strip()
    if raw == "":
        return None
    try:
        datetime.strptime(raw, "%Y-%m-%d")
        return raw
    except ValueError:
        print("Ignored: invalid date.")
        return None


def filter_expenses(expenses, category=None, start=None, end=None,
                    min_amount=None, max_amount=None, keyword=None):
    """Return expenses matching every filter that is given."""
    result = []
    for e in expenses:
        if category and e["category"].lower() != category.lower():
            continue
        if start and e["date"] < start:
            continue
        if end and e["date"] > end:
            continue
        if min_amount is not None and e["amount"] < min_amount:
            continue
        if max_amount is not None and e["amount"] > max_amount:
            continue
        if keyword and keyword.lower() not in (e["description"] + " " + e["category"]).lower():
            continue
        result.append(e)
    return result


def view_expenses(expenses):
    """Menu: view all, sort, or search/filter."""
    print("\n1. View all (newest first)")
    print("2. Sort by a column")
    print("3. Search / filter")
    choice = input("Choose: ").strip()

    if choice == "1":
        print_table(sorted(expenses, key=lambda e: e["date"], reverse=True))
    elif choice == "2":
        print("Sort by: 1 Date  2 Amount  3 Category  4 ID")
        picked = SORT_KEYS.get(input("Choose: ").strip())
        if picked is None:
            print("Invalid choice.")
            return
        descending = input("Descending? (y/n): ").strip().lower() == "y"
        print_table(sort_expenses(expenses, picked[0], descending))
    elif choice == "3":
        rows = filter_expenses(
            expenses,
            category=input("Category (blank to skip): ").strip() or None,
            start=ask_date("From date"),
            end=ask_date("To date"),
            min_amount=ask_float("Min amount (blank to skip): "),
            max_amount=ask_float("Max amount (blank to skip): "),
            keyword=input("Keyword (blank to skip): ").strip() or None,
        )
        print_table(rows)
    else:
        print("Invalid choice.")


SORT_KEYS = {
    "1": ("date", "Date"),
    "2": ("amount", "Amount"),
    "3": ("category", "Category"),
    "4": ("id", "ID"),
}


def sort_expenses(rows, key, descending=False):
    """Return the rows sorted by the given field."""
    return sorted(rows, key=lambda e: e[key], reverse=descending)


def get_monthly_total(expenses, month):
    """Total spent in a month given as 'YYYY-MM'."""
    return sum(e["amount"] for e in expenses if e["date"].startswith(month))