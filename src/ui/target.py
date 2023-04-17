"""Target component module"""

import datetime

import flet as ft


class Target(ft.UserControl):
    """Budgetwise Target Component"""

    def __init__(
        self,
        target_title: str = "Target Title",
        target_description: str = "Target Description",
        percentage: float = 0.3,
        start_date: datetime = datetime.date.today(),
        end_date: datetime = datetime.date(
            datetime.datetime.now().year + 1,
            datetime.datetime.now().month,
            datetime.datetime.now().day,
        ),
        icon: str = "fact_check",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.target_title = target_title
        self.target_description = target_description
        self.percentage = percentage
        self.start_date = start_date
        self.end_date = end_date
        self.icon = icon

    def build(self):
        return ft.Column(
            width=230,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    bgcolor="#F1ECFF",
                    padding=ft.Padding(15, 15, 15, 15),
                    margin=ft.Margin(20, 0, 20, 0),
                    border_radius=20,
                    border=ft.border.all(color="black"),
                    content=ft.Column(
                        spacing=0,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        ft.Icon(name=self.icon, size=50),
                                    ),
                                    ft.Column(
                                        spacing=3,
                                        width=100,
                                        height=70,
                                        controls=[
                                            ft.Container(
                                                content=ft.Text(
                                                    value=self.target_title,
                                                    text_align=ft.TextAlign.LEFT,
                                                    size=11,
                                                    color="black",
                                                ),
                                            ),
                                            ft.Divider(height=0, color="black"),
                                            ft.Container(
                                                padding=ft.Padding(0, 0, 0, 10),
                                                content=ft.Text(
                                                    value=self.target_description,
                                                    text_align=ft.TextAlign.LEFT,
                                                    size=7,
                                                    color="black",
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            ft.ProgressBar(
                                width=190,
                                bar_height=10,
                                color="#1FC3E8",
                                bgcolor="#385682",
                                value=self.percentage,
                            ),
                            ft.Container(
                                alignment=ft.alignment.center_right,
                                content=ft.Text(
                                    value=str(self.percentage * 100) + "% completed",
                                    color="#6182B2",
                                    size=8,
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                padding=ft.Padding(0, 0, 0, 10),
                            ),
                            ft.Row(
                                controls=[
                                    ft.Column(
                                        spacing=2,
                                        controls=[
                                            ft.Text(
                                                value="Start Date :",
                                                color="#2B9F18",
                                                size=9,
                                            ),
                                            ft.Text(
                                                value="End Date   :",
                                                color="#EF6161",
                                                size=9,
                                            ),
                                        ],
                                    ),
                                    ft.Column(
                                        spacing=2,
                                        controls=[
                                            ft.Text(
                                                value=self.start_date.strftime(
                                                    "%d %B %Y"
                                                ),
                                                size=9,
                                            ),
                                            ft.Text(
                                                value=self.end_date.strftime(
                                                    "%d %B %Y"
                                                ),
                                                size=9,
                                            ),
                                        ],
                                    ),
                                ]
                            ),
                        ],
                    ),
                ),
            ],
        )


class TargetEdit(Target):
    """Budgetwise Target Component"""

    def __init__(
        self,
        target_title: str = "Target Title",
        target_description: str = "Target Description",
        percentage: float = 0.3,
        start_date: datetime = datetime.date.today(),
        end_date: datetime = datetime.date(
            datetime.datetime.now().year + 1,
            datetime.datetime.now().month,
            datetime.datetime.now().day,
        ),
        icon: str = "fact_check",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.target_title = target_title
        self.target_description = target_description
        self.percentage = percentage
        self.start_date = start_date
        self.end_date = end_date
        self.icon = icon

    def build(self):
        return ft.Column(
            controls=[
                super().build(),
                ft.Container(
                    height=20,
                    width=230,
                    padding=ft.Padding(20, 0, 20, 0),
                    content=ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="Edit", color="black", bgcolor="#D9D9D9", width=90
                            ),
                            ft.ElevatedButton(
                                text="Delete",
                                color="black",
                                bgcolor="#D9D9D9",
                                width=90,
                            ),
                        ]
                    ),
                ),
            ]
        )


class TargetForm(ft.UserControl):
    """Target form component"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Column(
            width=1070,
            controls=[
                ft.Container(
                    bgcolor="white",
                    height=250,
                    padding=ft.Padding(10, 10, 10, 0),
                    margin=ft.Margin(0, 0, 20, 0),
                    border_radius=20,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                height=25,
                                content=ft.TextField(label="Title", text_size=12),
                            ),
                            ft.Container(
                                height=25,
                                content=ft.TextField(label="Nominal", text_size=12),
                            ),
                            ft.Container(
                                height=25,
                                content=ft.TextField(label="Target Date", text_size=12),
                            ),
                            ft.Container(
                                height=70,
                                content=ft.TextField(
                                    label="Descriptions",
                                    border=ft.InputBorder.UNDERLINE,
                                    text_size=12,
                                    multiline=True,
                                ),
                            ),
                            ft.Container(
                                alignment=ft.alignment.center_right,
                                content=ft.ElevatedButton(
                                    text="Add Target", bgcolor="#00FF47"
                                ),
                            ),
                        ]
                    ),
                ),
            ],
        )
