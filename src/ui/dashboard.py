"""Component for BudgetWise's dashboard"""
from typing import Optional, List

import matplotlib
import matplotlib.pyplot as plt

import flet as ft
from flet.matplotlib_chart import MatplotlibChart

from src.ui.target import Target_Box

matplotlib.use("svg")


class WelcomeMessage(ft.UserControl):
    """Welcome Message Component in Dashboard"""

    def __init__(self, welcome_str: str = "Hello, Jane Doe", **kwargs):
        super().__init__(**kwargs)
        self.welcome_message = welcome_str

    def build(self):
        return ft.Column(
            spacing=0,
            controls=[
                ft.Text(
                    value=self.welcome_message,
                    size=32,
                    weight=ft.FontWeight.W_600,
                ),
                ft.Text(
                    value="4.45 pm 15 April 2023",
                    weight=ft.FontWeight.W_600,
                    size=13,
                ),
            ],
        )


class SaldoCard(ft.UserControl):
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
        return ft.Container(
            bgcolor="#FFFFFF",
            padding=ft.Padding(20, 30, 20, 0),
            border_radius=20,
            content=ft.Row(
                controls=[
                    ft.Column(
                        spacing=0,
                        controls=[
                            ft.Text(
                                value=self.title,
                                size=32,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Text(
                                value=self.total_income,
                                size=18,
                                color="#793DFD",
                            ),
                            # Masukin Jumlah Pemasukan
                            ft.Text(
                                value="6.025.440,00",
                                size=18,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Text(
                                value=self.total_expense,
                                size=18,
                                color="#793DFD",
                            ),
                            # Jumlah pengeluaran
                            ft.Text(
                                value="4.502.440,00",
                                size=18,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Text(
                                value=self.total_balance,
                                size=18,
                                color="#793DFD",
                            ),
                            ft.Text(
                                value="2.000.000,00",
                                size=18,
                                weight=ft.FontWeight.W_600,
                            ),
                        ],
                    ),
                ]
            ),
        )


class FirstRow(ft.UserControl):
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
        self.refs = [ft.Ref[ft.OutlinedButton]() for _ in labels]

    def select_item(self, evt: ft.ControlEvent):
        """Event handler on item selected"""
        evt.control.disabled = True
        self.refs[self.selected_index].current.disabled = False
        self.selected_index = evt.control.data
        self.update()

    def build(self):
        buttons = [
            ft.Container(
                scale=0.75,
                margin=ft.Margin(-5, 0, -5, 0),
                content=ft.OutlinedButton(
                    ref=self.refs[i],
                    style=ft.ButtonStyle(
                        bgcolor={
                            ft.MaterialState.DEFAULT: "white",
                            ft.MaterialState.HOVERED: "blue",
                            ft.MaterialState.DISABLED: "blue",
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
        return ft.Row(
            alignment=ft.MainAxisAlignment.END,
            spacing=0,
            controls=[
                ft.Text(
                    expand=True,
                    value=self.title,
                    size=32,
                    weight=ft.FontWeight.W_600,
                ),
                *buttons,
            ],
        )


class SaldoOverviewSecondRow(ft.UserControl):
    """Second row for Saldo Overview Components"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                ft.Row(
                    expand=True,
                    spacing=2,
                    controls=[
                        ft.Image(src="images/stonks.svg"),
                        ft.Text(value="6.5%", size=12),
                    ],
                ),
                ft.Row(
                    spacing=2,
                    controls=[
                        ft.Image(src="images/green-button.svg"),
                        ft.Text(value="Income"),
                    ],
                ),
                ft.Row(
                    spacing=2,
                    controls=[
                        ft.Image(src="images/purple-button.svg"),
                        ft.Text(value="Expense"),
                    ],
                ),
            ],
        )


class SaldoChart(ft.UserControl):
    """Components for line chart at dashboard"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 1.5),
                    ft.LineChartDataPoint(5, 1.4),
                    ft.LineChartDataPoint(7, 3.4),
                    ft.LineChartDataPoint(10, 2),
                    ft.LineChartDataPoint(12, 2.2),
                    ft.LineChartDataPoint(13, 1.8),
                ],
                stroke_width=4,
                color="#00DEA3",
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 2.8),
                    ft.LineChartDataPoint(7, 1.2),
                    ft.LineChartDataPoint(10, 2.8),
                    ft.LineChartDataPoint(12, 2.6),
                    ft.LineChartDataPoint(13, 3.9),
                ],
                color=ft.colors.PINK,
                below_line_bgcolor=ft.colors.with_opacity(0, ft.colors.PINK),
                stroke_width=4,
                stroke_cap_round=True,
            ),
        ]
        return ft.LineChart(data_series=data_1)


class SaldoOverview(ft.UserControl):
    """Saldo Overview Components that consist of several rows"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Container(
            padding=ft.Padding(20, 30, 20, 10),
            border_radius=20,
            bgcolor="#FFFFFF",
            content=ft.Column(
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


class BalanceRow(ft.UserControl):
    """Row for balance that consist of two cards"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Row(
            spacing=24,
            controls=[
                SaldoOverview(expand=True),
                SaldoCard(width=260),
            ],
        )


class Targets(ft.UserControl):
    """Targets Component in Dashboard"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Container(
            bgcolor="#FFFFFF",
            padding=ft.Padding(20, 30, 20, 10),
            border_radius=20,
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(
                                value="Targets",
                                size=32,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Column(
                                expand=True,
                                scroll=ft.ScrollMode.AUTO,
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


class TransactionsDiagram(ft.UserControl):
    """Transaction Diagram component for BudgetWise"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sizes = [31.8, 18.2, 22.7, 27.3]
        self.colors = ["#F44336", "#FFEB3B", "#2196F3", "#4CAF50"]
        self.labels = ["Category 1", "Category 2", "Category 3", "Other"]

    def build(self):
        fig, axis = plt.subplots()
        plt.tight_layout(pad=-4.5)
        axis.pie(
            self.sizes,
            colors=self.colors,
            autopct="%1.1f%%",
            pctdistance=0.75,
            textprops={"fontsize": 20},
            wedgeprops={"linewidth": 7, "edgecolor": "white"},
        )
        plt.gcf().gca().add_artist(plt.Circle((0, 0), 0.5, color="white"))
        legend = ft.Column(
            spacing=5,
            controls=[
                ft.Row(
                    spacing=5,
                    controls=[
                        ft.Container(
                            width=13,
                            height=13,
                            bgcolor=color,
                        ),
                        ft.Text(
                            value=label,
                        ),
                    ],
                )
                for label, color in zip(self.labels, self.colors)
            ],
        )
        return ft.Container(
            bgcolor="#FFFFFF",
            padding=ft.Padding(20, 30, 20, 10),
            border_radius=20,
            content=ft.Column(
                controls=[
                    FirstRow(
                        title="Transaction Overview",
                        labels=["Income", "Expense"],
                    ),
                    ft.Stack(
                        expand=True,
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=MatplotlibChart(fig, expand=True),
                            ),
                            ft.Container(
                                top=0,
                                right=0,
                                alignment=ft.alignment.center,
                                content=legend,
                            ),
                        ],
                    ),
                ],
            ),
        )


class RecentTransactionTarget(ft.UserControl):
    """Row that consist of RecentTransactions and Target"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.END,
            spacing=24,
            controls=[
                TransactionsDiagram(expand=True),
                Targets(width=260),
            ],
        )


class Dashboard(ft.UserControl):
    """Dashboard Component"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Column(
            controls=[
                WelcomeMessage(),
                BalanceRow(expand=1),
                RecentTransactionTarget(expand=1),
            ]
        )
