"""This is UI module for BudgetWise App"""

from flet import margin
from flet.flet import app
from flet_core import (
    Theme,
    border_radius,
)
from flet_core.stack import Stack
from flet_core.column import Column
from flet_core.container import Container
from flet_core.page import Page
from flet_core.ref import Ref
from flet_core.row import Row
from flet_core.text import Text
from flet_core.types import (
    MainAxisAlignment,
)

from src.ui.dashboard import Dashboard
from src.ui.manage_transaction import ManageTransaction
from src.ui.navbar import Navbar, NavbarItem
from src.ui.profile_card import ProfileCard
from src.ui.target_page import TargetPage


def main(page: Page):
    """Main entry point for Flet App"""
    page.fonts = {
        "Nunito": "fonts/Nunito-Regular.ttf",
        "Istok Web": "fonts/IstokWeb-Regular.ttf",
    }

    page.title = "Flet counter example"
    page.padding = 0
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme = Theme(font_family="Nunito")
    page.bgcolor = "#2A3575"

    page_container = Ref[Stack]()

    def change_page(index: int):
        for view in page_container.current.controls:
            view.visible = False
        page_container.current.controls[index].visible = True
        page.update()

    # Put the pages inside this list
    views = [
        Dashboard(expand=True),
        ManageTransaction(expand=True),
        TargetPage(expand=True),
        Text("Article", size=50),
        Text("Settings", size=50),
    ]

    page.add(
        Row(
            expand=True,
            spacing=0,
            controls=[
                Container(
                    bgcolor="#2A3575",
                    padding=35,
                    content=Column(
                        controls=[
                            ProfileCard(),
                            Container(
                                margin=margin.only(top=70),
                                content=Navbar(
                                    on_item_selected=change_page,
                                    items=[
                                        NavbarItem(
                                            img_src="images/dashboard.svg",
                                            text="Dashboard",
                                        ),
                                        NavbarItem(
                                            img_src="images/edit-transaction.svg",
                                            text="Manage Transaction",
                                        ),
                                        NavbarItem(
                                            img_src="images/plan-target.svg",
                                            text="Plan Target",
                                        ),
                                        NavbarItem(
                                            img_src="images/article.svg",
                                            text="Article",
                                        ),
                                        NavbarItem(
                                            img_src="images/settings.svg",
                                            text="Settings",
                                        ),
                                    ],
                                ),
                            ),
                        ]
                    ),
                ),
                Container(
                    border_radius=border_radius.only(30, 0, 30, 0),
                    bgcolor="#E9EFFD",
                    expand=True,
                    padding=35,
                    content=Stack(
                        ref=page_container,
                        controls=[
                            Column(controls=[view], visible=(i == 0))
                            for i, view in enumerate(views)
                        ],
                    ),
                ),
            ],
        )
    )


if __name__ == "__main__":
    app(target=main, assets_dir="../assets")
