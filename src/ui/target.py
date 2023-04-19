"""Target component module"""
import datetime
from typing import Optional, Any, List

import flet as ft
from src.model import Target
from src import model
from src.saldo import Saldo


class TargetForms(ft.UserControl):
    """Component for target's forms"""

    def __init__(
        self,
        form_title: str,
        default_values: Optional[Target] = None,
        ref: Optional[ft.Ref["TargetForms"]] = None,
        on_submit: Any = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = ft.Ref[ft.TextField]()
        self.nominal = ft.Ref[ft.TextField]()
        self.target_date = ft.Ref[ft.TextField]()
        self.description = ft.Ref[ft.TextField]()
        self.ref = ref
        self.ref.current = self
        self.on_submit = on_submit
        self.default_values = default_values
        self.form_title = form_title

    @staticmethod
    def new_forms(
        name: str,
        keyboard_type: ft.KeyboardType.TEXT,
        ref: Optional[ft.Ref[ft.TextField]] = None,
        value: Optional[str] = None,
        on_change: Any = None,
    ):
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
                        ref=ref,
                        on_change=on_change,
                        border_color="transparent",
                        height=55,
                        text_size=13,
                        label=name,
                        label_style=ft.TextStyle(size=13),
                        content_padding=ft.padding.only(top=30, left=5),
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                        keyboard_type=keyboard_type,
                        error_text=ref.current.error_text
                        if ref.current is not None
                        else None,
                        value=value,
                    )
                ],
            ),
        )

    @staticmethod
    def desc_forms(
        name: str,
        ref=Optional[ft.Ref[ft.TextField]],
        value: Optional[str] = None,
    ):
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
                        ref=ref,
                        text_size=13,
                        label=name,
                        label_style=ft.TextStyle(size=13),
                        content_padding=ft.padding.only(top=30),
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                        multiline=True,
                        value=value,
                    )
                ],
            ),
        )

    def submit(self, event: ft.ControlEvent):
        """Handle submit event from targets"""
        try:
            valid_date = bool(
                datetime.datetime.strptime(self.target_date.current.value, "%d-%m-%Y")
            )
        except ValueError:
            valid_date = False

        if (
            valid_date
            and self.title.current.value
            and self.nominal.current.value.isdigit()
        ):
            event.control.data = model.Target(
                id_target=-1
                if self.default_values is None
                else self.default_values.id_target,
                judul=self.title.current.value,
                nominal_target=int(self.nominal.current.value),
                catatan=self.description.current.value,
                tanggal_dibuat=datetime.date.today(),
                tanggal_tercapai=datetime.datetime.strptime(
                    self.target_date.current.value, "%d-%m-%Y"
                ).date(),
            )
            self.title.current.value = ""
            self.nominal.current.value = ""
            self.description.current.value = ""
            self.target_date.current.value = ""
            self.target_date.current.error_text = None
            self.update()
            self.on_submit(event)
        else:
            self.target_date.current.error_text = (
                "Invalid date format" if not valid_date else None
            )
            self.nominal.current.error_text = (
                "Nominal must be an integer"
                if not self.nominal.current.value.isdigit()
                else None
            )
            self.title.current.error_text = (
                "Title cannot be empty" if not self.title.current.value else None
            )
            self.controls = [self.build()]
            self.update()

    def build(self):
        return ft.Container(
            expand=True,
            bgcolor="#FFFFFF",
            border=ft.border.all(1, "#ebebeb"),
            border_radius=20,
            padding=15,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Text(
                        value=self.form_title,
                        size=32,
                        weight=ft.FontWeight.W_600,
                    ),
                    ft.Row(
                        controls=[
                            self.new_forms(
                                "Title",
                                ft.KeyboardType.TEXT,
                                ref=self.title,
                                value=None
                                if self.default_values is None
                                else self.default_values.judul,
                            ),
                            self.new_forms(
                                "Nominal",
                                ft.KeyboardType.NUMBER,
                                ref=self.nominal,
                                value=None
                                if self.default_values is None
                                else str(self.default_values.nominal_target),
                            ),
                            self.new_forms(
                                "Target Date (DD-MM-YYYY)",
                                ft.KeyboardType.DATETIME,
                                ref=self.target_date,
                                value=None
                                if self.default_values is None
                                else self.default_values.tanggal_tercapai.strftime(
                                    "%d-%m-%Y"
                                ),
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.desc_forms(
                                name="Descriptions",
                                ref=self.description,
                                value=None
                                if self.default_values is None
                                else self.default_values.catatan,
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.ElevatedButton(
                                width=100,
                                bgcolor="#6761B9",
                                color="white",
                                text="Submit",
                                on_click=self.submit,
                            ),
                        ],
                    ),
                ],
            ),
        )


