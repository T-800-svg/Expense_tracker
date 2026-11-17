from datetime import datetime

BAR_WIDTH = 20


def show_category_chart(expenses):
    """Text bar chart of spending per category (optionally for one month)."""
    if not expenses:
        print("No expenses to chart.")
        return

    month = input("Month YYYY-MM (blank for all time): ").strip()
    if month:
        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            print("Invalid month. Use YYYY-MM.")
            return
        expenses = [e for e in expenses if e["date"].startswith(month)]
        if not expenses:
            print("No expenses in that month.")
            return

    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    grand_total = sum(totals.values())

    print(f"\nSpending by category ({month or 'all time'})")
    print("-" * 52)
    for cat, amount in sorted(totals.items(), key=lambda kv: kv[1], reverse=True):
        pct = amount / grand_total * 100
        filled = round(pct / 100 * BAR_WIDTH)
        bar = "#" * filled + "-" * (BAR_WIDTH - filled)
        print(f"{cat:<12} {bar}  Rs.{amount:>9,.0f} ({pct:.0f}%)")
    print("-" * 52)
    print(f"{'Total':<12} {'':<{BAR_WIDTH}}  Rs.{grand_total:>9,.0f}")