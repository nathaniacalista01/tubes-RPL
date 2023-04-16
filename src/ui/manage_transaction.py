"""Manage Transaction Page Module"""
import datetime
from src.ui.Dashboard import WelcomeMessage

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
    alignment,
)


class ManageTransaction(UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Column(
            spacing=0,
            controls=[
                WelcomeMessage(),
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
            ],
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
