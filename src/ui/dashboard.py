"""Component for BudgetWise's dashboard"""
from typing import Optional, List

import matplotlib
import matplotlib.pyplot as plt
from flet_core import (
    alignment,
    UserControl,
    Ref,
    ControlEvent,
    Text,
    Container,
    Column,
    Row,
    ButtonStyle,
    MaterialState,
    Margin,
    FontWeight,
    Padding,
    Image,
    MainAxisAlignment,
    LineChartData,
    LineChartDataPoint,
    colors,
    LineChart,
    ScrollMode,
    Stack,
    OutlinedButton,
)
from flet_core.matplotlib_chart import MatplotlibChart

from src.ui.target import Target_Box

matplotlib.use("svg")


class WelcomeMessage(UserControl):
    """Welcome Message Component in Dashboard"""

    def __init__(self, welcome_str: str = "Hello, Jane Doe", **kwargs):
        super().__init__(**kwargs)
        self.welcome_message = welcome_str

    def build(self):
        return Column(
            spacing=0,
            controls=[
                Text(
                    value=self.welcome_message,
                    size=32,
                    weight=FontWeight.W_600,
                ),
                Text(
                    value="4.45 pm 15 April 2023",
                    weight=FontWeight.W_600,
                    size=13,
                ),
            ],
        )


class SaldoCard(UserControl):
    """Saldo Card Components in dashboard"""

    def __init__(
        self,
        title: str = "Balances",
        total_income: str = "Total Income",
        total_expense: str = "Total Expense",
        total_balance: str = "Total Balance",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.title = title
        self.total_income = total_income
        self.total_expense = total_expense
        self.total_balance = total_balance

    def build(self):
        return Container(
            bgcolor="#FFFFFF",
            padding=Padding(20, 30, 20, 0),
            border_radius=20,
            content=Row(
                controls=[
                    Column(
                        spacing=0,
                        controls=[
                            Text(
                                value=self.title,
                                size=32,
                                weight=FontWeight.W_600,
                            ),
                            Text(
                                value=self.total_income,
                                size=18,
                                color="#793DFD",
                            ),
                            # Masukin Jumlah Pemasukan
                            Text(
                                value="6.025.440,00",
                                size=18,
                                weight=FontWeight.W_600,
                            ),
                            Text(
                                value=self.total_expense,
                                size=18,
                                color="#793DFD",
                            ),
                            # Jumlah pengeluaran
                            Text(
                                value="4.502.440,00",
                                size=18,
                                weight=FontWeight.W_600,
                            ),
                            Text(
                                value=self.total_balance,
                                size=18,
                                color="#793DFD",
                            ),
                            Text(
                                value="2.000.000,00",
                                size=18,
                                weight=FontWeight.W_600,
                            ),
                        ],
                    ),
                ]
            ),
        )


class FirstRow(UserControl):
    """First row in Saldo Overview Components"""

    def __init__(
        self,
        title: str,
        labels: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.title = title
        self.labels = labels
        self.selected_index = 0
        self.refs = [Ref[OutlinedButton]() for _ in labels]

    def select_item(self, e: ControlEvent):
        e.control.disabled = True
        self.refs[self.selected_index].current.disabled = False
        self.selected_index = e.control.data
        self.update()

    def build(self):
        buttons = [
            Container(
                scale=0.75,
                margin=Margin(-5, 0, -5, 0),
                content=OutlinedButton(
                    ref=self.refs[i],
                    style=ButtonStyle(
                        bgcolor={
                            MaterialState.DEFAULT: "white",
                            MaterialState.HOVERED: "blue",
                            MaterialState.DISABLED: "blue",
                        },
                        color="black",
                    ),
                    disabled=(i == self.selected_index),
                    data=i,
                    on_click=self.select_item,
                    text=label,
                ),
            )
            for i, label in enumerate(self.labels)
        ]
        return Row(
            alignment=MainAxisAlignment.END,
            spacing=0,
            controls=[
                Text(
                    expand=True,
                    value=self.title,
                    size=32,
                    weight=FontWeight.W_600,
                ),
                *buttons,
            ],
        )


class SaldoOverviewSecondRow(UserControl):
    """Second row for Saldo Overview Components"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Row(
            alignment=MainAxisAlignment.END,
            controls=[
                Row(
                    expand=True,
                    spacing=2,
                    controls=[
                        Image(src="images/stonks.svg"),
                        Text(value="6.5%", size=12),
                    ],
                ),
                Row(
                    spacing=2,
                    controls=[
                        Image(src="images/green-button.svg"),
                        Text(value="Income"),
                    ],
                ),
                Row(
                    spacing=2,
                    controls=[
                        Image(src="images/purple-button.svg"),
                        Text(value="Expense"),
                    ],
                ),
            ],
        )


class SaldoChart(UserControl):
    """Components for line chart at dashboard"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        data_1 = [
            LineChartData(
                data_points=[
                    LineChartDataPoint(1, 1),
                    LineChartDataPoint(3, 1.5),
                    LineChartDataPoint(5, 1.4),
                    LineChartDataPoint(7, 3.4),
                    LineChartDataPoint(10, 2),
                    LineChartDataPoint(12, 2.2),
                    LineChartDataPoint(13, 1.8),
                ],
                stroke_width=4,
                color="#00DEA3",
                stroke_cap_round=True,
            ),
            LineChartData(
                data_points=[
                    LineChartDataPoint(1, 1),
                    LineChartDataPoint(3, 2.8),
                    LineChartDataPoint(7, 1.2),
                    LineChartDataPoint(10, 2.8),
                    LineChartDataPoint(12, 2.6),
                    LineChartDataPoint(13, 3.9),
                ],
                color=colors.PINK,
                below_line_bgcolor=colors.with_opacity(0, colors.PINK),
                stroke_width=4,
                stroke_cap_round=True,
            ),
        ]
        return LineChart(data_series=data_1)


class SaldoOverview(UserControl):
    """Saldo Overview Components that consist of several rows"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Container(
            padding=Padding(20, 30, 20, 10),
            border_radius=20,
            bgcolor="#FFFFFF",
            content=Column(
                controls=[
                    FirstRow(
                        title="Balance Overview",
                        labels=["All", "1M", "3M", "6M", "1Y"],
                    ),
                    SaldoOverviewSecondRow(),
                    SaldoChart(expand=True),
                ]
            ),
        )


class BalanceRow(UserControl):
    """Row for balance that consist of two cards"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Row(
            spacing=24,
            controls=[
                SaldoOverview(expand=True),
                SaldoCard(width=260),
            ],
        )


