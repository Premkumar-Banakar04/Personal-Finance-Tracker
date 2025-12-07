COMPLETE YOUTUBE VIDEO SCRIPT
Personal Finance Tracker in Python — Full Tutorial
Total video length: 15–17 minutes
Format: Ready-to-read; pause slightly at [PAUSE] markers

═══════════════════════════════════════════════════════════════════════════════════
INTRO & HOOK (0:00 - 0:45) — 45 seconds
═══════════════════════════════════════════════════════════════════════════════════

[CAMERA ON - Look at camera, smile, energetic tone]

Hey everyone! Welcome back to the channel! I'm [Your Name], and today I'm going to show you something really cool — I built a Personal Finance Tracker app in Python, and it's completely open source on GitHub!

[PAUSE 2 seconds]

If you've ever wanted to track your expenses, visualize your spending in charts, and manage your finances all in one desktop app, this video is for you. And the best part? The code is free, you can download it, customize it, and learn from it.

[PAUSE 1 second]

So stick around, and let's build this project together!

[PAUSE 1 second - transition to screen]

═══════════════════════════════════════════════════════════════════════════════════
ABOUT ME & CHANNEL (0:45 - 1:15) — 30 seconds
═══════════════════════════════════════════════════════════════════════════════════

[On screen: show your GitHub profile or a quick intro slide, or voiceover]

Quick intro: I'm a developer passionate about building practical desktop applications and teaching others how to code. On this channel, I share Python tutorials, full-stack projects, and open-source code. If you like learning by building real projects, consider subscribing!

[PAUSE 1 second]

Now let's jump into the project.

═══════════════════════════════════════════════════════════════════════════════════
PROJECT OVERVIEW (1:15 - 3:00) — 105 seconds
═══════════════════════════════════════════════════════════════════════════════════

[Show screen with VS Code or file explorer open]

Alright, so here's what we're building today. This is the Personal Finance Tracker. It's a desktop application built with:

[Point to each as you mention it]
— Python 3.8 or higher — the programming language
— Tkinter — Python's built-in GUI framework for the user interface
— SQLite — a local database to store your transactions
— Matplotlib — for generating financial charts
— tkcalendar — for a nice date picker

[PAUSE 1 second]

The app has four main tabs:

[Show each tab area on screen as you describe]

One: Dashboard — Shows your total income, total expenses, and net balance. It also displays recent transactions so you can see what you've logged.

Two: Transactions — Lists all your transactions. You can filter by income or expense, and delete records if needed.

Three: Add Transaction — A form where you enter new transactions. You pick the date, select whether it's income or expense, choose a category, enter the amount, and add a description.

Four: Analytics — Shows you three types of charts: Income versus Expense, Category Breakdown, and a Monthly Trend line graph. Perfect for spotting patterns.

[PAUSE 1 second]

And here's the cool part — everything is stored locally in SQLite, so your data stays on your computer. No cloud, no sign-ups, just pure privacy and control.

[PAUSE 1 second]

Now, let's clone this from GitHub and get it running!

═══════════════════════════════════════════════════════════════════════════════════
SETUP PART 1: Clone from GitHub (3:00 - 4:00) — 60 seconds
═══════════════════════════════════════════════════════════════════════════════════

[Open PowerShell or Command Prompt; show it clearly]

Step one: Clone the repository. I'll open PowerShell and paste the GitHub clone command.

[Type or paste the following command; pause after each step for readability]

```
git clone https://github.com/YOUR_USERNAME/finance-tracker.git
```

[PAUSE 1 second while it clones]

Replace YOUR_USERNAME with your actual GitHub username. If you don't have Git installed, head to git-scm.com and install it first.

[PAUSE 1 second]

Once it's cloned, navigate into the project folder:

```
cd finance-tracker
```

[PAUSE 1 second]

Great! Now we're inside the project directory. Let's check what's in here.

[Show the directory listing — narration explains files]

You can see we have a `src/` folder with the main code, a `requirements.txt` file listing dependencies, and some documentation files like README.md and FEATURES.md. All the Python source files are in `src/`.

═══════════════════════════════════════════════════════════════════════════════════
SETUP PART 2: Create Virtual Environment (4:00 - 5:00) — 60 seconds
═══════════════════════════════════════════════════════════════════════════════════

[Still in PowerShell]

Next step: Create a Python virtual environment. This keeps our dependencies isolated.

[Type the command]

```
python -m venv .venv
```

[PAUSE 2 seconds while the venv is created]

This creates a folder called `.venv`. On Windows, to activate it, we run:

```
.\.venv\Scripts\Activate.ps1
```

[PAUSE 1 second]

If you get a permissions error, you may need to adjust your ExecutionPolicy. Just run:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

[PAUSE 1 second]

Then try activating again. Once activated, you'll see `.venv` in your prompt, like this:

[Point to the prompt showing (.venv)]

Perfect! Now we install the dependencies.

═══════════════════════════════════════════════════════════════════════════════════
SETUP PART 3: Install Dependencies (5:00 - 6:00) — 60 seconds
═══════════════════════════════════════════════════════════════════════════════════

[In activated PowerShell]

With the virtual environment active, run:

