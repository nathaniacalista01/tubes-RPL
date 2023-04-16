"""Manage Transaction Page Module"""

from flet_core import (
    UserControl,
    Container,
    Column,
    Padding,
    Text,
    Row,
    DataTable,
    DataRow,
    DataColumn,
    DataCell,
    TextAlign,
    FontWeight,
    Image,
)


class RecentTransactions(UserControl):
    """Recent Transactions's Card"""

    def __init__(
        self,
        title: str = "Recent Transactions",
        column_two: str = "Category",
        column_three: str = "Transaction\nTime",
        column_four: str = "Transaction\nAmount",
        column_five: str = "Notes",
        column_six: str = "Type",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.title = (title,)
        self.column_two = column_two
        self.column_three = column_three
        self.column_four = column_four
        self.column_five = column_five
        self.column_six = column_six

    def build(self):
        return Container(
            padding=Padding(20, 30, 20, 10),
            border_radius=20,
            bgcolor="#FFFFFF",
            content=Row(
                controls=[
                    Container(
                        expand=True,
                        content=Column(
                            controls=[
                                Text(
                                    value="Recent Transactions",
                                    size=32,
                                    weight=FontWeight.W_600,
                                ),
                                Row(
                                    controls=[
                                        DataTable(
                                            expand=True,
                                            bgcolor="#F6F3F3",
                                            border_radius=20,
                                            columns=[
                                                DataColumn(
                                                    label=Text(
                                                        value=self.column_two,
                                                        text_align=TextAlign.CENTER,
                                                        color="#707EAF",
                                                        weight=FontWeight.W_700,
                                                    )
                                                ),
                                                DataColumn(
                                                    label=Text(
                                                        value=self.column_three,
                                                        text_align=TextAlign.CENTER,
                                                        color="#707EAF",
                                                        weight=FontWeight.W_700,
                                                    )
                                                ),
                                                DataColumn(
                                                    label=Text(
                                                        value=self.column_four,
                                                        text_align=TextAlign.CENTER,
                                                        color="#707EAF",
                                                        weight=FontWeight.W_700,
                                                    )
                                                ),
                                                DataColumn(
                                                    label=Text(
                                                        value=self.column_five,
                                                        text_align=TextAlign.CENTER,
                                                        color="#707EAF",
                                                        weight=FontWeight.W_700,
                                                    )
                                                ),
                                                DataColumn(
                                                    label=Text(
                                                        value=self.column_six,
                                                        text_align=TextAlign.CENTER,
                                                        color="#707EAF",
                                                        weight=FontWeight.W_700,
                                                    )
                                                ),
                                            ],
                                            rows=[
                                                DataRow(
                                                    cells=[
                                                        DataCell(
                                                            Text(
                                                                value="shopping",
                                                                text_align=TextAlign.CENTER,
                                                                color="#707EAF",
                                                                weight=FontWeight.W_600,
                                                            )
                                                        ),
                                                        DataCell(
                                                            Text(
                                                                value="12:28:16 PM",
                                                                text_align=TextAlign.CENTER,
                                                                color="#707EAF",
                                                                weight=FontWeight.W_600,
                                                            )
                                                        ),
                                                        DataCell(
                                                            Text(
                                                                value="Rp 69.000,00",
                                                                text_align=TextAlign.CENTER,
                                                                color="#707EAF",
                                                                weight=FontWeight.W_600,
                                                            )
                                                        ),
                                                        DataCell(
                                                            Image(
                                                                src="images/notes.svg"
                                                            )
                                                        ),
                                                        DataCell(
                                                            Text(
                                                                value="Expense",
                                                                text_align=TextAlign.CENTER,
                                                                color="#F2428A",
                                                                weight=FontWeight.W_600,
                                                            )
                                                        ),
                                                    ]
                                                ),
                                                DataRow(
                                                    cells=[
                                                        DataCell(
                                                            Text(
                                                                value="Utilities",
                                                                text_align=TextAlign.CENTER,
                                                                color="#707EAF",
                                                                weight=FontWeight.W_600,
                                                            )
                                                        ),
                                                        DataCell(
                                                            Text(
                                                                value="7:34:13 AM",
                                                                text_align=TextAlign.CENTER,
                                                                color="#707EAF",
                                                                weight=FontWeight.W_600,
                                                            )
                                                        ),
                                                        DataCell(
                                                            Text(
                                                                value="Rp 55.000,00",
                                                                text_align=TextAlign.CENTER,
                                                                color="#707EAF",
                                                                weight=FontWeight.W_600,
                                                            )
                                                        ),
                                                        DataCell(
                                                            Image(
                                                                src="images/notes.svg"
                                                            )
                                                        ),
                                                        DataCell(
                                                            Text(
                                                                value="Income",
                                                                text_align=TextAlign.CENTER,
                                                                color="#0ADEA6",
                                                                weight=FontWeight.W_600,
                                                            )
                                                        ),
                                                    ]
                                                ),
                                            ],
                                        )
                                    ]
                                ),
                            ],
                        ),
                    )
                ]
            ),
        )


class ManageTransaction(UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Column(
            spacing=0,
            controls=[RecentTransactions()],
        )
