# Quick Start Guide - Personal Finance Tracker

## First Time Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python src/main.py
   ```

## First Steps

1. **Add Your First Transaction**
   - Go to "➕ Add Transaction" tab
   - Select today's date
   - Choose "Expense" or "Income"
   - Select a category (e.g., "Food & Dining" for expense)
   - Enter the amount (e.g., 50.00)
   - Add a description (optional)
   - Click "Add Transaction"

2. **View Your Finances**
   - Go to "📊 Dashboard" to see your summary
   - Scroll down to see recent transactions
   - Use the filter buttons to view different time periods

3. **Explore Analytics**
   - Go to "📈 Analytics" tab
   - Click "Income vs Expense" to see a bar chart
   - Click "Category Breakdown" to see spending by category
   - Click "Monthly Trend" to see trends over time

## Tips

- **Quick Filters**: Use "This Month", "This Year", or "Last 30 Days" buttons on the Dashboard
- **Delete Transactions**: Select a transaction in the "📝 Transactions" tab and click "🗑️ Delete Selected"
- **Filter by Type**: Use the dropdown in "📝 Transactions" to filter by Income/Expense
- **Responsive Layout**: The application adjusts to different window sizes

## Keyboard Shortcuts

- Tab through form fields with `Tab`
- Submit forms with `Enter` (button click)

## Data Storage

- All data is stored in `finance_tracker.db` (SQLite database)
- The database is created automatically on first run
- Your data persists between sessions

## Troubleshooting

**Issue**: "ModuleNotFoundError" when running
- **Solution**: Make sure you installed dependencies: `pip install -r requirements.txt`

**Issue**: Calendar widget not showing
- **Solution**: `tkcalendar` might not be installed. Run: `pip install tkcalendar`

**Issue**: Charts not displaying
- **Solution**: Make sure `matplotlib` is installed: `pip install matplotlib`

## Next Steps

- Add more transactions to see analytics become more meaningful
- Experiment with different date ranges
- Use the categories that fit your spending patterns
