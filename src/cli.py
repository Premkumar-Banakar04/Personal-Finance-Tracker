from db import get_conn
from datetime import datetime

def add_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: "))
    category = input("Category: ")
    ttype = input("Type (income/expense): ")
    note = input("Note (optional): ")

    with get_conn() as conn:
        conn.execute("""
            INSERT INTO transactions(date, amount, category, type, note)
            VALUES(?, ?, ?, ?, ?)
        """, (date, amount, category, ttype, note))

    print("✔ Transaction added successfully!")


def list_transactions():
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM transactions").fetchall()

    print("\n=== All Transactions ===")
    for r in rows:
        print(f"{r['id']}. {r['date']} - {r['category']} - {r['type']} - ₹{r['amount']} - {r['note']}")


def delete_transaction():
    tid = input("Enter transaction ID to delete: ")

    with get_conn() as conn:
        conn.execute("DELETE FROM transactions WHERE id = ?", (tid,))

    print("✔ Transaction deleted!")
