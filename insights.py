from datetime import datetime


def prev_month_key(now):
    """Return last month as 'YYYY-MM'."""
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def show_insights(expenses):
    """Show spending insights for the current month."""
    if not expenses:
        print("No expenses yet.")
        return

    now = datetime.now()
    month = now.strftime("%Y-%m")
    current = [e for e in expenses if e["date"].startswith(month)]
    if not current:
        print(f"No expenses recorded for {month} yet.")
        return

    totals = {}
    for e in current:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    top_cat, top_amount = max(totals.items(), key=lambda kv: kv[1])
    total = sum(totals.values())
    daily_avg = total / now.day

    prev_total = sum(e["amount"] for e in expenses if e["date"].startswith(prev_month_key(now)))
    if prev_total == 0:
        change = "no data for last month"
    else:
        diff = (total - prev_total) / prev_total * 100
        change = f"{abs(diff):.0f}% {'more' if diff >= 0 else 'less'} than last month"

    top3 = sorted(current, key=lambda e: e["amount"], reverse=True)[:3]

    print(f"\n===== INSIGHTS: {month} =====")
    print(f"Total spent:      Rs.{total:,.0f}")
    print(f"Top category:     {top_cat} (Rs.{top_amount:,.0f})")
    print(f"Daily average:    Rs.{daily_avg:,.0f}")
    print(f"vs last month:    {change}")
    print("Top 3 expenses:")
    for i, e in enumerate(top3, 1):
        print(f"  {i}. {e['description'] or e['category']:<20} Rs.{e['amount']:,.0f}")