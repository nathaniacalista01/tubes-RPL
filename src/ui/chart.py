"""Chart components for BudgetWise"""
from datetime import datetime
from datetime import timedelta
from typing import Literal
from itertools import groupby

from flet.matplotlib_chart import MatplotlibChart
from flet import Ref
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from src.database import DatabaseManager

matplotlib.use("svg")


class LineChart(MatplotlibChart):
    def __init__(
        self,
        db_ref: Ref[DatabaseManager],
        group_by: Literal["All", "1M", "3M", "6M", "1Y"],
        **kwargs
    ):
        kwargs = dict(filter(lambda tup: tup[0] != "figure", kwargs.items()))
        self.group_by = group_by
        self.db_ref = db_ref
        self.fetch_data(self.group_by)
        super().__init__(figure=self.figure, **kwargs)

    def update(self):
        plt.close("all")
        self.fetch_data(self.group_by)
        super().update()

    def fetch_data(self, group_by: Literal["All", "1M", "3M", "6M", "1Y"]):
        incomes = self.db_ref.current.fetch_data("Pemasukan")
        expenses = self.db_ref.current.fetch_data("Pengeluaran")
        self.figure, axis = plt.subplots(figsize=(20, 5))
        axis.tick_params(axis="both", which="major", labelsize=16)
        axis.tick_params(axis="both", which="minor", labelsize=16)
        incomes = [
            (
                datetime.strptime(item["tanggal"], "%Y-%m-%d").date(),
                item["nominal"],
            )
            for item in incomes
        ]
        expenses = [
            (
                datetime.strptime(item["tanggal"], "%Y-%m-%d").date(),
                item["nominal"],
            )
            for item in expenses
        ]

        x_incomes = []
        y_incomes = []
        x_expenses = []
        y_expenses = []

        if group_by == "All":
            for key, group in groupby(incomes, lambda x: x[0]):
                x_incomes.append(key)
                y_incomes.append(sum([item[1] for item in group]))
            for key, group in groupby(expenses, lambda x: x[0]):
                x_expenses.append(key)
                y_expenses.append(sum([item[1] for item in group]))
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
            plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
        elif group_by == "1M":
            [x_incomes, y_incomes], [x_expenses, y_expenses] = self.group_by_daterange(
                incomes, expenses, days=30
            )
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
            plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
        elif group_by == "3M":
            [x_incomes, y_incomes], [x_expenses, y_expenses] = self.group_by_daterange(
                incomes, expenses, days=30 * 3
            )
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
            plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30 * 3))
        elif group_by == "6M":
            [x_incomes, y_incomes], [x_expenses, y_expenses] = self.group_by_daterange(
                incomes, expenses, days=30 * 6
            )
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
            plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30 * 6))
        elif group_by == "1Y":
            [x_incomes, y_incomes], [x_expenses, y_expenses] = self.group_by_daterange(
                incomes, expenses, days=365
            )
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
            plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=365))

        plt.gca().xaxis.set_tick_params(rotation=30)
        axis.plot(
            x_incomes,
            y_incomes,
            marker="o",
            linewidth=2,
            color="#00DEA3",
            markersize=10,
        )
        axis.plot(
            x_expenses,
            y_expenses,
            marker="o",
            linewidth=2,
            color="#793DFD",
            markersize=10,
        )
        plt.tight_layout()

    @staticmethod
    def group_by_daterange(incomes, expenses, days: int):
        grouped_incomes = []
        x_incomes = []
        x_expenses = []
        start_date = min(incomes, default=(datetime.today(), 0), key=lambda k: k[0])[0]
        end_date = min(incomes, default=(start_date, 0), key=lambda k: k[0])[0]
        delta = timedelta(days=days)
        while start_date <= end_date:
            group = list(
                filter(lambda x: start_date <= x[0] < start_date + delta, incomes)
            )
            if len(group) != 0:
                grouped_incomes.append(group)
                x_incomes.append(start_date)
            start_date += delta
        grouped_expenses = []
        start_date = min(expenses, default=(datetime.today(), 0), key=lambda k: k[0])[0]
        end_date = min(expenses, default=(start_date, 0), key=lambda k: k[0])[0]
        while start_date <= end_date:
            group = list(
                filter(lambda x: start_date <= x[0] < start_date + delta, expenses)
            )
            if len(group) != 0:
                grouped_expenses.append(group)
                x_expenses.append(start_date)
            start_date += delta
        y_incomes = list(
            map(lambda seq: sum(list(map(lambda item: item[1], seq))), grouped_incomes)
        )
        y_expenses = list(
            map(lambda seq: sum(list(map(lambda item: item[1], seq))), grouped_expenses)
        )
        return [x_incomes, y_incomes], [x_expenses, y_expenses]
