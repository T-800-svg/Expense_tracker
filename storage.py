import json
import os
import shutil
from datetime import datetime

DATA_FILE = "data.json"


def load_json(path, default):
    """Read a JSON file. If it is corrupted, try the backup (.bak) file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        backup = path + ".bak"
        if os.path.exists(backup):
            try:
                with open(backup, "r", encoding="utf-8") as f:
                    data = json.load(f)
                print(f"[WARN] {path} was missing - restored from backup")
                return data
            except json.JSONDecodeError:
                pass
        return default
    except json.JSONDecodeError:
        backup = path + ".bak"
        if os.path.exists(backup):
            try:
                with open(backup, "r", encoding="utf-8") as f:
                    data = json.load(f)
                print(f"[WARN] {path} was corrupted - restored from backup")
                return data
            except json.JSONDecodeError:
                pass
        print(f"[WARN] {path} was corrupted and no backup worked - starting empty")
        return default


def save_json(path, data, backup=False):
    """Write data to a JSON file, optionally copying the old file to .bak first."""
    if backup and os.path.exists(path):
        shutil.copy(path, path + ".bak")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_data():
    """Load all expenses and print a short startup summary."""
    expenses = load_json(DATA_FILE, [])
    month = datetime.now().strftime("%Y-%m")
    month_total = sum(e["amount"] for e in expenses if e["date"].startswith(month))
    print(f"[OK] Loaded {len(expenses)} expenses | This month: Rs.{month_total:,.0f}")
    return expenses


def save_data(expenses):
    """Save all expenses (with automatic backup)."""
    save_json(DATA_FILE, expenses, backup=True)