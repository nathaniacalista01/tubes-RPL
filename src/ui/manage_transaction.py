"""Manage Transaction Page Module"""
import datetime
import locale
from typing import Optional, List, Any

import flet as ft

import src.database as db
from src.model import Transaction
from src.ui.forms import TransactionsForms

locale.setlocale(locale.LC_ALL, "id_ID")


class TransactionRow(ft.DataRow):
    """Row for transaction"""

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
        """Function to create cells"""
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
                    value=self.transaction_data.date.strftime("%Y-%m-%d"),
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
                    color="#F2428A"
                    if self.transaction_data.type == "Expense"
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
        on_delete: Any = None,
        on_edit: Any = None,
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
        self.on_delete = on_delete
        self.on_edit = on_edit

    def create_edit_form(self, event: ft.ControlEvent):
        """Event handler on transaction data edit"""
        add_transaction = self.form_ref.current.on_submit

        def update_row(event2: ft.ControlEvent):
            event.control.data.transaction_data = event2.control.data
            event.control.data.ref.current.cells = event.control.data.create_cells()
            event.control.data.ref.current.update()
            self.form_ref.current.default_values = None
            self.form_ref.current.title = "Add Transaction"
            self.form_ref.current.on_submit = add_transaction
            self.form_ref.current.disable_dropdown = False
            self.form_ref.current.controls = [self.form_ref.current.build()]
            self.form_ref.current.update()
            self.on_edit(event2)

        self.form_ref.current.default_values = event.control.data.transaction_data
        self.form_ref.current.title = "Edit Transaction"
        self.form_ref.current.on_submit = update_row
        self.form_ref.current.disable_dropdown = True
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
                                                    on_delete=self.on_delete,
                                                    on_edit=self.create_edit_form,
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
        self.type = ""
        self.transactions_expense = db_ref.current.fetch_data("transaksi_pengeluaran")
        self.transactions_income = db_ref.current.fetch_data("transaksi_pemasukan")
        self.transactions = []
        for rows in self.transactions_expense:
            new = Transaction(
                id_transaksi=rows["id_transaksi"],
                id_sumber=rows["id_pengeluaran"],
                category=rows["kategori"],
                date=datetime.datetime.strptime(rows["tanggal"], "%Y-%m-%d").date(),
                amount=rows["nominal"],
                notes=rows["catatan"],
                type="Expense",
            )
            self.transactions.append(new)
        for rows in self.transactions_income:
            new = Transaction(
                id_transaksi=rows["id_transaksi"],
                id_sumber=rows["id_pemasukan"],
                category=rows["kategori"],
                date=datetime.datetime.strptime(rows["tanggal"], "%Y-%m-%d").date(),
                amount=rows["nominal"],
                notes=rows["catatan"],
                type="Income",
            )
            self.transactions.append(new)

    def fetch_data(self):
        """Procedure to fetch data from database"""
        self.transactions_expense = self.db_ref.current.fetch_data(
            "transaksi_pengeluaran"
        )
        self.transactions_income = self.db_ref.current.fetch_data("transaksi_pemasukan")
        self.update()

    def add_transactions_list(self):
        """Add new transactions into transactions list"""
        if self.type == "Income":
            income_data = self.transactions_income[len(self.transactions_income) - 1]
            new_income = Transaction(
                id_transaksi=income_data["id_transaksi"],
                id_sumber=income_data["id_pemasukan"],
                category=income_data["kategori"],
                date=datetime.datetime.strptime(
                    income_data["tanggal"], "%Y-%m-%d"
                ).date(),
                amount=income_data["nominal"],
                notes=income_data["catatan"],
                type="Income",
            )
            self.transactions.append(new_income)
        else:
            last_data = self.transactions_expense[len(self.transactions_expense) - 1]

            new = Transaction(
                id_transaksi=last_data["id_transaksi"],
                id_sumber=last_data["id_pengeluaran"],
                category=last_data["kategori"],
                date=datetime.datetime.strptime(
                    last_data["tanggal"], "%Y-%m-%d"
                ).date(),
                amount=last_data["nominal"],
                notes=last_data["catatan"],
                type="Expense",
            )
            self.transactions.append(new)
        self.controls = [self.build()]
        self.update()

    def add_transaction(self, event: ft.ControlEvent):
        """Function to edit existing transaction in database"""
        data: Transaction = event.control.data
        database = self.db_ref.current
        self.type = data.type
        if self.type == "Expense":
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
        self.fetch_data()
        self.add_transactions_list()

    def edit_transaction(self, event: ft.ControlEvent):
        """Function to insert new transaction into database"""
        data: Transaction = event.control.data
        database = self.db_ref.current
        self.type = data.type
        if self.type == "Expense":
            table_name = database.pengeluaran.name
            condition = f"id_pengeluaran = {data.id_sumber}"
        else:
            table_name = database.pemasukan.name
            condition = f"id_pemasukan = {data.id_sumber}"
        database.update_data(
            table_name=table_name,
            columns=["nominal", "tanggal", "kategori", "catatan"],
            values=[
                data.amount,
                data.date,
                data.category,
                data.notes,
            ],
            condition=condition,
        )
        self.fetch_data()

    def delete_row(self, event: ft.ControlEvent):
        """Function to delete row"""
        deleted_item = self.transactions.pop(event.control.data.row_idx)
        transactions_query = "id_transaksi="
        self.db_ref.current.delete_data(
            "Transaksi", f"{transactions_query}{deleted_item.id_transaksi}"
        )
        if deleted_item.type == "Expense":
            expense_query = "id_pengeluaran="
            self.db_ref.current.delete_data(
                "Pengeluaran", f"{expense_query}{deleted_item.id_sumber}"
            )
        else:
            income_query = "id_pemasukan="
            self.db_ref.current.delete_data(
                "Pemasukan", f"{income_query}{deleted_item.id_sumber}"
            )
        self.controls = [self.build()]
        self.update()

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
                    transactions=self.transactions,
                    form_ref=self.form_ref,
                    on_delete=self.delete_row,
                    on_edit=self.edit_transaction,
                ),
            ],
        )
