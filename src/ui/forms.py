"""Components for creating transactions forms"""
from datetime import date
from typing import Optional, Any

import flet as ft

from src import model
from src.model import Transaction


class TransactionsForms(ft.UserControl):
    """Forms to add new transactions"""

    def __init__(
        self,
        title: str,
        default_values: Optional[Transaction] = None,
        ref: Optional[ft.Ref["TransactionsForms"]] = None,
        on_submit: Any = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.category_field = ft.Ref[ft.TextField]()
        self.amount_field = ft.Ref[ft.TextField]()
        self.notes_field = ft.Ref[ft.TextField]()
        self.type_dropdown = ft.Ref[ft.Dropdown]()
        self.on_submit = on_submit
        self.valid = False
        self.title = title
        self.default_values = default_values
        self.ref = ref
        self.ref.current = self

    @staticmethod
    def dropdown(
        name: str,
        ref=Optional[ft.Ref[ft.Dropdown]],
        value: Optional[str] = None,
    ):
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
                        ref=ref,
                        value=value,
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
    def new_forms(
        name: str,
        ref: Optional[ft.Ref[ft.TextField]] = None,
        kbd_type: ft.KeyboardType = ft.KeyboardType.TEXT,
        on_change: Any = None,
        value: Optional[str] = None,
    ):
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
                    ft.TextField(
                        ref=ref,
                        value=value,
                        border_color="transparent",
                        keyboard_type=kbd_type,
                        on_change=on_change,
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

    def submit(self, event: ft.ControlEvent):
        """Methods to submit new transactions"""
        event.control.data = model.Transaction(
            type=self.type_dropdown.current.value,
            category=self.category_field.current.value,
            amount=float(self.amount_field.current.value)
            if self.amount_field.current.value != ""
            else 0,
            notes=self.notes_field.current.value,
            date=date.today(),
        )
        self.on_submit(event)

    def validate(self, event: ft.ControlEvent):
        """Function to validate user input for transactions"""
        try:
            float(event.control.value)
        except ValueError:
            self.valid = True

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
                        value=self.title,
                        size=32,
                        weight=ft.FontWeight.W_600,
                    ),
                    ft.Row(
                        controls=[
                            self.new_forms(
                                name="Notes",
                                ref=self.notes_field,
                                value=None
                                if self.default_values is None
                                else self.default_values.notes,
                            ),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            self.new_forms(
                                name="Amount",
                                ref=self.amount_field,
                                kbd_type=ft.KeyboardType.NUMBER,
                                on_change=self.validate,
                                value=None
                                if self.default_values is None
                                else str(self.default_values.amount),
                            ),
                            self.new_forms(
                                name="Category",
                                ref=self.category_field,
                                value=None
                                if self.default_values is None
                                else str(self.default_values.category),
                            ),
                            self.dropdown(
                                name="Type",
                                ref=self.type_dropdown,
                                value=None
                                if self.default_values is None
                                else str(self.default_values.type),
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.ElevatedButton(
                                width=100,
                                bgcolor="#6761B9",
                                color="white",
                                text="Submit",
                                on_click=self.submit,
                            ),
                        ],
                    ),
                ],
            ),
        )