class TargetBox(ft.UserControl):
    """Budgetwise Target Component"""

    def __init__(
        self,
        percentage: float,
        target_title: str = "Target Title",
        target_description: str = "Target Description",
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
                                    value=str(round(self.percentage * 100, 2))
                                    + "% completed",
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
                                                value=self.start_date,
                                                size=9,
                                            ),
                                            ft.Text(
                                                value=self.end_date,
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


class Targets(ft.UserControl):
    """List of Target component"""

    def __init__(
        self,
        saldo_value: Saldo,
        form_ref: ft.Ref[TargetForms],
        targets: Optional[List[Target]] = None,
        on_delete: Any = None,
        on_edit: Any = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.targets = [] if targets is None else targets
        self.on_delete = on_delete
        self.on_edit = on_edit
        self.saldo_value = saldo_value
        self.form_ref = form_ref

    def create_edit_form(self, event: ft.ControlEvent):
        """Create edit form"""
        self.form_ref.current.default_values = self.targets[event.control.data]
        self.form_ref.current.form_title = "Edit Transaction"
        self.form_ref.current.on_submit = self.on_edit
        self.form_ref.current.controls = [self.form_ref.current.build()]
        self.form_ref.current.update()

    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                    bgcolor="white",
                    height=280,
                    padding=ft.padding.all(10),
                    border_radius=20,
                    content=ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        content=ft.Text(
                                            value="Targets",
                                            size=32,
                                            weight=ft.FontWeight.W_600,
                                        ),
                                        padding=ft.padding.only(
                                            left=10, top=5, right=10
                                        ),
                                    ),
                                    ft.Container(
                                        padding=ft.padding.only(bottom=10),
                                        content=ft.Row(
                                            scroll=ft.ScrollMode.HIDDEN,
                                            controls=[
                                                ft.Column(
                                                    height=250,
                                                    controls=[
                                                        TargetBox(
                                                            target_title=t.judul,
                                                            target_description=t.catatan,
                                                            start_date=t.tanggal_dibuat,
                                                            end_date=t.tanggal_tercapai,
                                                            percentage=min(
                                                                1,
                                                                self.saldo_value.get_saldo()
                                                                / t.nominal_target,
                                                            ),
                                                        ),
                                                        ft.Container(
                                                            height=20,
                                                            width=230,
                                                            padding=ft.Padding(
                                                                20, 0, 20, 0
                                                            ),
                                                            content=ft.Row(
                                                                controls=[
                                                                    ft.ElevatedButton(
                                                                        text="Edit",
                                                                        color="black",
                                                                        bgcolor="#D9D9D9",
                                                                        width=90,
                                                                        on_click=self.create_edit_form,
                                                                        data=i,
                                                                    ),
                                                                    ft.ElevatedButton(
                                                                        text="Delete",
                                                                        color="black",
                                                                        bgcolor="#D9D9D9",
                                                                        width=90,
                                                                        on_click=self.on_delete,
                                                                        data=i,
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                    ],
                                                )
                                                for i, t in enumerate(self.targets)
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                )
            ]
        )
