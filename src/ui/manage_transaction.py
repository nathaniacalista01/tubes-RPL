"""Manage Transaction Page Module"""
import datetime
from src.ui.dashboard import WelcomeMessage

from flet_core import (
    UserControl,
    PieChart,
    Container,
    Column,
    PieChartSection,
    Padding,
    Text,
    ScrollMode,
    Row,
    Icon,
    alignment,DataTable, DataRow,DataColumn,DataCell, TextAlign,FontWeight, Image
)
class History(UserControl):
    def __init__(
        self,
        icon: str = "attach_money",
        title: str = "payment",
        date: datetime = datetime.date.today(),
        nominal: float = 0.0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.icon = icon
        self.title = title
        self.date = date
        self.nominal = nominal

    def build(self):
        return Row(
            controls=[
                Icon(name=self.icon, size=30),
                Column(
                    spacing=2,
                    controls=[
                        Text(value=self.title, size=15),
                        Text(value=self.date.strftime("%B %d, %Y"), size=10),
                    ],
                ),
                Container(
                    alignment=alignment.center_right,
                    content=Text(value="$" + str(self.nominal), size=15),
                ),
            ],
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

class TransactionsDiagram(UserControl):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def build(self):
        return(
            Container(
                content=Row(
                    controls=[
                        Container(
                            content=PieChart(
                                center_space_radius=40,
                                sections=[
                                    PieChartSection(
                                        value=31.8,
                                        title="31.8%",
                                        color="red",
                                        radius=70,
                                    ),
                                    PieChartSection(
                                        value=18.2,
                                        title="18.2%",
                                        color="yellow",
                                        radius=70,
                                    ),
                                    PieChartSection(
                                        value=22.7,
                                        title="22.7%",
                                        color="blue",
                                        radius=70,
                                    ),
                                    PieChartSection(
                                        value=27.3,
                                        title="27.3%",
                                        color="green",
                                        radius=70,
                                    ),
                                ],
                            ),
                        ),
                        Container(
                            expand=True,
                            bgcolor="white",
                            padding=Padding(20, 20, 20, 20),
                            border_radius=20,
                            content=Row(
                                controls=[
                                    Column(
                                        expand=True,
                                        controls=[
                                            Text("History", size=30),
                                            Column(
                                                scroll=ScrollMode.AUTO,
                                                expand=True,
                                                spacing=5,
                                                controls=[
                                                    History(),
                                                    History(),
                                                    History(),
                                                    History(),
                                                    History(),
                                                    History(),
                                                    History(),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ]
                )
            )
        )

class ManageTransaction(UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Column(
            spacing=0,
            controls=[
                RecentTransactions()
            ],
        )



