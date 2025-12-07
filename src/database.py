import sqlite3
from datetime import datetime
from typing import List, Tuple, Optional

class FinanceDatabase:
    """Database layer for managing finance transactions"""
    
    def __init__(self, db_path: str = "finance_tracker.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database with required tables"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create transactions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL,
                    type TEXT NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create budget table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS budgets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT UNIQUE NOT NULL,
                    limit_amount REAL NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create categories table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    type TEXT NOT NULL
                )
            """)
            
            conn.commit()
            self._initialize_default_categories()
    
    def _initialize_default_categories(self):
        """Initialize default expense and income categories"""
        default_categories = [
            ("Food & Dining", "expense"),
            ("Transportation", "expense"),
            ("Utilities", "expense"),
            ("Entertainment", "expense"),
            ("Shopping", "expense"),
            ("Health", "expense"),
            ("Education", "expense"),
            ("Other Expenses", "expense"),
            ("Salary", "income"),
            ("Freelance", "income"),
            ("Investment", "income"),
            ("Other Income", "income"),
        ]
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            for category, cat_type in default_categories:
                try:
                    cursor.execute("INSERT INTO categories (name, type) VALUES (?, ?)",
                                 (category, cat_type))
                except sqlite3.IntegrityError:
                    pass
            conn.commit()
    
    def add_transaction(self, date: str, category: str, amount: float, 
                       trans_type: str, description: str = "") -> int:
        """Add a new transaction"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO transactions (date, category, amount, type, description)
                VALUES (?, ?, ?, ?, ?)
            """, (date, category, amount, trans_type, description))
            conn.commit()
            return cursor.lastrowid
    
    def get_transactions(self, limit: int = 100, offset: int = 0) -> List[dict]:
        """Get all transactions with pagination"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM transactions 
                ORDER BY date DESC 
                LIMIT ? OFFSET ?
            """, (limit, offset))
            return [dict(row) for row in cursor.fetchall()]
    
    def get_transactions_by_date_range(self, start_date: str, end_date: str) -> List[dict]:
        """Get transactions within a date range"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM transactions 
                WHERE date BETWEEN ? AND ? 
                ORDER BY date DESC
            """, (start_date, end_date))
            return [dict(row) for row in cursor.fetchall()]
    
    def update_transaction(self, trans_id: int, date: str, category: str, 
                          amount: float, trans_type: str, description: str = ""):
        """Update an existing transaction"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE transactions 
                SET date=?, category=?, amount=?, type=?, description=?
                WHERE id=?
            """, (date, category, amount, trans_type, description, trans_id))
            conn.commit()
    
    def delete_transaction(self, trans_id: int):
        """Delete a transaction"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM transactions WHERE id=?", (trans_id,))
            conn.commit()
    
    def get_categories(self, cat_type: str = None) -> List[str]:
        """Get all categories, optionally filtered by type"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if cat_type:
                cursor.execute("SELECT name FROM categories WHERE type=? ORDER BY name",
                             (cat_type,))
            else:
                cursor.execute("SELECT name FROM categories ORDER BY name")
            return [row[0] for row in cursor.fetchall()]
    
    def get_summary(self, start_date: str, end_date: str) -> dict:
        """Get financial summary for date range"""
        transactions = self.get_transactions_by_date_range(start_date, end_date)
        
        income = sum(t['amount'] for t in transactions if t['type'] == 'income')
        expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
        balance = income - expense
        
        return {
            'income': income,
            'expense': expense,
            'balance': balance,
            'transactions_count': len(transactions)
        }
    
    def get_category_summary(self, start_date: str, end_date: str) -> dict:
        """Get summary grouped by category"""
        transactions = self.get_transactions_by_date_range(start_date, end_date)
        summary = {}
        
        for trans in transactions:
            category = trans['category']
            if category not in summary:
                summary[category] = {'expense': 0, 'income': 0}
            
            if trans['type'] == 'income':
                summary[category]['income'] += trans['amount']
            else:
                summary[category]['expense'] += trans['amount']
        
        return summary
    
    def set_budget(self, category: str, limit: float):
        """Set or update budget for a category"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO budgets (category, limit_amount)
                VALUES (?, ?)
            """, (category, limit))
            conn.commit()
    
    def get_budgets(self) -> dict:
        """Get all budget limits"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT category, limit_amount FROM budgets")
            return {row['category']: row['limit_amount'] for row in cursor.fetchall()}
