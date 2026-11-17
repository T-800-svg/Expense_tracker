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


def filter_expenses(expenses):
    pass


def get_monthly_total(expenses, month):
    pass

print("hehe")