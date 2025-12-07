from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
    id: int | None
    date: datetime
    amount: float
    category: str
    type: str  # income or expense
    note: str = ""
