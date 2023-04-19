"""Component for BudgetWise's dashboard"""
from typing import Optional, List, Any

import datetime as dt
import matplotlib
import matplotlib.pyplot as plt

import flet as ft
from flet.matplotlib_chart import MatplotlibChart

from src.ui.chart import LineChart
from src.ui.target import TargetBox
import src.database as db
import src.saldo as saldo
from src.model import Target

matplotlib.use("svg")


class WelcomeMessage(ft.UserControl):
    """Welcome Message Component in Dashboard"""

    def __init__(self, welcome_str: str = "Hello, Jane Doe", **kwargs):
        super().__init__(**kwargs)
        current_date = dt.datetime.now()
        self.date = current_date.strftime("%d %b %Y")
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
                    value=self.date,
                    weight=ft.FontWeight.W_600,
                    size=13,
                ),
            ],
        )


class SaldoCard(ft.UserControl):
    """Saldo Card Components in dashboard"""

    def __init__(
        self,
        saldo_value: saldo.Saldo,
        title: str = "Balances",
        total_income: str = "Total Income",
        total_expense: str = "Total Expense",
        balance_title: str = "Total Balance",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.title = title
        self.total_income = total_income
        self.total_expense = total_expense
        self.balance_title = balance_title
        self.saldo = saldo_value
        self.income_value = saldo_value.get_income()
        self.expense_value = saldo_value.get_expense()
        self.total_balance = saldo_value.get_saldo()

    def refresh_saldo(self, _: ft.ControlEvent):
        """Function to refresh saldo data"""
        self.income_value = self.saldo.get_income()
        self.expense_value = self.saldo.get_expense()
        self.total_balance = self.saldo.get_saldo()
        self.update()
        self.controls = [self.build()]
        self.update()

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
                            ft.Row(
                                controls=[
                                    ft.Text(
                                        value=self.title,
                                        size=32,
                                        weight=ft.FontWeight.W_600,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.REFRESH,
                                        on_click=self.refresh_saldo,
                                    ),
                                ]
                            ),
                            ft.Text(
                                value=self.total_income,
                                size=18,
                                color="#793DFD",
                            ),
                            # Masukin Jumlah Pemasukan
                            ft.Text(
                                value=self.income_value,
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
                                value=self.expense_value,
                                size=18,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Text(
                                value=self.balance_title,
                                size=18,
                                color="#793DFD",
                            ),
                            ft.Text(
                                value=self.total_balance,
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
        on_label_click: Any = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.title = title
        self.labels = labels
        self.selected_index = 0
        self.on_label_click = on_label_click
        self.refs = [ft.Ref[ft.OutlinedButton]() for _ in labels]

    def select_item(self, evt: ft.ControlEvent):
        """Event handler on item selected"""
        evt.control.disabled = True
        self.refs[self.selected_index].current.disabled = False
        self.selected_index = evt.control.data
        self.update()
        evt.data = self.labels[evt.control.data]
        self.on_label_click(evt)

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


class SaldoOverview(ft.UserControl):
    """Saldo Overview Components that consist of several rows"""

    def __init__(self, db_ref: ft.Ref[db.DatabaseManager], **kwargs):
        super().__init__(**kwargs)
        self.db_ref = db_ref
        self.line_chart_ref = ft.Ref[LineChart]()

    def handle_grouping(self, event: ft.ControlEvent):
        self.line_chart_ref.current.group_by = event.data
        self.line_chart_ref.current.update()

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
                        on_label_click=self.handle_grouping,
                    ),
                    SaldoOverviewSecondRow(),
                    LineChart(
                        ref=self.line_chart_ref,
                        expand=True,
                        group_by="All",
                        db_ref=self.db_ref,
                    ),
                ]
            ),
        )


class BalanceRow(ft.UserControl):
    """Row for balance that consist of two cards"""

    def __init__(self, db_ref: ft.Ref[db.DatabaseManager], saldo_value, **kwargs):
        super().__init__(**kwargs)
        self.saldo_value = saldo_value
        self.db_ref = db_ref

    def build(self):
        return ft.Row(
            spacing=24,
            controls=[
                SaldoOverview(expand=True, db_ref=self.db_ref),
                SaldoCard(width=260, saldo_value=self.saldo_value),
            ],
        )


