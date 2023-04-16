"""Target Page module"""

import flet as ft
import datetime

from src.ui.target import TargetEdit, TargetForm
from src.ui.dashboard import WelcomeMessage


class TargetPage(ft.UserControl):
    """Budgetwise Target Page"""

    def __init__(self, date: datetime = datetime.date.today(), **kwargs):
        super().__init__(**kwargs)
        self.date = date

    def build(self):
        return ft.Container(
            margin=ft.margin.only(left=40, top=10),
            content=ft.Column(
                width=1070,
                controls=[
                    WelcomeMessage(),
                    TargetForm(),
                    ft.Container(
                        bgcolor="white",
                        height=270,
                        width=1070,
                        padding=ft.padding.all(10),
                        margin=ft.margin.only(top=10, right=20),
                        border_radius=20,
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Text(value="Targets", size=20),
                                    padding=ft.padding.only(left=10, top=5, right=10),
                                ),
                                ft.Container(
                                    padding=ft.padding.only(bottom=10),
                                    content=ft.Row(
                                        scroll=ft.ScrollMode.HIDDEN,
                                        width=890,
                                        controls=[
                                            TargetEdit(),
                                            TargetEdit(
                                                target_title="Beli iphone 20",
                                                target_description="iPhone adalah kebutuhan yang aku perlukan untuk "
                                                                   "hidup :)",
                                                percentage=0.7,
                                                icon="phone_iphone",
                                            ),
                                            TargetEdit(),
                                            TargetEdit(),
                                            TargetEdit(),
                                            TargetEdit(),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )
