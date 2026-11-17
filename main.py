from storage import load_data, save_data
from expenses import add_expense, edit_expense, delete_expense
from budget import set_budget, check_budget
from recurring import add_recurring, generate_recurring
from reports import view_expenses
from charts import show_category_chart
from insights import show_insights
from export import export_csv, import_csv


def show_menu():
    print("\n1. Add expense")
    print("2. Edit expense")
    print("3. Delete expense")
    print("4. Set budget")
    print("5. Recurring expenses")
    print("6. View / search / filter")
    print("7. Spending chart")
    print("8. Insights")
    print("9. Export / import")
    print("0. Exit")


def main():
    print("Expense Tracker V1")
    expenses = load_data()
    generate_recurring(expenses)

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            edit_expense(expenses, int(input("Expense ID: ")))
        elif choice == "3":
            delete_expense(expenses, int(input("Expense ID: ")))
        elif choice == "4":
            set_budget(input("Category: "), float(input("Limit: ")))
            check_budget(expenses)
        elif choice == "5":
            add_recurring(expenses)
        elif choice == "6":
            view_expenses(expenses)
        elif choice == "7":
            show_category_chart(expenses)
        elif choice == "8":
            show_insights(expenses)
        elif choice == "9":
            export_csv(expenses)
        elif choice == "0":
            save_data(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()