# 💰 Personal Expense Tracker

A command-line application for recording, analysing and exporting personal expenses, built with **Python** and developed collaboratively using **Git, GitHub and Markdown**.

> **Course:** SEC101: MCA, Advanced Tools and Applications
> **Assignment:** Project Development Using Git, GitHub and Markdown
> **Repository:** [github.com/T-800-svg/Expense_tracker](https://github.com/T-800-svg/Expense_tracker)

---

## 📖 Description

The Personal Expense Tracker lets a user log daily spending, set monthly budgets, schedule recurring bills, and understand where their money goes through tables, text charts, insights and exportable reports. All data is stored locally in JSON files, so the app needs no database or internet connection.

## 🎯 Objectives

- Build a working multi-file software project with at least five functional features.
- Demonstrate **version control** using Git: branching, commits, pull requests, code review, merging and conflict resolution.
- Collaborate through **GitHub** using two separate accounts.
- Document the project with **Markdown** (`README.md` and `CONTRIBUTING.md`).

## 👥 Team Members and Contributions

| Student | Roll No. | GitHub | Branch | Contribution |
|---|---|---|---|---|
| **Vivek Shukla** | 65 | [@T-800-svg](https://github.com/T-800-svg) | `feature-member1` | Repository setup, expense management, budgets, recurring expenses, storage, documentation |
| **Zaki Zaheer** | 69 | [@ZakiZaheer](https://github.com/ZakiZaheer) | `feature-member2` | Search/filter, charts, insights, export/import |

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full breakdown of branches, pull requests and reviews.

## ✨ Features

### Student 1: Vivek Shukla

1. **Expense management**: add, edit and delete expenses with validation (positive amount, valid `YYYY-MM-DD` date), unique IDs and a confirmation prompt before deleting.
2. **Budget limits with alerts**: set a monthly budget per category. The app warns at **80%** and flags when the budget is **exceeded**.
3. **Recurring expenses**: define monthly items such as rent or subscriptions. They are generated automatically once per month on startup.
4. **Smart storage**: auto-save after every change, automatic `.bak` backup, recovery from corrupted or missing data files, and a startup summary.

### Student 2: Zaki Zaheer

5. **View / Search / Filter**: aligned table view, sorting by any column, and filtering by category, date range, amount range or keyword.
6. **Terminal spending charts**: text bar chart of spending per category with percentages.
7. **Spending insights**: top category, daily average, comparison with last month, and the top 3 expenses.
8. **Smart export / import**: filtered CSV export, formatted monthly report (`.txt`), auto-named files in `exports/`, and CSV import that skips invalid rows.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| **Python 3.8+** | Programming language (standard library only, so nothing to install) |
| `json`, `csv`, `shutil`, `os`, `datetime`, `calendar` | Storage, export, backups and date handling |
| **Git** | Version control |
| **GitHub** | Remote hosting, pull requests and code review |
| **Markdown** | Documentation |

## 📁 Project Structure

```
Expense_tracker/
├── main.py          # menu and program flow (shared)
├── expenses.py      # add / edit / delete + validation      (Student 1)
├── budget.py        # budget limits + alerts                (Student 1)
├── recurring.py     # recurring expenses                    (Student 1)
├── storage.py       # JSON save/load, backup, recovery      (Student 1)
├── reports.py       # view / search / filter / sort         (Student 2)
├── charts.py        # terminal bar charts                   (Student 2)
├── insights.py      # spending analytics                    (Student 2)
├── export.py        # CSV export/import + monthly report    (Student 2)
├── README.md        # project documentation
├── CONTRIBUTING.md  # contributions, branches, PRs, reviews
└── .gitignore       # files Git should ignore
```

Files created while the app runs (`data.json`, `data.json.bak`, `budget.json`, `recurring.json` and the `exports/` folder) are listed in `.gitignore` and are **not** stored in the repository.

## ⚙️ Installation

**Prerequisites:** [Python 3.8 or newer](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads).

```bash
# 1. Clone the repository
git clone https://github.com/T-800-svg/Expense_tracker.git

# 2. Move into the project folder
cd Expense_tracker
```

No packages need to be installed.

## ▶️ How to Run

```bash
python main.py
```

On some Windows setups use `py main.py` instead.

### Menu

| Option | Action |
|---|---|
| 1 | Add expense |
| 2 | Edit expense (asks for the expense ID) |
| 3 | Delete expense (asks for the expense ID) |
| 4 | Set budget |
| 5 | Add recurring expense |
| 6 | View / sort / search / filter |
| 7 | Spending chart |
| 8 | Insights |
| 9 | Export / import (CSV, monthly report) |
| 0 | Save and exit |

### Data format

Each expense is stored as:

```json
{"id": 1, "amount": 250.0, "category": "Food", "date": "2026-11-10", "description": "Lunch"}
```

## 🖼️ Screenshots and Sample Output

### Startup and adding an expense

> <img width="521" height="407" alt="Screenshot 2026-11-17 215114" src="https://github.com/user-attachments/assets/03dd4c4f-d843-4e0f-ad57-bf9919b52582" />
 the terminal after running `python main.py`, showing the startup line (`Loaded N expenses | This month: ...`) and the menu, then adding one expense (option 1) with the `[OK] Added expense` message.

### Budget alerts

> <img width="390" height="280" alt="Screenshot 2026-11-17 215900" src="https://github.com/user-attachments/assets/f0ffd304-7a40-493f-b8e8-4870edf317e5" />
  <img width="561" height="320" alt="Screenshot 2026-11-17 215944" src="https://github.com/user-attachments/assets/730a9193-9df7-4a72-8643-ba07b4aa90fc" />
  <img width="525" height="322" alt="Screenshot 2026-11-17 220300" src="https://github.com/user-attachments/assets/ed88b3b7-c3f6-4312-a292-736e0e95fb4f" />

 option 4 setting a budget, then adding expenses until both the `[WARN]` (80%) and `[OVER]` (over budget) messages appear.

```text
[WARN] Food: Rs.1,750 of Rs.2,000 spent (88%) - nearing your limit
[OVER] Food: Rs.2,050 of Rs.2,000 spent - OVER BUDGET by Rs.50
```

### Recurring expenses

> <img width="386" height="317" alt="image" src="https://github.com/user-attachments/assets/09b5221b-0e4d-4502-89df-3f7f2c59c4e2" />
 option 5 adding a recurring expense, showing `[OK] Added 1 recurring expense(s) for 2026-11`.

### View, sort and filter

> <img width="557" height="497" alt="image" src="https://github.com/user-attachments/assets/23a5019d-85ae-493d-8736-c17f8423795d" />
 option 6 showing the expense table, and a second shot of a filtered result (for example by category or keyword).

```text
ID   Date        Category          Amount  Description
--------------------------------------------------------------
3    2026-11-01  Bills           8,000.00  Rent
2    2026-11-05  Travel          3,600.00  Train tickets
1    2026-11-03  Food            4,200.00  Mess fees
--------------------------------------------------------------
3 expense(s) | Total: Rs.15,800.00
```

### Spending chart

> <img width="452" height="411" alt="image" src="https://github.com/user-attachments/assets/d4f75fec-3095-4ba2-b43f-44223ba9c0f8" />
 option 7 showing the category bar chart.

```text
Spending by category (all time)
----------------------------------------------------
Bills        ######--------------  Rs.    8,000 (30%)
Rent         #####---------------  Rs.    6,999 (26%)
Food         ####----------------  Rs.    4,899 (18%)
Travel       ###-----------------  Rs.    3,600 (14%)
Sports       ##------------------  Rs.    3,000 (11%)
----------------------------------------------------
Total                              Rs.   26,498
```

### Insights

> <img width="421" height="392" alt="image" src="https://github.com/user-attachments/assets/a471723d-fda9-47c2-815c-b86abdd8fc2b" />
 option 8 showing the insights output.

### Export and monthly report

> <img width="498" height="352" alt="Screenshot 2026-11-17 223336" src="https://github.com/user-attachments/assets/2cab7ad6-df33-453d-a775-5d2b026f4e54" />
  <img width="657" height="180" alt="Screenshot 2026-11-17 223401" src="https://github.com/user-attachments/assets/aec8ce90-4c64-4171-9ad0-f698df4d35c7" />
  <img width="310" height="46" alt="Screenshot 2026-11-17 223423" src="https://github.com/user-attachments/assets/87a17b18-4273-46a5-a7c1-78fd8b94db2f" />
 option 9 exporting a CSV and a monthly report, and the generated `exports/` files (or the report opened in an editor).

## 🌿 Git Workflow Used

1. `main` was created with the project structure and pushed to GitHub (Student 1).
2. Each student worked on their own branch: `feature-member1` and `feature-member2`.
3. Each branch was pushed and merged into `main` through a **pull request** after being **reviewed by the other student**.
4. A deliberate **merge conflict** was created on the welcome line in `main.py` and resolved by both students.
5. The documentation was added on the `docs` branch.

### Commit history

> <img width="837" height="687" alt="image" src="https://github.com/user-attachments/assets/824d735d-df91-45d4-8ec6-18cb597f0851" />
 the output of `git log --oneline --graph --all` showing both feature branches, the merges and the conflict resolution.

```bash
git log --oneline --graph --all
```

## 🤝 Contributing

Branching, pull request and code review details are in [CONTRIBUTING.md](CONTRIBUTING.md).

## 📝 Notes

- All data is stored locally. Nothing is sent over the internet.
- Passwords, API keys and personal data are **not** committed to this repository.
- *Individual contributions can be verified through the GitHub commit history and pull requests.*
