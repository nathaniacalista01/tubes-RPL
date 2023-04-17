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


class TargetForms(ft.UserControl):
    """Component for target's forms"""

    def __init__(
        self,
        title: str = "Title",
        nominal: float = 0.0,
        target_date: datetime = datetime.date.today(),
        description: str = "Description",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = title
        self.nominal = nominal
        self.target_date = target_date
        self.description = description

    @staticmethod
    def new_forms(name: str, keyboard_type: ft.KeyboardType):
        """Components for new form's input"""
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
                        border_color="transparent",
                        height=30,
                        text_size=13,
                        label=name,
                        label_style=ft.TextStyle(size=13),
                        content_padding=ft.padding.only(top=30),
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                        keyboard_type=keyboard_type,
                    )
                ],
            ),
        )

    @staticmethod
    def desc_forms(name: str):
        """Component for forms' descriptions"""
        return ft.Container(
            expand=True,
            height=65,
            bgcolor="#ebebeb",
            border_radius=ft.border_radius.all(6),
            margin=ft.margin.only(top=10),
            padding=ft.padding.all(8),
            content=ft.Column(
                spacing=1,
                controls=[
                    ft.TextField(
                        border_color="transparent",
                        height=65,
                        text_size=13,
                        label=name,
                        label_style=ft.TextStyle(size=13),
                        content_padding=ft.padding.only(top=30),
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                        multiline=True,
                    )
                ],
            ),
        )

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
                        value="Add Target",
                        size=32,
                        weight=ft.FontWeight.W_600,
                    ),
                    ft.Row(
                        controls=[
                            self.new_forms("Title", ft.KeyboardType.TEXT),
                            self.new_forms("Nominal", ft.KeyboardType.NUMBER),
                            self.new_forms("Target Date", ft.KeyboardType.DATETIME),
                        ]
                    ),
                    ft.Row(controls=[self.desc_forms(self.description)]),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.ElevatedButton(
                                width=100,
                                bgcolor="#6761B9",
                                color="white",
                                text="Add",
                            ),
                        ],
                    ),
                ],
            ),
        )
