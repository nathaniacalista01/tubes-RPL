"""Target Page module"""
import datetime
import flet as ft
import src.database as db
from src.ui.target import TargetForms, Targets

from src.model import Target
class TargetPage(ft.UserControl):
    """Budgetwise Target Page"""

    def __init__(self, db_ref: ft.Ref[db.DatabaseManager], **kwargs):
        super().__init__(**kwargs)
        self.form_ref = ft.Ref[TargetForms]()
        self.db_ref = db_ref
        self.targets = db_ref.current.fetch_data("Target")
        self.list_of_targets = []
        for rows in self.targets:
            temp = Target(
                judul=rows["judul"],
                nominal_target=rows["nominal_target"],
                catatan=rows["catatan"],
                tanggal_dibuat=rows["tanggal_dibuat"],
                tanggal_tercapai=rows["tanggal_tercapai"],
            )
            self.list_of_targets.append(temp)

    def add_target(self, event: ft.ControlEvent):
        """Methods to add target into database"""
        data: Target = event.control.data
        database = self.db_ref.current
        database.insert_data(
            table_name="Target",
            columns=[
                "judul",
                "nominal_target",
                "catatan",
                "tanggal_dibuat",
                "tanggal_tercapai",
            ],
            values=[
                data.judul,
                data.nominal_target,
                data.catatan,
                data.tanggal_dibuat,
                data.tanggal_tercapai,
            ],
        )
        new = Target(
            judul=data.judul,
            nominal_target=data.nominal_target,
            catatan=data.catatan,
            tanggal_dibuat=data.tanggal_dibuat,
            tanggal_tercapai=data.tanggal_tercapai,
        )
        self.list_of_targets.append(new)
        self.controls = [self.build()]
        self.update()

    def build(self):
        return ft.Container(
            margin=ft.margin.only(left=40, top=10),
            content=ft.Column(
                controls=[
                    TargetForms(ref=self.form_ref, on_submit=self.add_target),
                    Targets(targets=self.list_of_targets),
                ],
            ),
        )
