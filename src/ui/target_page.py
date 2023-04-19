"""Target Page module"""
import datetime

import flet as ft
import src.database as db
from src.ui.target import TargetForms, Targets
from src.saldo import Saldo

from src.model import Target


class TargetPage(ft.UserControl):
    """Budgetwise Target Page"""

    def __init__(
        self, db_ref: ft.Ref[db.DatabaseManager], saldo_value: Saldo, **kwargs
    ):
        super().__init__(**kwargs)
        self.form_ref = ft.Ref[TargetForms]()
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
                tanggal_dibuat=datetime.datetime.strptime(
                    rows["tanggal_dibuat"], "%Y-%m-%d"
                ).date(),
                tanggal_tercapai=datetime.datetime.strptime(
                    rows["tanggal_tercapai"], "%Y-%m-%d"
                ).date(),
            )
            self.list_of_targets.append(temp)

    def fetch_data(self):
        """Fetch data from database"""
        self.targets = self.db_ref.current.fetch_data("Target")
        self.update()

    def add_targets_list(self):
        """ "Add new data into targets list"""
        last_data = self.targets[len(self.targets) - 1]
        new = Target(
            id_target=last_data["id_target"],
            judul=last_data["judul"],
            nominal_target=last_data["nominal_target"],
            catatan=last_data["catatan"],
            tanggal_dibuat=datetime.datetime.strptime(
                last_data["tanggal_dibuat"], "%Y-%m-%d"
            ).date(),
            tanggal_tercapai=datetime.datetime.strptime(
                last_data["tanggal_tercapai"], "%Y-%m-%d"
            ).date(),
        )
        self.list_of_targets.append(new)
        self.controls = [self.build()]
        self.update()

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
        self.fetch_data()
        self.add_targets_list()

    def delete_target(self, event: ft.ControlEvent):
        """Delete target with spesific id"""
        query = "id_target="
        deleted_item = self.list_of_targets.pop(event.control.data)
        self.db_ref.current.delete_data("Target", f"{query}{deleted_item.id_target}")
        self.controls = [self.build()]
        self.update()

    def edit_target(self, event: ft.ControlEvent):
        """Edit target with spesific id"""
        data: Target = event.control.data
        database = self.db_ref.current
        database.update_data(
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
            condition=f"id_target = {data.id_target}",
        )
        idx = list(map(lambda x: x.id_target, self.list_of_targets)).index(
            event.control.data.id_target
        )
        self.list_of_targets[idx] = event.control.data
        self.controls = [self.build()]
        self.update()

    def build(self):
        return ft.Column(
            spacing=24,
            controls=[
                TargetForms(
                    form_title="Add Target",
                    ref=self.form_ref,
                    on_submit=self.add_target,
                ),
                Targets(
                    targets=self.list_of_targets,
                    form_ref=self.form_ref,
                    on_delete=self.delete_target,
                    on_edit=self.edit_target,
                    saldo_value=self.saldo_value,
                ),
            ],
        )
