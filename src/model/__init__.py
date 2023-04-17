from dataclasses import dataclass
from datetime import date
from typing import Literal, Union


@dataclass
class Transaction:
    """Transaction model"""

    category: str
    time: date
    amount: float
    notes: str
    type: Literal["Expense", "Income"]
