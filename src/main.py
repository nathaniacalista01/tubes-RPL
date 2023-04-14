"""This is UI module for BudgetWise App"""

from flet.flet import app
from flet_core import (
    Theme,
    border_radius,
)
from flet_core.column import Column
from flet_core.container import Container
from flet_core.margin import Margin
from flet_core.padding import Padding
from flet_core.page import Page
from flet_core.ref import Ref
from flet_core.row import Row
from flet_core.text import Text
from flet_core.types import (
    MainAxisAlignment,
)

from src.ui.navbar import Navbar, NavbarItem
from src.ui.profile_card import ProfileCard


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

    page_container = Ref[Column]()
    navbar = Ref[Navbar]()

    def change_page(index: int):
        page_container.current.controls[0] = views[index]
        page.update()

    # Put the pages inside this list
    views = [
        Text("Dashboard", size=50),
        Text("Manage Transaction", size=50),
        Text("Plan Target", size=50),
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
                    padding=Padding(35, 35, 35, 35),
                    content=Column(
                        controls=[
                            ProfileCard(),
                            Container(
                                margin=Margin(0, 70, 0, 0),
                                content=Navbar(
                                    ref=navbar,
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
                    bgcolor="#E8E8E8",
                    expand=True,
                    content=Column(
                        ref=page_container,
                        controls=[views[navbar.current.selected_index]],
                    ),
                ),
            ],
        )
    )


if __name__ == "__main__":
    app(target=main, assets_dir="../assets")