```
pip install -r requirements.txt
```

[PAUSE 2-3 seconds while pip installs]

This installs matplotlib for charts, tkcalendar for the date picker, and Pillow for image handling. All the libraries the app needs.

[Wait for installation to complete]

Alright, everything is installed! Let's fire up the app.

═══════════════════════════════════════════════════════════════════════════════════
SETUP PART 4: Launch the Application (6:00 - 6:30) — 30 seconds
═══════════════════════════════════════════════════════════════════════════════════

[In activated PowerShell]

To run the app, type:

```
python src/main.py
```

[PAUSE 1 second]

And boom! The Personal Finance Tracker window opens!

[Show the app window launching with the Dashboard tab visible]

Isn't that beautiful? Clean, professional, dark blue and white theme. Let's take a tour of the features.

═══════════════════════════════════════════════════════════════════════════════════
DEMO PART 1: Dashboard & Summary Cards (6:30 - 8:00) — 90 seconds
═══════════════════════════════════════════════════════════════════════════════════

[App is open on Dashboard tab]

Here's the Dashboard. At the top, you see three summary cards:

[Point to each]

Total Income — shows zero because we haven't added any transactions yet.
Total Expenses — also zero.
Net Balance — zero.

Below that are four preset date range buttons: This Month, This Year, Last 30 Days. These let you filter your summary instantly.

[PAUSE 1 second]

And below the buttons is a table showing Recent Transactions. Right now it's empty, so let's add some data. Switch to the Add Transaction tab.

[Click the "Add Transaction" tab]

═══════════════════════════════════════════════════════════════════════════════════
DEMO PART 2: Add Transaction Form (8:00 - 10:00) — 120 seconds
═══════════════════════════════════════════════════════════════════════════════════

[On the "Add Transaction" tab]

Perfect! Here's the form to add a new transaction. Let me walk you through it.

[Point to each field as you describe]

First, the Date picker — I'll click it to open a calendar and select today's date.

[Click the date picker, select a date]

[PAUSE 1 second]

Next, Transaction Type — you choose between Expense and Income. For this first one, let's log an expense. I'll click Expense.

[Click Expense radio button]

Now, Category. When I click Expense, the categories update automatically. I can choose from predefined categories like Groceries, Transport, Entertainment, etc.

[Click the Category dropdown, select one — e.g., "Groceries"]

Let me pick Groceries.

Amount — I'll enter 1250. That's 1,250 Indian Rupees, by the way. The app is set to use rupees for currency.

[Type in the amount field: 1250]

[PAUSE 1 second]

Description — optional. I'll type something like "Weekly groceries shopping".

[Type in the description field]

[PAUSE 1 second]

Now, click Add Transaction.

[Click the "Add Transaction" button]

[PAUSE 1 second]

Great! A success message appears. The transaction is now in the database. Let me add one more — this time an income entry.

[The form clears. Now select Income]

[Click the Income radio button]

Now the category changes to income categories. I'll select Salary.

[Click the Category dropdown, select Salary]

Let me enter an amount — say 50000 rupees.

[Type in the amount field: 50000]

Add a description — "Monthly salary".

[Type in the description field]

Now, click Add Transaction again.

[Click the "Add Transaction" button]

[PAUSE 1 second]

Excellent! Two transactions added. Now let's see the dashboard update with these values.

═══════════════════════════════════════════════════════════════════════════════════
DEMO PART 3: Dashboard with Data (10:00 - 11:15) — 75 seconds
═══════════════════════════════════════════════════════════════════════════════════

[Click the Dashboard tab]

Look at that! The summary cards have updated:

[Point to each]

Total Income is now 50,000 rupees.
Total Expenses is 1,250 rupees.
Net Balance is 48,750 rupees.

[PAUSE 1 second]

And in the Recent Transactions table below, you can see both entries we just added — the date, category, type, amount, and description.

[PAUSE 1 second]

Perfect! Now let's go to the Transactions tab to see the full list and filtering options.

═══════════════════════════════════════════════════════════════════════════════════
DEMO PART 4: Transactions Tab & Filtering (11:15 - 12:30) — 75 seconds
═══════════════════════════════════════════════════════════════════════════════════

[Click the Transactions tab]

Here's the Transactions tab. It shows a complete list of all your transactions in a table format.

[Point to the filter dropdown]

At the top is a filter dropdown. Right now it's set to "All", showing both income and expense. Let me change it to "Expense" to show only expenses.

[Click the filter dropdown, select Expense]

[PAUSE 1 second]

Now the table shows only the grocery expense. If I select "Income", I'll see only the salary entry.

[Click the filter dropdown, select Income]

[PAUSE 1 second]

Great! And here's a key feature — the Delete Selected button. If you select a transaction row and click Delete Selected, it removes that record from the database.

[Select a row]

Let me select this income entry.

[Click to select]

[PAUSE 1 second]

Now, click Delete Selected.

[Click the Delete Selected button]

[PAUSE 1 second]

A confirmation dialog appears — "Are you sure?". Let me cancel this because we want to keep the data for the demo.

[Click Cancel or press Escape]

[PAUSE 1 second]

