from datetime import datetime
from storage import load_json, save_json

BUDGET_FILE = "budget.json"


def set_budget(category, limit):
    """Set a monthly budget limit for a category."""
    category = category.strip().title()
    if not category or limit <= 0:
        print("Enter a category name and a positive limit.")
        return
    budgets = load_json(BUDGET_FILE, {})
    budgets[category] = limit
    save_json(BUDGET_FILE, budgets)
    print(f"[OK] Budget for {category} set to Rs.{limit:,.0f} per month")


def check_budget(expenses, only_alerts=False):
    """Compare this month's spending with each budget. Warn at 80%, flag when over."""
    budgets = load_json(BUDGET_FILE, {})
    if not budgets:
        if not only_alerts:
            print("No budgets set yet.")
        return

    month = datetime.now().strftime("%Y-%m")
    spent = {}
    for e in expenses:
        if e["date"].startswith(month):
            cat = e["category"].title()
            spent[cat] = spent.get(cat, 0) + e["amount"]

    for cat, limit in budgets.items():
        used = spent.get(cat, 0)
        pct = used / limit * 100
        if used > limit:
            print(f"[OVER] {cat}: Rs.{used:,.0f} of Rs.{limit:,.0f} spent - OVER BUDGET by Rs.{used - limit:,.0f}")
        elif pct >= 80:
            print(f"[WARN] {cat}: Rs.{used:,.0f} of Rs.{limit:,.0f} spent ({pct:.0f}%) - nearing your limit")
        elif not only_alerts:
            print(f"[OK] {cat}: Rs.{used:,.0f} of Rs.{limit:,.0f} spent ({pct:.0f}%)")