class Targets(ft.UserControl):
    """Targets Component in Dashboard"""

    def __init__(self, db_ref: ft.Ref[db.DatabaseManager], saldo_value, **kwargs):
        super().__init__(**kwargs)
        self.db_ref = db_ref
        self.saldo_value = saldo_value
        self.targets = db_ref.current.fetch_data("Target")
        self.list_of_targets = []
        for rows in self.targets:
            temp = Target(
                id_target=rows["id_target"],
                judul=rows["judul"],
                nominal_target=rows["nominal_target"],
                catatan=rows["catatan"],
                tanggal_dibuat=rows["tanggal_dibuat"],
                tanggal_tercapai=rows["tanggal_tercapai"],
            )
            self.list_of_targets.append(temp)

    def refresh_target(self, _: ft.ControlEvent):
        """Function to refresh target"""
        self.targets = self.db_ref.current.fetch_data("Target")
        self.list_of_targets = []
        for rows in self.targets:
            temp = Target(
                id_target=rows["id_target"],
                judul=rows["judul"],
                nominal_target=rows["nominal_target"],
                catatan=rows["catatan"],
                tanggal_dibuat=rows["tanggal_dibuat"],
                tanggal_tercapai=rows["tanggal_tercapai"],
            )
            self.list_of_targets.append(temp)
        self.controls = [self.build()]
        self.update()

    def build(self):
        return ft.Container(
            bgcolor="#FFFFFF",
            padding=ft.Padding(20, 30, 20, 10),
            border_radius=20,
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text(
                                        value="Targets",
                                        size=32,
                                        weight=ft.FontWeight.W_600,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.REFRESH,
                                        on_click=self.refresh_target,
                                    ),
                                ]
                            ),
                            ft.Column(
                                expand=True,
                                scroll=ft.ScrollMode.AUTO,
                                spacing=5,
                                controls=[
                                    TargetBox(
                                        target_title=t.judul,
                                        target_description=t.catatan,
                                        start_date=t.tanggal_dibuat,
                                        end_date=t.tanggal_tercapai,
                                        percentage=min(
                                            1,
                                            self.saldo_value.get_saldo()
                                            / t.nominal_target,
                                        ),
                                    )
                                    for (i, t) in enumerate(self.list_of_targets)
                                ],
                            ),
                        ]
                    )
                ]
            ),
        )


class TransactionFirstRow(ft.UserControl):
    """First row of transactions"""

    def __init__(
        self,
        title: str,
        selected_index,
        handle_click,
        labels: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.title = title
        self.labels = labels
        self.selected_index = selected_index
        self.refs = [ft.Ref[ft.OutlinedButton]() for _ in labels]
        self.handle_click = handle_click

    def select_item(self, evt: ft.ControlEvent):
        """Event handler on item selected"""
        evt.control.disabled = True
        self.refs[self.selected_index].current.disabled = False
        self.selected_index = evt.control.data
        self.update()
        self.handle_click(evt)

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


class TransactionsDiagram(ft.UserControl):
    """Transaction Diagram component for BudgetWise"""

    def __init__(self, db_ref: ft.Ref[db.DatabaseManager], **kwargs):
        super().__init__(**kwargs)
        self.sizes = []
        self.colors = ["#F44336", "#FFEB3B", "#2196F3", "#4CAF50"]
        self.labels = []
        self.db_ref = db_ref
        self.categories = db_ref.current.group_income_by_category()
        self.selected_index = (0,)
        for rows in self.categories:
            self.sizes.append(rows["persen"])
            self.labels.append(rows["kategori"])
        self.last_choice = 0

    def handle_click(self, event: ft.ControlEvent):
        """Handle click or change between expense and income"""
        if event.control.text == "Expense":
            self.categories = self.db_ref.current.group_expense_by_category()
            self.sizes = []
            self.labels = []
            self.last_choice = 1
            for rows in self.categories:
                self.sizes.append(rows["persen"])
                self.labels.append(rows["kategori"])
        else:
            self.categories = self.db_ref.current.group_income_by_category()
            self.sizes = []
            self.labels = []
            self.last_choice = 0
            for rows in self.categories:
                self.sizes.append(rows["persen"])
                self.labels.append(rows["kategori"])
        self.controls = [self.build()]
        self.update()

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
                    TransactionFirstRow(
                        title="Transaction Overview",
                        labels=["Income", "Expense"],
                        selected_index=self.last_choice,
                        handle_click=self.handle_click,
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

    def __init__(self, db_ref: ft.Ref[db.DatabaseManager], saldo_value, **kwargs):
        super().__init__(**kwargs)
        self.db_ref = db_ref
        self.saldo_value = saldo_value

    def build(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.END,
            spacing=24,
            controls=[
                TransactionsDiagram(expand=True, db_ref=self.db_ref),
                Targets(width=260, db_ref=self.db_ref, saldo_value=self.saldo_value),
            ],
        )


class Dashboard(ft.UserControl):
    """Dashboard Component"""

    def __init__(
        self, db_ref: ft.Ref[db.DatabaseManager], saldo_value: saldo.Saldo, **kwargs
    ):
        super().__init__(**kwargs)
        self.saldo_value = saldo_value
        self.db_ref = db_ref

    def build(self):
        return ft.Column(
            controls=[
                WelcomeMessage(),
                BalanceRow(expand=1, saldo_value=self.saldo_value, db_ref=self.db_ref),
                RecentTransactionTarget(
                    expand=1, db_ref=self.db_ref, saldo_value=self.saldo_value
                ),
            ]
        )
