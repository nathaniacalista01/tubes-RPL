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
        disable_dropdown: bool = False,
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
        self.disable_dropdown = disable_dropdown

    @staticmethod
    def dropdown(
        name: str,
        ref=Optional[ft.Ref[ft.Dropdown]],
        value: Optional[str] = None,
        disable: bool = False,
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
                        # expand=True,
                        value=value,
                        disabled=disable,
                        border_color="transparent",
                        height=55,
                        text_size=13,
                        label_style=ft.TextStyle(size=13),
                        label=name,
                        color="black",
                        content_padding=ft.padding.only(top=14),
                        options=[
                            ft.dropdown.Option("Expense"),
                            ft.dropdown.Option("Income"),
                        ],
                        error_text=ref.current.error_text
                        if ref.current is not None
                        else None,
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
                        height=55,
                        text_size=13,
                        label=name,
                        label_style=ft.TextStyle(size=13),
                        content_padding=ft.padding.only(top=30),
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                        error_text=ref.current.error_text
                        if ref.current is not None
                        else None,
                    )
                ],
            ),
        )

    def submit(self, event: ft.ControlEvent):
        """Methods to submit new transactions"""
        if (
            self.type_dropdown.current.value
            and self.category_field.current.value
            and self.amount_field.current.value.isdigit()
        ):
            event.control.data = model.Transaction(
                id_transaksi=-1
                if self.default_values is None
                else self.default_values.id_transaksi,
                id_sumber=-1
                if self.default_values is None
                else self.default_values.id_sumber,
                type=self.type_dropdown.current.value,
                category=self.category_field.current.value,
                amount=float(self.amount_field.current.value)
                if self.amount_field.current.value != ""
                else 0,
                notes=self.notes_field.current.value,
                date=date.today(),
            )
            self.type_dropdown.current.value = ""
            self.category_field.current.value = ""
            self.amount_field.current.value = ""
            self.on_submit(event)
        else:
            self.type_dropdown.current.error_text = (
                "Please select a type" if not self.type_dropdown.current.value else None
            )
            self.category_field.current.error_text = (
                "Category cannot be empty"
                if not self.category_field.current.value
                else None
            )
            self.amount_field.current.error_text = (
                "Amount must be a number"
                if not self.amount_field.current.value.isdigit()
                else None
            )
            self.controls = [self.build()]
            self.update()

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
                                # on_change=self.validate,
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
                                disable=self.disable_dropdown,
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
