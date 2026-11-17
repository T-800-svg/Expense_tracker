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
    """Write a formatted monthly report to exports/report_YYYY-MM.txt."""
    rows = [e for e in expenses if e["date"].startswith(month)]
    if not rows:
        print(f"No expenses found for {month}.")
        return

    year, mon = map(int, month.split("-"))
    now = datetime.now()
    if (year, mon) == (now.year, now.month):
        days = now.day
    else:
        days = calendar.monthrange(year, mon)[1]

    total = sum(e["amount"] for e in rows)
    totals = {}
    for e in rows:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    top3 = sorted(rows, key=lambda e: e["amount"], reverse=True)[:3]
    title = datetime.strptime(month, "%Y-%m").strftime("%B %Y").upper()

    lines = [
        f"===== MONTHLY REPORT: {title} =====",
        f"Total spent:   Rs.{total:,.0f}",
        f"Daily average: Rs.{total / days:,.0f}",
        "",
        f"{'Category':<14}{'Amount':>12}{'Share':>8}",
    ]
    for cat, amount in sorted(totals.items(), key=lambda kv: kv[1], reverse=True):
        lines.append(f"{cat:<14}{'Rs.' + format(amount, ',.0f'):>12}{amount / total * 100:>7.0f}%")
    lines += ["", "Top 3 expenses:"]
    for i, e in enumerate(top3, 1):
        lines.append(f"{i}. {e['description'] or e['category']:<20} Rs.{e['amount']:,.0f}")

    os.makedirs(EXPORT_DIR, exist_ok=True)
    path = os.path.join(EXPORT_DIR, f"report_{month}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"[OK] Report saved to {path}")


def import_csv(expenses, path):
    """Import expenses from a CSV with columns: amount, category, date, description."""
    try:
        f = open(path, "r", newline="", encoding="utf-8-sig")
    except FileNotFoundError:
        print("File not found.")
        return

    added = skipped = 0
    next_id = max((e["id"] for e in expenses), default=0) + 1
    with f:
        for row in csv.DictReader(f):
            try:
                amount = float(row["amount"])
                datetime.strptime(row["date"], "%Y-%m-%d")
                if amount <= 0:
                    raise ValueError
            except (KeyError, ValueError, TypeError):
                skipped += 1
                continue
            expenses.append({
                "id": next_id,
                "amount": amount,
                "category": (row.get("category") or "Other").strip().title(),
                "date": row["date"],
                "description": (row.get("description") or "").strip(),
            })
            next_id += 1
            added += 1

    if added:
        save_data(expenses)
    print(f"[OK] Imported {added} expense(s), skipped {skipped} invalid row(s).")