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

from src.ui.Dashboard import Dashboard
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

    container1 = Ref[Container]()
    container2 = Ref[Container]()
    navbar = Ref[Navbar]()

    def change_page(index: int):
        container2.current.content = views[index]
        page.update()

    def resize_containers(_e):
        container1.current.height = page.window_height
        container2.current.height = page.window_height
        page.update()

    page.on_resize = resize_containers

    # Put the pages inside this list
    views = [
        Dashboard(),
        Text("Manage Transaction", size=50),
        Text("Plan Target", size=50),
        Text("Article", size=50),
        Text("Settings", size=50),
    ]

    page.add(
        Row(
            controls=[
                Container(
                    ref=container1,
                    height=page.window_height,
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
                    ref=container2,
                    height=page.window_height,
                    border_radius=border_radius.only(30, 0, 30, 0),
                    expand=True,
                    bgcolor="#E9EFFD",
                    content=views[navbar.current.selected_index],
                ),
            ]
        )
    )


if __name__ == "__main__":
    app(target=main, assets_dir="../assets")
