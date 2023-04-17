"""Components for creating transactions forms"""
from typing import Optional

import flet as ft


class TransactionsForms(ft.UserControl):
    """Forms to add new transactions"""
    def __init__(
        self,
        ref: Optional[ft.Ref["TransactionsForms"]] = None,
        category: str = "Category",
        amount: str = "Transaction Amount",
        notes: str = "Notes",
        transaction_type: str = "Type",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.category = category
        self.amount = amount
        self.notes = notes
        self.type = transaction_type
        self.ref = ref

    @staticmethod
    def dropdown(name: str):
        """Produce dropdown for transaction type"""
        return ft.Container(
            expand=True,
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            margin=ft.margin.only(top=10),
            padding=ft.padding.all(8),
            content=ft.Column(
                spacing=1,
                controls=[
                    ft.Dropdown(
                        expand=True,
                        border_color="transparent",
                        height=30,
                        text_size=13,
                        label_style=ft.TextStyle(size=13),
                        label=name,
                        color="black",
                        content_padding=ft.padding.only(top=14),
                        options=[
                            ft.dropdown.Option("Expense"),
                            ft.dropdown.Option("Income"),
                        ],
                    )
                ],
            ),
        )

    @staticmethod
    def new_forms(name: str):
        """Component for new input for a form"""
        return ft.Container(
            expand=True,
            height=45,
            bgcolor="#ebebeb",
            border_radius=ft.border_radius.all(6),
            margin=ft.margin.only(top=10),
            padding=ft.padding.all(8),
            content=ft.Column(
                spacing=1,
                controls=[
                    # Text(value=name,size=9,color="black",weight="bold"),
                    ft.TextField(
                        border_color="transparent",
                        height=30,
                        text_size=13,
                        label=name,
                        label_style=ft.TextStyle(size=13),
                        content_padding=ft.padding.only(top=30),
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                    )
                ],
            ),
        )

    def build(self):
        return ft.Container(
            expand=True,
            bgcolor="#FFFFFF",
            border=ft.border.all(1, "#ebebeb"),
            border_radius=20,
            padding=15,
            margin=ft.margin.only(top=10),
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Text(
                        value="Add Transactions",
                        size=32,
                        weight=ft.FontWeight.W_600,
                    ),
                    ft.Row(controls=[self.new_forms(self.notes)]),
                    ft.Row(
                        controls=[
                            self.new_forms(self.amount),
                            self.new_forms(self.category),
                            self.dropdown(self.type),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.ElevatedButton(
                                width=100,
                                bgcolor="#6761B9",
                                color="white",
                                text="Add",
                            ),
                        ],
                    ),
                ],
            ),
        )
