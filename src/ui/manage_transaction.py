"""Manage Transaction Page Module"""
import datetime
from flet_core import (
    UserControl,
    PieChart,
    Container,
    Column,
    PieChartSection,
    Padding,
    Margin,
    Text,
    ScrollMode,
    Row,
    Icon,
    alignment
)

class ManageTransaction(UserControl):
    """ Component for Manage Transactions """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Container(
            margin=Margin(40,10,0,0),
            content=Column(
                spacing=0,
                controls=[
                    Container(
                        height=200,
                        content= PieChart(
                            center_space_radius=40,
                            sections=[
                                PieChartSection(
                                    31.8,
                                    title="31.8%",
                                    color="red",
                                ),
                                PieChartSection(
                                    18.2,
                                    title="18.2%",
                                    color="yellow",
                                ),
                                PieChartSection(
                                    22.7,
                                    title="22.7%",
                                    color="blue",
                                ),
                                PieChartSection(
                                    27.3,
                                    title="27.3%",
                                    color="green",
                                ),
                            ]
                        )),
                    Container(
                        bgcolor="white",
                        height=300,
                        width=1070,
                        margin=Margin(0,10,20,0),
                        padding=Padding(20,20,20,20),
                        border_radius=20,
                        content=Column(
                            height=290,
                            controls=[
                                Text("History", size=30),
                                Column(
                                    scroll=ScrollMode.AUTO,
                                    spacing=2,
                                    height=220,
                                    controls=[
                                        History(),
                                        History(),
                                        History(),
                                        History(),
                                        History(),
                                        History()
                                    ]
                                )
                            ]

                        )
                    )
                ]
            )
        )

class History(UserControl):
    """Component to display transactions's history"""
    def __init__(self,
        icon: str="attach_money",
        title: str="payment",
        date: datetime=datetime.date.today(),
        nominal: float=0.0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.icon = icon
        self.title = title
        self.date = date
        self.nominal = nominal

    def build(self):
        return Row(
            width=1000,
            controls=[
                Icon(name=self.icon,size=30),
                Column(
                    spacing=2,
                    width=780,
                    controls=[
                        Text(value=self.title, size=15),
                        Text(value=self.date.strftime("%B %d, %Y"), size=10)
                    ]
                ),
                Container(
                    alignment=alignment.center_right,
                    content=Text(value="$" + str(self.nominal), size=15)
                )
            ]
        )
    