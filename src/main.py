import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, font
from datetime import datetime, timedelta
from database import FinanceDatabase
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkcalendar import DateEntry
import os

class PersonalFinanceTracker:
    """Main GUI application for Personal Finance Tracker with Professional Corporate Design"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Personal Finance Tracker")
        self.root.geometry("1400x800")
        self.root.minsize(900, 600)
        
        # Initialize database
        self.db = FinanceDatabase()
        
        # Configure styles with professional design
        self.setup_modern_styles()
        
        # Create main layout
        self.create_main_layout()
        
        # Load initial data
        self.refresh_data()
    
    def setup_modern_styles(self):
        """Configure professional corporate color scheme"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Define professional corporate color palette
        self.colors = {
            'bg': "#FFFFFF",            # Clean white background
            'card_bg': "#F8F9FA",       # Light gray card background
            'accent_primary': "#1E40AF",   # Professional navy blue
            'accent_secondary': "#059669", # Corporate teal/green
            'accent_tertiary': "#7C3AED",  # Executive purple
            'success_green': "#16A34A",    # Success green
            'danger_red': "#DC2626",       # Alert red
            'warning_orange': "#EA580C",   # Warning orange
            'text_dark': "#1F2937",        # Dark gray text
            'text_gray': "#6B7280",        # Medium gray text
            'border_color': "#E5E7EB",     # Light gray border
            'gradient_blue': "#2563EB",    # Bright professional blue
            'gradient_teal': "#0891B2",    # Cyan teal
            'hover_bg': "#F3F4F6",         # Hover background
        }
        
        # Configure frame styles
        style.configure('TFrame', background=self.colors['bg'])
        style.configure('Card.TFrame', background=self.colors['card_bg'], relief='flat', borderwidth=0)
        
        # Configure label styles
        style.configure('TLabel', background=self.colors['bg'], foreground=self.colors['text_dark'], 
                       font=('Segoe UI', 10))
        style.configure('Title.TLabel', background=self.colors['bg'], foreground=self.colors['accent_primary'], 
                       font=('Segoe UI', 26, 'bold'))
        style.configure('Header.TLabel', background=self.colors['card_bg'], foreground=self.colors['accent_primary'],
                       font=('Segoe UI', 13, 'bold'))
        style.configure('Subtitle.TLabel', background=self.colors['bg'], foreground=self.colors['accent_secondary'],
                       font=('Segoe UI', 12, 'bold'))
        style.configure('Stat.TLabel', background=self.colors['card_bg'], foreground=self.colors['text_dark'],
                       font=('Segoe UI', 11))
        style.configure('StatValue.TLabel', background=self.colors['card_bg'], foreground=self.colors['gradient_blue'],
                       font=('Segoe UI', 22, 'bold'))
        
        # Configure button styles - Professional appearance
        style.configure('TButton', background=self.colors['gradient_blue'], foreground="#FFFFFF",
                       font=('Segoe UI', 10, 'bold'), borderwidth=0, relief='flat', padding=10)
        style.map('TButton', 
                 background=[('active', self.colors['accent_primary']), ('pressed', '#1E3A8A')],
                 foreground=[('active', '#FFFFFF')])
        
        style.configure('Success.TButton', background=self.colors['success_green'], foreground="#FFFFFF")
        style.map('Success.TButton',
                 background=[('active', '#15803D'), ('pressed', '#166534')])
        
        style.configure('Danger.TButton', background=self.colors['danger_red'], foreground="#FFFFFF")
        style.map('Danger.TButton',
                 background=[('active', '#B91C1C'), ('pressed', '#991B1B')])
        
        # Configure notebook style
        style.configure('TNotebook', background=self.colors['bg'], borderwidth=0)
        style.configure('TNotebook.Tab', padding=[20, 10], font=('Segoe UI', 11, 'bold'),
                       background=self.colors['border_color'], foreground=self.colors['text_gray'])
        style.map('TNotebook.Tab', 
                 background=[('selected', self.colors['gradient_blue'])],
                 foreground=[('selected', '#FFFFFF')])
        
        # Configure combobox
        style.configure('TCombobox', fieldbackground=self.colors['card_bg'], background=self.colors['gradient_blue'],
                       foreground=self.colors['text_dark'], font=('Segoe UI', 10))
        
        # Configure entry
        style.configure('TEntry', fieldbackground=self.colors['card_bg'], foreground=self.colors['text_dark'],
                       font=('Segoe UI', 10), padding=5)
        
        # Configure Treeview (transactions) font sizes for better readability
        style.configure('Treeview', background=self.colors['card_bg'], fieldbackground=self.colors['card_bg'],
                   foreground=self.colors['text_dark'], font=('Segoe UI', 12))
        style.configure('Treeview.Heading', font=('Segoe UI', 12, 'bold'), foreground=self.colors['text_dark'])
        style.map('Treeview', background=[('selected', self.colors['gradient_blue'])], foreground=[('selected', '#FFFFFF')])
        
        self.root.configure(bg=self.colors['bg'])
    
    def create_main_layout(self):
        """Create the main application layout"""
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create tabs
        self.dashboard_tab = ttk.Frame(self.notebook)
        self.transactions_tab = ttk.Frame(self.notebook)
        self.add_transaction_tab = ttk.Frame(self.notebook)
        self.analytics_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.dashboard_tab, text="📊 Dashboard")
        self.notebook.add(self.transactions_tab, text="📝 Transactions")
        self.notebook.add(self.add_transaction_tab, text="➕ Add Transaction")
        self.notebook.add(self.analytics_tab, text="📈 Analytics")
        
        # Build tab contents
        self.setup_dashboard_tab()
        self.setup_transactions_tab()
        self.setup_add_transaction_tab()
        self.setup_analytics_tab()
    
    def setup_dashboard_tab(self):
        """Setup the dashboard tab with professional design and summary cards"""
        main_frame = ttk.Frame(self.dashboard_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Title with professional styling
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title = ttk.Label(title_frame, text="📊 Financial Overview", style="Title.TLabel")
        title.pack(side=tk.LEFT)
        
        # Date range selection with professional styling
        date_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], highlightthickness=2, 
                             highlightbackground=self.colors['border_color'], highlightcolor=self.colors['gradient_blue'])
        date_frame.pack(fill=tk.X, pady=10, ipady=10, ipadx=10)
        
        ttk.Label(date_frame, text="📅 Select Period:", style="Header.TLabel").pack(side=tk.LEFT, padx=10)
        
        ttk.Button(date_frame, text="📆 This Month", 
                  command=self.set_this_month).pack(side=tk.LEFT, padx=5)
        ttk.Button(date_frame, text="📆 This Year", 
                  command=self.set_this_year).pack(side=tk.LEFT, padx=5)
        ttk.Button(date_frame, text="📆 Last 30 Days", 
                  command=self.set_last_30_days).pack(side=tk.LEFT, padx=5)
        
        # Summary cards frame with professional styling
        cards_frame = ttk.Frame(main_frame)
        cards_frame.pack(fill=tk.BOTH, expand=False, pady=20)
        
        # Create summary cards with professional colors
        self.income_label = self.create_modern_card(cards_frame, "💰 Total Income", 0, 0, 
                                                    self.colors['success_green'], self.colors['gradient_teal'])
        self.expense_label = self.create_modern_card(cards_frame, "💸 Total Expenses", 0, 1, 
                                                     self.colors['danger_red'], self.colors['warning_orange'])
        self.balance_label = self.create_modern_card(cards_frame, "💵 Net Balance", 0, 2, 
                                                     self.colors['gradient_blue'], self.colors['accent_tertiary'])
        
        # Recent transactions section
        recent_title_frame = ttk.Frame(main_frame)
        recent_title_frame.pack(pady=(20, 10), fill=tk.X)
        ttk.Label(recent_title_frame, text="📝 Recent Transactions", style="Subtitle.TLabel").pack(side=tk.LEFT)
        
        # Tree view frame with professional border
        tree_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], highlightthickness=1,
                             highlightbackground=self.colors['border_color'])
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        columns = ("Date", "Category", "Type", "Amount", "Description")
        self.dashboard_tree = ttk.Treeview(tree_frame, columns=columns, height=8, style='Treeview')
        self.dashboard_tree.heading('#0', text='ID')
        self.dashboard_tree.column('#0', width=30)
        
        for col in columns:
            self.dashboard_tree.heading(col, text=col)
            self.dashboard_tree.column(col, width=100)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, 
                                 command=self.dashboard_tree.yview)
        self.dashboard_tree.configure(yscrollcommand=scrollbar.set)
        
        self.dashboard_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def create_modern_card(self, parent, title, row, col, primary_color, secondary_color):
        """Create a professional summary card"""
        card = tk.Frame(parent, bg=self.colors['card_bg'], highlightthickness=2, 
                       highlightbackground=primary_color, highlightcolor=secondary_color,
                       relief=tk.FLAT)
        card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew", ipadx=20, ipady=20)
        
        parent.grid_columnconfigure(col, weight=1)
        parent.grid_rowconfigure(row, weight=1)
        
        # Title with icon
        title_label = tk.Label(card, text=title, font=('Segoe UI', 12, 'bold'),
                              bg=self.colors['card_bg'], fg=primary_color)
        title_label.pack(pady=(0, 15))
        
        # Value label with professional color
        value_label = tk.Label(card, text="₹0.00", font=('Segoe UI', 28, 'bold'),
                              bg=self.colors['card_bg'], fg=secondary_color)
        value_label.pack(pady=10)
        
        return value_label
    
    def create_card(self, parent, title, row, col, color):
        """Legacy create_card for compatibility"""
        return self.create_modern_card(parent, title, row, col, color, color)
    
    def setup_transactions_tab(self):
        """Setup the transactions tab with professional design"""
        main_frame = ttk.Frame(self.transactions_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Title
        title = ttk.Label(main_frame, text="📝 All Transactions", style="Title.TLabel")
        title.pack(pady=(0, 20))
        
        # Filter frame with professional styling
        filter_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], highlightthickness=1,
                               highlightbackground=self.colors['border_color'])
        filter_frame.pack(fill=tk.X, pady=10, ipady=10, ipadx=10)
        
        ttk.Label(filter_frame, text="🔍 Filter by Type:", style="Header.TLabel").pack(side=tk.LEFT, padx=10)
        self.filter_var = tk.StringVar(value="All")
        filter_combo = ttk.Combobox(filter_frame, textvariable=self.filter_var,
                                   values=["All", "Income", "Expense"], width=15)
        filter_combo.pack(side=tk.LEFT, padx=5)
        filter_combo.bind("<<ComboboxSelected>>", lambda e: self.refresh_transactions())
        
        ttk.Button(filter_frame, text="🔄 Refresh", 
                  command=self.refresh_transactions).pack(side=tk.LEFT, padx=5)
        ttk.Button(filter_frame, text="🗑️ Delete Selected", style="Danger.TButton",
                  command=self.delete_transaction).pack(side=tk.LEFT, padx=5)
        
        # Tree view frame with professional border
        tree_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], highlightthickness=1,
                             highlightbackground=self.colors['border_color'])
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        columns = ("Date", "Category", "Type", "Amount", "Description")
        self.transactions_tree = ttk.Treeview(tree_frame, columns=columns)
        self.transactions_tree.heading('#0', text='ID')
        self.transactions_tree.column('#0', width=40)
        
        for col in columns:
            self.transactions_tree.heading(col, text=col)
            if col == "Amount":
                self.transactions_tree.column(col, width=100)
            elif col == "Description":
                self.transactions_tree.column(col, width=200)
            else:
                self.transactions_tree.column(col, width=100)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL,
                                 command=self.transactions_tree.yview)
        self.transactions_tree.configure(yscrollcommand=scrollbar.set)
        
        self.transactions_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def setup_add_transaction_tab(self):
        """Setup the add transaction tab with professional form design"""
        main_frame = ttk.Frame(self.add_transaction_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Title
        title = ttk.Label(main_frame, text="➕ Add New Transaction", 
                         style="Title.TLabel")
        title.pack(pady=(0, 20))
        
        # Form card with professional border
        form_card = tk.Frame(main_frame, bg=self.colors['card_bg'], highlightthickness=1,
                            highlightbackground=self.colors['border_color'])
        form_card.pack(fill=tk.BOTH, expand=True, ipady=20, ipadx=20)
        
        # Form frame inside card
        form_frame = tk.Frame(form_card, bg=self.colors['card_bg'])
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Date
        date_label_frame = tk.Frame(form_frame, bg=self.colors['card_bg'])
        date_label_frame.pack(fill=tk.X, pady=(0, 5))
        tk.Label(date_label_frame, text="📅 Date:", font=('Segoe UI', 11, 'bold'),
                bg=self.colors['card_bg'], fg=self.colors['gradient_teal']).pack(side=tk.LEFT)
        
        self.date_entry = DateEntry(form_frame, width=12, background=self.colors['gradient_teal'],
                                    foreground='white', borderwidth=2, font=('Segoe UI', 10))
        self.date_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Transaction Type with professional radio buttons
        type_label_frame = tk.Frame(form_frame, bg=self.colors['card_bg'])
        type_label_frame.pack(fill=tk.X, pady=(0, 5))
        tk.Label(type_label_frame, text="💱 Type:", font=('Segoe UI', 11, 'bold'),
                bg=self.colors['card_bg'], fg=self.colors['accent_secondary']).pack(side=tk.LEFT)
        
        self.type_var = tk.StringVar(value="expense")
        type_frame = tk.Frame(form_frame, bg=self.colors['card_bg'])
        type_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Radiobutton(type_frame, text="💸 Expense", variable=self.type_var,
                       value="expense", command=self.update_categories).pack(side=tk.LEFT, padx=20)
        ttk.Radiobutton(type_frame, text="💰 Income", variable=self.type_var,
                       value="income", command=self.update_categories).pack(side=tk.LEFT, padx=20)
        
        # Category
        cat_label_frame = tk.Frame(form_frame, bg=self.colors['card_bg'])
        cat_label_frame.pack(fill=tk.X, pady=(0, 5))
        tk.Label(cat_label_frame, text="📂 Category:", font=('Segoe UI', 11, 'bold'),
                bg=self.colors['card_bg'], fg=self.colors['success_green']).pack(side=tk.LEFT)
        
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(form_frame, textvariable=self.category_var, height=8)
        self.category_combo.pack(fill=tk.X, pady=(0, 15))
        
        # Amount
        amt_label_frame = tk.Frame(form_frame, bg=self.colors['card_bg'])
        amt_label_frame.pack(fill=tk.X, pady=(0, 5))
        tk.Label(amt_label_frame, text="💵 Amount:", font=('Segoe UI', 11, 'bold'),
                bg=self.colors['card_bg'], fg=self.colors['danger_red']).pack(side=tk.LEFT)
        
        self.amount_entry = ttk.Entry(form_frame, width=20)
        self.amount_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Description
        desc_label_frame = tk.Frame(form_frame, bg=self.colors['card_bg'])
        desc_label_frame.pack(fill=tk.X, pady=(0, 5))
        tk.Label(desc_label_frame, text="📝 Description (Optional):", font=('Segoe UI', 11, 'bold'),
                bg=self.colors['card_bg'], fg=self.colors['accent_tertiary']).pack(side=tk.LEFT)
        
        self.description_text = tk.Text(form_frame, height=4, width=40, 
                                       bg=self.colors['card_bg'], fg=self.colors['text_dark'],
                                       insertbackground=self.colors['gradient_blue'],
                                       font=('Segoe UI', 10))
        self.description_text.pack(fill=tk.X, pady=(0, 20))
        
        # Buttons
        button_frame = tk.Frame(form_frame, bg=self.colors['card_bg'])
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="✅ Add Transaction", style="Success.TButton",
                  command=self.add_transaction).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🔄 Clear Form", 
                  command=self.clear_form).pack(side=tk.LEFT, padx=5)
        
        # Initialize categories
        self.update_categories()
    
    def setup_analytics_tab(self):
        """Setup the analytics tab with professional charts"""
        main_frame = ttk.Frame(self.analytics_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Title
        title = ttk.Label(main_frame, text="📈 Financial Analytics", 
                         style="Title.TLabel")
        title.pack(pady=(0, 20))
        
        # Button frame with professional styling
        button_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], highlightthickness=1,
                               highlightbackground=self.colors['border_color'])
        button_frame.pack(fill=tk.X, pady=10, ipady=10, ipadx=10)
        
        ttk.Button(button_frame, text="💹 Income vs Expense", 
                  command=self.show_income_expense_chart).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(button_frame, text="📊 Category Breakdown", 
                  command=self.show_category_chart).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(button_frame, text="📉 Monthly Trend", 
                  command=self.show_monthly_chart).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Chart frame
        self.chart_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], highlightthickness=1,
                                   highlightbackground=self.colors['border_color'])
        self.chart_frame.pack(fill=tk.BOTH, expand=True, pady=10)
    
    def update_categories(self):
        """Update category dropdown based on transaction type"""
        trans_type = self.type_var.get()
        categories = self.db.get_categories(trans_type)
        self.category_combo['values'] = categories
        if categories:
            self.category_combo.current(0)
    
    def add_transaction(self):
        """Add a new transaction"""
        try:
            # Get date in YYYY-MM-DD format
            date_obj = self.date_entry.get_date()
            date = date_obj.strftime("%Y-%m-%d")
            
            trans_type = self.type_var.get()
            category = self.category_var.get()
            amount_str = self.amount_entry.get()
            description = self.description_text.get("1.0", tk.END).strip()
            
            if not amount_str or not category:
                messagebox.showwarning("Input Error", "Please fill all required fields")
                return
            
            amount = float(amount_str)
            if amount <= 0:
                messagebox.showwarning("Input Error", "Amount must be positive")
                return
            
            self.db.add_transaction(date, category, amount, trans_type, description)
            messagebox.showinfo("Success", "Transaction added successfully!")
            
            self.clear_form()
            self.refresh_data()
            
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered")
    
    def clear_form(self):
        """Clear the transaction form"""
        today = datetime.now()
        self.date_entry.set_date(today)
        self.type_var.set("expense")
        self.amount_entry.delete(0, tk.END)
        self.description_text.delete("1.0", tk.END)
        self.update_categories()
    
    def delete_transaction(self):
        """Delete selected transaction"""
        selection = self.transactions_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a transaction to delete")
            return
        
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this transaction?"):
            for item in selection:
                trans_id = self.transactions_tree.item(item)['text']
                self.db.delete_transaction(int(trans_id))
            
            self.refresh_data()
            messagebox.showinfo("Success", "Transaction deleted successfully!")
    
    def set_this_month(self):
        """Set date range to this month"""
        today = datetime.now()
        self.start_date = today.replace(day=1).strftime("%Y-%m-%d")
        self.end_date = today.strftime("%Y-%m-%d")
        self.refresh_data()
    
    def set_this_year(self):
        """Set date range to this year"""
        today = datetime.now()
        self.start_date = today.replace(month=1, day=1).strftime("%Y-%m-%d")
        self.end_date = today.strftime("%Y-%m-%d")
        self.refresh_data()
    
    def set_last_30_days(self):
        """Set date range to last 30 days"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        self.start_date = start_date.strftime("%Y-%m-%d")
        self.end_date = end_date.strftime("%Y-%m-%d")
        self.refresh_data()
    
    def refresh_data(self):
        """Refresh all data displays"""
        if not hasattr(self, 'start_date'):
            self.set_this_month()
        
        self.refresh_dashboard()
        self.refresh_transactions()
    
    def refresh_dashboard(self):
        """Refresh dashboard summary"""
        summary = self.db.get_summary(self.start_date, self.end_date)
        
        self.income_label.config(text=f"₹{summary['income']:,.2f}")
        self.expense_label.config(text=f"₹{summary['expense']:,.2f}")
        balance = summary['balance']
        balance_text = self.balance_label
        balance_text.config(text=f"₹{balance:,.2f}")
        
        # Update recent transactions
        self.dashboard_tree.delete(*self.dashboard_tree.get_children())
        transactions = self.db.get_transactions(limit=5)
        
        for trans in transactions:
            amount_color = "green" if trans['type'] == "income" else "red"
            self.dashboard_tree.insert("", "end", text=trans['id'],
                                      values=(trans['date'], trans['category'],
                                             trans['type'].capitalize(),
                                            f"₹{trans['amount']:.2f}",
                                             trans['description']))
    
    def refresh_transactions(self):
        """Refresh transactions list"""
        self.transactions_tree.delete(*self.transactions_tree.get_children())
        
        transactions = self.db.get_transactions_by_date_range(self.start_date, 
                                                             self.end_date)
        
        filter_type = self.filter_var.get()
        
        for trans in transactions:
            if filter_type != "All" and trans['type'].lower() != filter_type.lower():
                continue
            
            self.transactions_tree.insert("", "end", text=trans['id'],
                                         values=(trans['date'], trans['category'],
                                                trans['type'].capitalize(),
                                                f"₹{trans['amount']:.2f}",
                                                trans['description']))
    
    def show_income_expense_chart(self):
        """Display income vs expense chart"""
        summary = self.db.get_summary(self.start_date, self.end_date)
        
        # Clear previous chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
        
        # Create figure
        fig = Figure(figsize=(8, 5), dpi=100)
        ax = fig.add_subplot(111)
        
        categories = ['Income', 'Expense']
        values = [summary['income'], summary['expense']]
        colors = ['#16A34A', '#DC2626']
        
        bars = ax.bar(categories, values, color=colors, alpha=0.7, edgecolor='black')
        ax.set_ylabel('Amount (₹)', fontsize=12)
        ax.set_title('Income vs Expenses', fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'₹{value:,.2f}', ha='center', va='bottom', fontweight='bold')
        
        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def show_category_chart(self):
        """Display category breakdown chart"""
        category_summary = self.db.get_category_summary(self.start_date, 
                                                       self.end_date)
        
        # Clear previous chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
        
        if not category_summary:
            messagebox.showinfo("No Data", "No transactions found for the selected period")
            return
        
        # Create figure
        fig = Figure(figsize=(10, 5), dpi=100)
        ax = fig.add_subplot(111)
        
        categories = list(category_summary.keys())
        expenses = [category_summary[cat]['expense'] for cat in categories]
        incomes = [category_summary[cat]['income'] for cat in categories]
        
        x = range(len(categories))
        width = 0.35
        
        ax.bar([i - width/2 for i in x], incomes, width, label='Income', 
              color='#16A34A', alpha=0.7)
        ax.bar([i + width/2 for i in x], expenses, width, label='Expense', 
              color='#DC2626', alpha=0.7)
        
        ax.set_ylabel('Amount (₹)', fontsize=12)
        ax.set_title('Expenses and Income by Category', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(categories, rotation=45, ha='right')
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def show_monthly_chart(self):
        """Display monthly trend chart"""
        # Get last 12 months of data
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)

        # Clear previous chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(12, 5), dpi=100)
        ax = fig.add_subplot(111)

        # Prepare monthly data
        monthly_data = {}
        current_date = start_date
        while current_date <= end_date:
            month_key = current_date.strftime("%Y-%m")
            monthly_data[month_key] = {'income': 0, 'expense': 0}
            current_date += timedelta(days=1)

        # Aggregate transactions
        transactions = self.db.get_transactions_by_date_range(
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d")
        )

        for trans in transactions:
            month_key = trans['date'][:7]
            if month_key in monthly_data:
                if trans['type'] == 'income':
                    monthly_data[month_key]['income'] += trans['amount']
                else:
                    monthly_data[month_key]['expense'] += trans['amount']

        months = sorted(monthly_data.keys())
        incomes = [monthly_data[m]['income'] for m in months]
        expenses = [monthly_data[m]['expense'] for m in months]

        ax.plot(months, incomes, marker='o', label='Income', color='#16A34A', linewidth=2)
        ax.plot(months, expenses, marker='s', label='Expense', color='#DC2626', linewidth=2)

        ax.set_ylabel('Amount (₹)', fontsize=12)
        ax.set_xlabel('Month', fontsize=12)
        ax.set_title('Monthly Income and Expense Trend', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(alpha=0.3)

        # Rotate x labels
        fig.autofmt_xdate()
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def main():
    root = tk.Tk()
    app = PersonalFinanceTracker(root)
    root.mainloop()


if __name__ == "__main__":
    main()
