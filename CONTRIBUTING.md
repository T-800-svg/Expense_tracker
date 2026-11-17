# 🤝 Contributing

This document describes how the **Personal Expense Tracker** was built collaboratively by two students using Git and GitHub: who did what, which branches were used, how pull requests were raised, and how code reviews were carried out. Both students contributed equally to the project.

> **Course:** SEC101: MCA, Advanced Tools and Applications
> **Assignment:** Project Development Using Git, GitHub and Markdown
> **Repository:** [github.com/T-800-svg/Expense_tracker](https://github.com/T-800-svg/Expense_tracker)

---

## 👥 Team Members

| Student | Roll No. | GitHub | Role | Branch |
|---|---|---|---|---|
| **Vivek Shukla** | 65 | [@T-800-svg](https://github.com/T-800-svg) | Student 1 (Repository Owner) | `feature-member1` |
| **Zaki Zaheer** | 69 | [@ZakiZaheer](https://github.com/ZakiZaheer) | Student 2 (Collaborator) | `feature-member2` |

---

## ⚖️ Contribution Summary

| Area | Vivek Shukla | Zaki Zaheer |
|---|---|---|
| Features implemented | 4 (features 1–4) | 4 (features 5–8) |
| Source files written | 4 | 4 |
| Feature branch | `feature-member1` | `feature-member2` |
| Feature pull request merged | #1 | #3 |
| Code review of partner's pull request | Reviewed #3 | Reviewed #1 |
| Merge-conflict task | Raised PR #5 and took part in resolving the conflict | Raised PR #4 and took part in resolving the conflict |
| Documentation | Co-wrote `README.md` and `CONTRIBUTING.md` | Co-wrote `README.md` and `CONTRIBUTING.md` |

---

## 🧑‍💻 Individual Contributions

### Student 1: Vivek Shukla (Roll No. 65)

**Repository setup**

- Initialised the Git repository, configured Git and created the `.gitignore` file.
- Created the initial project structure on `main` and pushed it to a public GitHub repository.
- Invited Student 2 as a collaborator.

**Features implemented on `feature-member1`**

| # | Feature | Source file | Description |
|---|---|---|---|
| 1 | Expense management | `expenses.py` | Add, edit and delete expenses with validation (positive amount, valid `YYYY-MM-DD` date), unique IDs and a confirmation prompt before deleting. |
| 2 | Budget limits with alerts | `budget.py` | Monthly budget per category, with a warning at 80% and an alert when the budget is exceeded. |
| 3 | Recurring expenses | `recurring.py` | Monthly items such as rent or subscriptions, generated automatically once per month on startup. |
| 4 | Smart storage | `storage.py` | Auto-save after every change, automatic `.bak` backup, recovery from corrupted or missing data files, and a startup summary. |

**Collaboration and documentation**

- Raised Pull Request **#1** for the feature branch and Pull Request **#5** for the merge-conflict task.
- Reviewed Student 2's Pull Request **#3**.
- Took part in the merge-conflict task on the welcome line of `main.py`, working with Student 2 to resolve it.
- Contributed to writing both `README.md` and `CONTRIBUTING.md` together with Student 2.

---

### Student 2: Zaki Zaheer (Roll No. 69)

**Setup**

- Accepted the collaborator invitation, cloned the repository and configured Git locally.
- Created the `feature-member2` branch.

**Features implemented on `feature-member2`**

| # | Feature | Source file | Description |
|---|---|---|---|
| 5 | View / Search / Filter | `reports.py` | Aligned table view, sorting by any column, and filtering by category, date range, amount range or keyword. |
| 6 | Terminal spending charts | `charts.py` | Text bar chart of spending per category, with percentages. |
| 7 | Spending insights | `insights.py` | Top category, daily average, comparison with last month, and the top 3 expenses. |
| 8 | Smart export / import | `export.py` | Filtered CSV export, formatted monthly report (`.txt`), auto-named files in `exports/`, and CSV import that skips invalid rows. |

**Collaboration, conflict resolution and documentation**

- Raised Pull Request **#3** for the feature branch and Pull Request **#4** for the merge-conflict task.
- Reviewed Student 1's Pull Request **#1**.
- Took part in the merge-conflict task, resolving the conflict on the welcome line in `main.py` and committing the corrected version, together with Student 1.
- Contributed to writing both `README.md` and `CONTRIBUTING.md` together with Student 1.

---

## 🌿 Branches

| Branch | Owner | Purpose |
|---|---|---|
| `main` | Shared | Stable branch. Holds the initial project structure and receives all merged work. |
| `feature-member1` | Vivek Shukla | Expense management, budgets, recurring expenses and storage. |
| `feature-member2` | Zaki Zaheer | Reports, charts, insights and CSV export/import. |

**Branching rules followed**

1. No feature work was committed directly to `main`.
2. Each student worked only on their own feature branch.
3. Branches were pushed to GitHub and merged into `main` only through pull requests.
4. Commit messages describe the change that was made (for example, "Add budget alert at 80%").

---

## 🔀 Pull Requests

| PR | Title | Author | Status | Reviewed by |
|---|---|---|---|---|
| [#1](https://github.com/T-800-svg/Expense_tracker/pull/1) | Added expense management, budgets, recurring expenses and storage | Vivek Shukla (`T-800-svg`) | ✅ Merged | Zaki Zaheer |
| [#3](https://github.com/T-800-svg/Expense_tracker/pull/3) | completed report, insight, chart and csv features. | Zaki Zaheer (`ZakiZaheer`) | ✅ Merged | Vivek Shukla |
| [#4](https://github.com/T-800-svg/Expense_tracker/pull/4) | Changed Print Statement Content for merge Conflict | Zaki Zaheer (`ZakiZaheer`) | ✅ Merged | Merge-conflict task |
| [#5](https://github.com/T-800-svg/Expense_tracker/pull/5) | Merge conflict case | Vivek Shukla (`T-800-svg`) | ✅ Merged | Merge-conflict task |

PRs #4 and #5 were used for the deliberate merge-conflict task described below.

---

## 🔍 Code Reviews

Each student reviewed the other's feature pull request before it was merged into `main`.

### Review of PR #1 by Zaki Zaheer (Student 2)

Reviewed: *Added expense management, budgets, recurring expenses and storage.*

| Feature | Reviewer remarks | Result |
|---|---|---|
| Expense management (`expenses.py`) | Add, edit and delete work correctly. Validation of amount and date is in place, and the delete confirmation prompt works. Code is readable. | ✅ Approved |
| Budget limits with alerts (`budget.py`) | Budget can be set per category. The 80% warning and the over-budget alert appear as expected. | ✅ Approved |
| Recurring expenses (`recurring.py`) | Recurring items are generated once per month and are not duplicated on restart. | ✅ Approved |
| Smart storage (`storage.py`) | Data is saved after every change. Backup and recovery from a missing or corrupted file work correctly. | ✅ Approved |

**Overall remark:** All features work as described and the code is clean. Approved and merged.

### Review of PR #3 by Vivek Shukla (Student 1)

Reviewed: *completed report, insight, chart and csv features.*

| Feature | Reviewer remarks | Result |
|---|---|---|
| View / Search / Filter (`reports.py`) | Table is neatly aligned. Sorting and all filters (category, date range, amount range, keyword) give correct results. | ✅ Approved |
| Terminal spending charts (`charts.py`) | Bar chart displays per-category spending with correct percentages. | ✅ Approved |
| Spending insights (`insights.py`) | Top category, daily average, last-month comparison and top 3 expenses are calculated correctly. | ✅ Approved |
| Smart export / import (`export.py`) | CSV export, monthly report and CSV import work. Invalid rows are skipped without crashing the app. | ✅ Approved |

**Overall remark:** All features are working and well integrated with the rest of the application. Approved and merged.

---

## ⚔️ Merge Conflict Resolution

As required by the assignment, both students deliberately edited **the same line** (the welcome message in `main.py`) on separate branches.

1. Student 1 changed the line on their branch and raised PR [#5](https://github.com/T-800-svg/Expense_tracker/pull/5), which was merged into `main` first.
2. Student 2 changed the same line on a separate branch and raised PR [#4](https://github.com/T-800-svg/Expense_tracker/pull/4). Git reported a **merge conflict** because both branches had edited the same line.
3. **Both students took part in resolving the conflict**: Zaki Zaheer removed the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) and committed the corrected version, while Vivek Shukla agreed on the final welcome line with him.
4. PR #4 was then merged successfully.

The commit history can be viewed with:

```bash
git log --oneline --graph --all
```

---

## 📌 How to Contribute (Workflow Used)

1. Clone the repository: `git clone https://github.com/T-800-svg/Expense_tracker.git`
2. Create or switch to your feature branch: `git checkout -b feature-memberX`
3. Make small, meaningful commits: `git add .` then `git commit -m "Describe the change"`
4. Push the branch: `git push origin feature-memberX`
5. Open a pull request on GitHub, targeting `main`.
6. Ask your partner to review. Address any comments.
7. Merge the pull request once it is approved.

---

*Individual contributions can be verified through the GitHub commit history and pull requests.*
