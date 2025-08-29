# 💸 Personal Expense Tracker

A command-line Python application to help you log daily expenses, view summaries, and track your spending habits. Built with simplicity and clarity in mind, this tool is perfect for anyone who wants to take control of their finances without the complexity of spreadsheets or apps.

---

## 📦 Features

- ✅ Add daily expenses with amount, category, and date
- 📊 View total spending across all entries
- 🔍 Analyze spending by category or specific date
- 🧾 Summarize expenses with breakdowns by category and date
- 💾 Persistent storage using JSON file

---

## 🛠 Technologies Used

- Python 3
- JSON for file-based data storage
- Datetime module for date handling
- List of dictionaries for expense records

---

## 📁 File Structure

```
├── expense_tracker.py   # Main application script
├── expenses.json        # Auto-generated file to store expense data
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed. You can check by running:

```bash
python --version
```

### Run the Program

```bash
python expense_tracker.py
```

---

## 📋 Usage

Once the program starts, you'll see a menu like this:

```
==== Personal Expense Tracker ====
1. Add Expense
2. View Summary
3. View Spending by Category
4. View Spending by Date
5. Exit
```

Just enter the number corresponding to your desired action and follow the prompts.

---

## 🧠 Example

```text
Enter choice: 1
Enter amount: 150
Enter category (Food/Transport/Entertainment/etc.): Transport
Enter date (YYYY-MM-DD) or press Enter for today:
✅ Expense added successfully!
```

---

## 📌 Notes

- If `expenses.json` does not exist, it will be created automatically.
- Input validation is included for amount and date formats.
- Categories are normalized to title case (e.g., "food" becomes "Food").

---

## 🔮 Future Enhancements

- Monthly and weekly summaries
- Export to CSV or Excel
- GUI version using Tkinter or PyQt
- Add tags or notes to each expense

---

## 👨‍💻 Author

Made with ❤️ by Aman  
Feel free to fork, modify, and improve!

