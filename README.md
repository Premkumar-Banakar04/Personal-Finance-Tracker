# Personal Finance Tracker

A modern, responsive GUI application for tracking personal finances with an intuitive user interface built with Python and Tkinter.

## Features

- **📊 Dashboard**: View financial overview with summary cards showing total income, expenses, and net balance
- **📝 Transactions**: Manage all your transactions with filtering and deletion options
- **➕ Add Transaction**: Easy-to-use form for adding new income or expense transactions
- **📈 Analytics**: Visual charts for:
  - Income vs Expense comparison
  - Category-wise breakdown
  - Monthly trends over time
- **💾 Database**: SQLite-based persistent storage
- **🎨 Responsive UI**: Modern, user-friendly interface with proper styling

## Requirements

- Python 3.8+
- tkinter (usually comes with Python)
- matplotlib
- tkcalendar
- pillow

## Installation

1. Clone or download the project
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python src/main.py
```

## Project Structure

```
finance-tracker/
├── src/
│   ├── main.py          # Main GUI application
│   ├── database.py      # Database operations
│   ├── cli.py          # CLI utilities
│   ├── db.py           # Database setup
│   └── models.py       # Data models
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Usage Guide

### Dashboard Tab
- View your financial summary for selected periods
- Quick filters: This Month, This Year, Last 30 Days
- See your most recent transactions at a glance

### Add Transaction Tab
- Select transaction date
- Choose transaction type (Income/Expense)
- Pick category from available options
- Enter amount
- Add optional description
- Click "Add Transaction" to save

### Transactions Tab
- View all transactions in a table
- Filter by type (All, Income, Expense)
- Select and delete transactions as needed
- Refresh to see latest changes

### Analytics Tab
- **Income vs Expense**: Bar chart comparing income and expenses
- **Category Breakdown**: See spending by category
- **Monthly Trend**: Track income and expenses over time

## Categories

### Default Expense Categories
- Food & Dining
- Transportation
- Utilities
- Entertainment
- Shopping
- Health
- Education
- Other Expenses

### Default Income Categories
- Salary
- Freelance
- Investment
- Other Income

## Database

The application uses SQLite for data persistence. The database file (`finance_tracker.db`) is automatically created in the project directory when you first run the app.

## Customization

You can customize categories, colors, and other settings by editing the source code:
- Modify categories in `database.py`
- Change colors in `setup_styles()` method in `main.py`
- Adjust window size and default settings in `PersonalFinanceTracker.__init__()`

## License

This project is open source and available for personal and educational use.

## Support

For issues or suggestions, please refer to the source code documentation.
