import csv
import os
import calendar
from datetime import datetime
from reports import filter_expenses
from storage import save_data

EXPORT_DIR = "exports"
FIELDS = ["id", "amount", "category", "date", "description"]


def valid_month(text):
    """True if text is a valid 'YYYY-MM' month."""
    try:
        datetime.strptime(text, "%Y-%m")
        return True
    except ValueError:
        return False


def write_csv(expenses, month=None, category=None):
    """Write expenses (optionally one month and/or category) to exports/."""
    rows = filter_expenses(expenses, category=category)
    if month:
        rows = [e for e in rows if e["date"].startswith(month)]
    if not rows:
        print("Nothing to export.")
        return

    os.makedirs(EXPORT_DIR, exist_ok=True)
    label = month or "all"
    if category:
        label += "_" + category.lower()
    path = os.path.join(EXPORT_DIR, f"expenses_{label}.csv")

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"[OK] Exported {len(rows)} expense(s) to {path}")


def export_csv(expenses, month=None):
    """Export / import menu (this is what main.py calls)."""
    print("\n1. Export expenses to CSV")
    print("2. Monthly report (.txt)")
    print("3. Import expenses from CSV")
    choice = input("Choose: ").strip()

    if choice == "1":
        raw = input("Month YYYY-MM (blank for all): ").strip()
        if raw and not valid_month(raw):
            print("Invalid month. Use YYYY-MM.")
            return
        category = input("Category (blank for all): ").strip() or None
        write_csv(expenses, raw or None, category)
    elif choice == "2":
        raw = input("Month YYYY-MM: ").strip()
        if not valid_month(raw):
            print("Invalid month. Use YYYY-MM.")
            return
        export_report(expenses, raw)
    elif choice == "3":
        import_csv(expenses, input("CSV file path: ").strip())
    else:
        print("Invalid choice.")


def export_report(expenses, month):
    pass


def import_csv(expenses, path):
    pass