"""Manage Transaction Page Module"""
import locale
from datetime import date
from typing import Optional, List, Any

import flet as ft

import src.database as db
from src.model import Transaction
from src.ui.forms import TransactionsForms

locale.setlocale(locale.LC_ALL, "id_ID")


class TransactionRow(ft.DataRow):
    def __init__(
        self,
        transaction_data: Transaction,
        on_edit: Any,
        on_delete: Any,
        row_idx: int,
        **kwargs,
    ):
        self.ref = ft.Ref[ft.DataRow]()
        self.row_idx = row_idx
        self.transaction_data = transaction_data
        self._on_edit = on_edit
        self._on_delete = on_delete
        super().__init__(
            ref=self.ref,
            cells=self.create_cells(),
            **kwargs,
        )

    def create_cells(self):
        return [
            ft.DataCell(
                ft.Text(
                    value=self.transaction_data.category,
                    text_align=ft.TextAlign.CENTER,
                    color="#707EAF",
                    weight=ft.FontWeight.W_600,
                )
            ),
            ft.DataCell(
                ft.Text(
                    value=self.transaction_data.date.strftime("%x"),
                    text_align=ft.TextAlign.CENTER,
                    color="#707EAF",
                    weight=ft.FontWeight.W_600,
                )
            ),
            ft.DataCell(
                ft.Text(
                    value=locale.currency(self.transaction_data.amount, grouping=True),
                    text_align=ft.TextAlign.CENTER,
                    color="#707EAF",
                    weight=ft.FontWeight.W_600,
                )
            ),
            ft.DataCell(
                ft.Image(
                    src="images/notes.svg",
                    tooltip=self.transaction_data.notes,
                )
            ),
            ft.DataCell(
                ft.Text(
                    value=self.transaction_data.type,
                    text_align=ft.TextAlign.CENTER,
                    color="#F2428A" if self.transaction_data.type == "Expense" else "#0ADEA6",
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
                            on_click=self._on_edit,
                            data=self,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_ROUNDED,
                            icon_color="red",
                            on_click=self._on_delete,
                            data=self,
                        ),
                    ],
                ),
            ),
        ]


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
        self.transactions.pop(event.control.data.row_idx)
        self.table_ref.current.rows.pop(event.control.data.row_idx)
        self.controls = [self.build()]
        self.update()

    def edit_transaction(self, event: ft.ControlEvent):
        """Event handler on transaction data edit"""
        add_transaction = self.form_ref.current.on_submit

        def update_row(event2: ft.ControlEvent):
            event.control.data.transaction_data = event2.control.data
            event.control.data.ref.current.cells = event.control.data.create_cells()
            event.control.data.ref.current.update()
            self.form_ref.current.default_values = None
            self.form_ref.current.title = "Add Transaction"
            self.form_ref.current.on_submit = add_transaction
            self.form_ref.current.controls = [self.form_ref.current.build()]
            self.form_ref.current.update()

        self.form_ref.current.default_values = event.control.data.transaction_data
        self.form_ref.current.title = "Edit Transaction"
        self.form_ref.current.on_submit = update_row
        self.form_ref.current.controls = [self.form_ref.current.build()]
        self.form_ref.current.update()

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
                                                TransactionRow(
                                                    transaction_data=transaction,
                                                    row_idx=i,
                                                    on_delete=self.delete_row,
                                                    on_edit=self.edit_transaction,
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
            spacing=24,
            controls=[
                TransactionsForms(
                    ref=self.form_ref,
                    on_submit=self.add_transaction,
                    title="Add Transaction",
                ),
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
            ],
        )
