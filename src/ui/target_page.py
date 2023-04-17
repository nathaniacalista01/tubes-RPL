"""Target Page module"""

import flet as ft
import datetime

from src.ui.target import TargetForms, Targets
from src.ui.dashboard import WelcomeMessage

from model import Target
targets = [
    Target(
        id_target = 1,
        judul= "title1",
        nominal_target= 5000,
        catatan="desc1",
        tanggal_dibuat=datetime.date.today(),
        tanggal_tercapai=datetime.date.today(),
    ),
    Target(
        id_target = 2,
        judul= "title2",
        nominal_target= 50000,
        catatan="desc2",
        tanggal_dibuat=datetime.date.today(),
        tanggal_tercapai=datetime.date.today(),
    )
]

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
                    # WelcomeMessage(),
                    TargetForms(),
                    Targets(targets=targets)
                ],
            ),
        )
