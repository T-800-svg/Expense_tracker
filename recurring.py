from datetime import datetime
from storage import load_json, save_json, save_data
from expenses import read_amount, next_id

RECURRING_FILE = "recurring.json"


def add_recurring(expenses):
    """Define a monthly recurring expense (rent, subscription, Wi-Fi...)."""
    amount = read_amount("Monthly amount: ")
    category = input("Category: ").strip().title() or "Other"
    description = input("Description (e.g. Rent): ").strip()

    while True:
        raw = input("Day of month it is charged (1-28): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= 28:
            day = int(raw)
            break
        print("Enter a number from 1 to 28.")

    items = load_json(RECURRING_FILE, [])
    items.append({
        "amount": amount,
        "category": category,
        "description": description,
        "day": day,
        "last_generated": "",
    })
    save_json(RECURRING_FILE, items)
    print("[OK] Recurring expense saved.")
    generate_recurring(expenses)


def generate_recurring(expenses):
    """Add this month's expense for every recurring item that has not been added yet."""
    items = load_json(RECURRING_FILE, [])
    month = datetime.now().strftime("%Y-%m")
    created = 0

    for item in items:
        if item["last_generated"] == month:
            continue
        expenses.append({
            "id": next_id(expenses),
            "amount": item["amount"],
            "category": item["category"],
            "date": f"{month}-{item['day']:02d}",
            "description": item["description"] + " (recurring)",
        })
        item["last_generated"] = month
        created += 1

    if created:
        save_json(RECURRING_FILE, items)
        save_data(expenses)
        print(f"[OK] Added {created} recurring expense(s) for {month}")