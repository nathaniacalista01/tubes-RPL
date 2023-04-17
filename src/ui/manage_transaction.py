"""Manage Transaction Page Module"""
import locale
from datetime import date
from typing import Optional, List

import flet as ft

import src.database as db
from src.model import Transaction
from src.ui.forms import TransactionsForms

locale.setlocale(locale.LC_ALL, "id_ID")


class RecentTransactions(ft.UserControl):
    """Recent Transactions's Card"""

    def __init__(
        self,
        transactions: Optional[List[Transaction]] = None,
        form_ref: Optional[ft.Ref[TransactionsForms]] = None,
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
        self.form_ref = form_ref

    def delete_row(self, event: ft.ControlEvent):
        """Function to delete row"""
        self.transactions.pop(event.control.data)
        self.table_ref.current.rows.pop(event.control.data)
        self.controls = [self.build()]
        self.update()

    def edit_transaction(self, evt: ft.ControlEvent):
        """Event handler on transaction data edit"""

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
                                ft.ListView(
                                    expand=True,
                                    controls=[
                                        ft.DataTable(
                                            ref=self.table_ref,
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
                                                                value=transaction.date.strftime(
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
                                                                        on_click=self.edit_transaction,
                                                                        data=(
                                                                            i,
                                                                            transaction,
                                                                        ),
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

    def __init__(self, db_ref: ft.Ref[db.DatabaseManager], **kwargs):
        super().__init__(**kwargs)
        self.form_ref = ft.Ref[TransactionsForms]()
        self.db_ref = db_ref

    def add_transaction(self, event: ft.ControlEvent):
        """Function to insert new transaction into database"""
        data: Transaction = event.control.data
        database = self.db_ref.current
        if data.type == "Expense":
            table_name = database.pengeluaran.name
        else:
            table_name = database.pemasukan.name
        inserted_data = database.insert_data(
            table_name=table_name,
            columns=["nominal", "tanggal", "kategori", "catatan"],
            values=[
                data.amount,
                data.date,
                data.category,
                data.notes,
            ],
            returning=True,
        )
        database.insert_data(
            table_name=database.transaksi.name,
            columns=["tipe_transaksi", "id_sumber"],
            values=[
                "Pengeluaran" if data.type == "Expense" else "Pemasukan",
                inserted_data[0],
            ],
        )

    def build(self):
        return ft.Column(
            spacing=0,
            controls=[
                RecentTransactions(
                    expand=1,
                    transactions=[
                        Transaction(
                            category="Shopping",
                            date=date.today(),
                            amount=65000,
                            type="Expense",
                            notes="Belanja IPhone di Singapura",
                        )
                        for _ in range(10)
                        # Transaction(
                        #     category="Utilities",
                        #     time=date.today(),
                        #     amount=46000,
                        #     type="Income",
                        #     notes="",
                        # ),
                    ],
                    form_ref=self.form_ref,
                ),
                TransactionsForms(
                    ref=self.form_ref,
                    on_submit=self.add_transaction,
                    expand=1,
                ),
            ],
        )
