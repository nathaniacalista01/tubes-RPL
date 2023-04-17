"""Manage Transaction Page Module"""
import locale
from datetime import date
from typing import Optional, List

import flet as ft

from src.model import Transaction
from src.ui.forms import TransactionsForms

locale.setlocale(locale.LC_ALL, "id_ID")


class RecentTransactions(ft.UserControl):
    """Recent Transactions's Card"""

    def __init__(
        self,
        transactions: Optional[List[Transaction]] = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.headers = [
            "Category",
            "Transaction\nTime",
            "Transaction\nAmount",
            "Notes",
            "Type",
            "Action",
        ]
        self.transactions = [] if transactions is None else transactions
        self.table_ref = ft.Ref[ft.DataTable]()

    def delete_row(self, event: ft.ControlEvent):
        """Function to delete row"""
        self.transactions.pop(event.control.data)
        self.table_ref.current.rows.pop(event.control.data)
        self.controls = [self.build()]
        self.update()

    def build(self):
        return ft.Container(
            padding=ft.Padding(20, 10, 20, 10),
            border_radius=20,
            bgcolor="#FFFFFF",
            content=ft.Row(
                controls=[
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    value="Recent Transactions",
                                    size=32,
                                    weight=ft.FontWeight.W_600,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.DataTable(
                                            ref=self.table_ref,
                                            expand=True,
                                            heading_text_style=ft.TextStyle(
                                                weight=ft.FontWeight.W_700,
                                                color="#707EAF",
                                            ),
                                            bgcolor="#F6F3F3",
                                            border_radius=20,
                                            columns=[
                                                ft.DataColumn(
                                                    label=ft.Text(
                                                        value=header,
                                                        text_align=ft.TextAlign.CENTER,
                                                    )
                                                )
                                                for header in self.headers
                                            ],
                                            rows=[
                                                ft.DataRow(
                                                    cells=[
                                                        ft.DataCell(
                                                            ft.Text(
                                                                value=transaction.category,
                                                                text_align=ft.TextAlign.CENTER,
                                                                color="#707EAF",
                                                                weight=ft.FontWeight.W_600,
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                value=transaction.time.strftime(
                                                                    "%x"
                                                                ),
                                                                text_align=ft.TextAlign.CENTER,
                                                                color="#707EAF",
                                                                weight=ft.FontWeight.W_600,
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                value=locale.currency(
                                                                    transaction.amount,
                                                                    grouping=True,
                                                                ),
                                                                text_align=ft.TextAlign.CENTER,
                                                                color="#707EAF",
                                                                weight=ft.FontWeight.W_600,
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Image(
                                                                src="images/notes.svg",
                                                                tooltip=transaction.notes,
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                value=transaction.type,
                                                                text_align=ft.TextAlign.CENTER,
                                                                color="#F2428A"
                                                                if transaction.type
                                                                == "Expense"
                                                                else "#0ADEA6",
                                                                weight=ft.FontWeight.W_600,
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Row(
                                                                spacing=0,
                                                                controls=[
                                                                    ft.IconButton(
                                                                        ft.icons.EDIT,
                                                                        icon_color="amber",
                                                                    ),
                                                                    ft.IconButton(
                                                                        ft.icons.DELETE_ROUNDED,
                                                                        icon_color="red",
                                                                        on_click=self.delete_row,
                                                                        data=i,
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                )
                                                for i, transaction in enumerate(
                                                    self.transactions
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )


class ManageTransaction(ft.UserControl):
    """Component for manage transactions"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Column(
            spacing=0,
            controls=[
                RecentTransactions(
                    expand=1,
                    transactions=[
                        Transaction(
                            category="Shopping",
                            time=date.today(),
                            amount=65000,
                            type="Expense",
                            notes="Belanja IPhone di Singapura",
                        ),
                        Transaction(
                            category="Utilities",
                            time=date.today(),
                            amount=46000,
                            type="Income",
                            notes="",
                        ),
                    ],
                ),
                TransactionsForms(expand=1),
            ],
        )
