"""Target Page module"""
import datetime
import flet as ft
import src.database as db
from src.ui.target import TargetForms, Targets

from src.model import Target

targets = [
    Target(
        judul="title1",
        nominal_target=5000,
        catatan="desc1",
        tanggal_dibuat=datetime.date.today(),
        tanggal_tercapai=datetime.date.today(),
    ),
    Target(
        judul="title2",
        nominal_target=50000,
        catatan="desc2",
        tanggal_dibuat=datetime.date.today(),
        tanggal_tercapai=datetime.date.today(),
    ),
]


class TargetPage(ft.UserControl):
    """Budgetwise Target Page"""

    def __init__(
        self,
        db_ref : ft.Ref[db.DatabaseManager],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.form_ref = ft.Ref[TargetForms]()
        self.db_ref = db_ref

    def add_target(self, event : ft.ControlEvent):
        """Methods to add target into database"""
        data : Target = event.control.data
        database = self.db_ref.current
        database.insert_data(
            table_name="Target",
            columns=["judul","nominal_target","catatan","tanggal_dibuat","tanggal_tercapai"],
            values=[
                data.judul,data.nominal_target,data.catatan,data.tanggal_dibuat,
                data.tanggal_tercapai
            ],
        )

    def build(self):
        return ft.Container(
            margin=ft.margin.only(left=40, top=10),
            content=ft.Column(
                controls=[
                    TargetForms(ref = self.form_ref,on_submit=self.add_target),
                    Targets(targets=targets),
                ],
            ),
        )
