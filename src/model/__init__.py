"""Budgetwise's models"""

from dataclasses import dataclass
from datetime import date
from typing import Literal


@dataclass
class Transaction:
    """Transaction model"""

    id_transaksi: int
    id_sumber: int
    category: str
    date: date
    amount: float
    notes: str
    type: Literal["Expense", "Income"]


@dataclass
class Target:
    """Target model"""

    id_target: int
    judul: str
    nominal_target: int
    catatan: str
    tanggal_dibuat: date
    tanggal_tercapai: date