Alright, let's add a few more transactions quickly so we have good data for the charts.

[Quickly add 2-3 more transactions via Add Transaction tab — show faster, minimal narration]

[Switch back to Add Transaction, add a few more entries: e.g., Electricity 800, Entertainment 500, etc.]

═══════════════════════════════════════════════════════════════════════════════════
DEMO PART 5: Analytics & Charts (12:30 - 14:30) — 120 seconds
═══════════════════════════════════════════════════════════════════════════════════

[Click the Analytics tab]

Now for the coolest part — Analytics! This tab shows you three beautiful charts to visualize your finances.

[Point to the three buttons]

We have three chart options: Income vs Expense, Category Breakdown, and Monthly Trend. Let me click the first one.

[Click "Income vs Expense" button]

[PAUSE 1 second while chart renders]

Boom! Here's a bar chart showing your total income in green and total expenses in red. The numbers are displayed in rupees on top of each bar. This instantly shows you whether you're spending more than you're earning.

[PAUSE 1 second]

Now let me show the Category Breakdown. I'll click that button.

[Click "Category Breakdown" button]

[PAUSE 1 second while chart renders]

This chart shows income and expense broken down by category. You can see how much you spent in each category — groceries, entertainment, transport, etc. Really useful for spotting where your money is going.

[PAUSE 1 second]

And finally, the Monthly Trend.

[Click "Monthly Trend" button]

[PAUSE 1 second while chart renders]

This is a line graph showing income and expense trends over the last 12 months. If you have historical data, you'll see the pattern of your spending over time. Great for budgeting and forecasting.

[PAUSE 1 second]

These charts are generated using matplotlib, a powerful Python graphing library. They update automatically based on your transaction data.

═══════════════════════════════════════════════════════════════════════════════════
CODE WALKTHROUGH (14:30 - 15:15) — 45 seconds
═══════════════════════════════════════════════════════════════════════════════════

[Open VS Code with the project folder]

Now let me quickly show you the code structure so you understand how it all works.

[Show the src/ folder structure]

Inside `src/`, we have:

[Point to each file]

`main.py` — 664 lines of code. This is the GUI layer. It defines all the tabs, buttons, forms, and styling using Tkinter.

`database.py` — This handles all database operations. Creating tables, inserting transactions, fetching data, and deletions.

`models.py` — Optional data models if you want to extend the app.

[Open database.py briefly]

In `database.py`, you can see the SQL schema for the transactions table. It stores date, category, amount, type, and description.

[Open main.py briefly]

In `main.py`, the `setup_modern_styles()` function defines the professional color scheme and fonts. You can customize this if you want a different theme.

[PAUSE 1 second]

That's the beauty of open source — you can take this code, modify it, and make it your own!

═══════════════════════════════════════════════════════════════════════════════════
KEY FEATURES SUMMARY (15:15 - 15:45) — 30 seconds
═══════════════════════════════════════════════════════════════════════════════════

[Back to showing the app or a summary slide]

Let me recap the key features of this app:

✓ Add, view, and delete transactions
✓ Filter transactions by type
✓ Dashboard with summary cards
✓ Three types of analytics charts
✓ Local SQLite database — your data stays private
✓ Professional, clean UI with Indian Rupee currency
✓ Built entirely in Python — open source and free

═══════════════════════════════════════════════════════════════════════════════════
OUTRO & CALL TO ACTION (15:45 - 17:00) — 75 seconds
═══════════════════════════════════════════════════════════════════════════════════

[Look at camera, friendly tone]

That's it! You now have a fully functional Personal Finance Tracker. If you want to use it, customize it, or learn from the code, it's all on GitHub.

[Show GitHub link on screen, or mention it verbally]

The GitHub repository is linked in the description below. You can clone it, run it, modify it — it's all yours. And if you make cool improvements, feel free to contribute back!

[PAUSE 1 second]

Now, if you found this helpful, here are a few things you can do:

One — Like this video! It helps the YouTube algorithm show this to more people.

Two — Subscribe to the channel! I post weekly tutorials on Python, GUI development, and full-stack projects.

Three — Drop a comment below. Tell me: What feature would you add to this app? Recurring transactions? Budget alerts? Let me know!

[PAUSE 1 second]

And if you want the code, just click the GitHub link in the description.

[PAUSE 1 second]

Thanks so much for watching! I'm [Your Name], and I'll see you in the next one. Peace!

[Wave, smile, fade out]

═══════════════════════════════════════════════════════════════════════════════════
END OF SCRIPT
═══════════════════════════════════════════════════════════════════════════════════

NOTES FOR RECORDING:
- Total runtime: approximately 16–17 minutes (adjust pacing based on your demo speed).
- Use screen capture for the PowerShell/GitHub clone, setup, and app demo.
- Record intro + outro with camera on for personality.
- Pause between major sections for natural transitions.
- Read naturally; don't rush.
- Keep captions on-screen for key commands and file names.

TECHNICAL SETUP:
- Use OBS or ffmpeg to record screen + microphone.
- Export as 1920x1080, 30fps, H.264, ~8–10 Mbps.
- Add the SRT captions file (provided separately) to YouTube for automatic captions.
