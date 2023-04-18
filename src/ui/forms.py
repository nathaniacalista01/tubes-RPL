"""Components for creating transactions forms"""
from datetime import date
from typing import Optional, Any

import flet as ft
from src import model


class TransactionsForms(ft.UserControl):
    """Forms to add new transactions"""

    def __init__(
        self,
        ref: Optional[ft.Ref["TransactionsForms"]] = None,
        on_submit: Any = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.category_field = ft.Ref[ft.TextField]()
        self.amount_field = ft.Ref[ft.TextField]()
        self.notes_field = ft.Ref[ft.TextField]()
        self.type_dropdown = ft.Ref[ft.Dropdown]()
        self.ref = ref
        self.on_submit = on_submit
        self.valid = False

    @staticmethod
    def dropdown(name: str, ref=Optional[ft.Ref[ft.Dropdown]]):
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
                        value="Add Transactions",
                        size=32,
                        weight=ft.FontWeight.W_600,
                    ),
                    ft.Row(
                        controls=[self.new_forms(name="Notes", ref=self.notes_field)]
                    ),
                    ft.Row(
                        controls=[
                            self.new_forms(
                                name="Amount",
                                ref=self.amount_field,
                                kbd_type=ft.KeyboardType.NUMBER,
                                on_change=self.validate,
                            ),
                            self.new_forms(name="Category", ref=self.category_field),
                            self.dropdown(name="Type", ref=self.type_dropdown),
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
                                on_click=self.submit,
                                disabled=self.valid,
                            ),
                        ],
                    ),
                ],
            ),
        )