class Targets(UserControl):
    """Targets Component in Dashboard"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Container(
            bgcolor="#FFFFFF",
            padding=Padding(20, 30, 20, 10),
            border_radius=20,
            content=Row(
                controls=[
                    Column(
                        controls=[
                            Text(
                                value="Targets",
                                size=32,
                                weight=FontWeight.W_600,
                            ),
                            Column(
                                expand=True,
                                scroll=ScrollMode.AUTO,
                                spacing=5,
                                controls=[
                                    Target_Box(),
                                    Target_Box(),
                                    Target_Box(),
                                    Target_Box(),
                                    Target_Box(),
                                ],
                            ),
                        ]
                    )
                ]
            ),
        )


class TransactionsDiagram(UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sizes = [31.8, 18.2, 22.7, 27.3]
        self.colors = ["#F44336", "#FFEB3B", "#2196F3", "#4CAF50"]
        self.labels = ["Category 1", "Category 2", "Category 3", "Other"]

    def build(self):
        fig, ax = plt.subplots()
        plt.tight_layout(pad=-4.5)
        ax.pie(
            self.sizes,
            colors=self.colors,
            autopct="%1.1f%%",
            pctdistance=0.75,
            textprops={"fontsize": 20},
            wedgeprops={"linewidth": 7, "edgecolor": "white"},
        )
        plt.gcf().gca().add_artist(plt.Circle((0, 0), 0.5, color="white"))
        legend = Column(
            spacing=5,
            controls=[
                Row(
                    spacing=5,
                    controls=[
                        Container(
                            width=13,
                            height=13,
                            bgcolor=color,
                        ),
                        Text(
                            value=label,
                        ),
                    ],
                )
                for label, color in zip(self.labels, self.colors)
            ],
        )
        return Container(
            bgcolor="#FFFFFF",
            padding=Padding(20, 30, 20, 10),
            border_radius=20,
            content=Column(
                controls=[
                    FirstRow(
                        title="Transaction Overview",
                        labels=["Income", "Expense"],
                    ),
                    Stack(
                        expand=True,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                content=MatplotlibChart(fig, expand=True),
                            ),
                            Container(
                                top=0,
                                right=0,
                                alignment=alignment.center,
                                content=legend,
                            ),
                        ],
                    ),
                ],
            ),
        )


class RecentTransactionTarget(UserControl):
    """Row that consist of RecentTransactions and Target"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Row(
            alignment=MainAxisAlignment.END,
            spacing=24,
            controls=[
                TransactionsDiagram(expand=True),
                Targets(width=260),
            ],
        )


class Dashboard(UserControl):
    """Dashboard Component"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Column(
            controls=[
                WelcomeMessage(),
                BalanceRow(expand=1),
                RecentTransactionTarget(expand=1),
            ]
        )
