"""This is UI module for BudgetWise App"""

import flet as ft

import src.database as db
from src import load_profile
from src.ui.dashboard import Dashboard
from src.ui.manage_transaction import ManageTransaction
from src.ui.navbar import Navbar, NavbarItem
from src.ui.profile_card import ProfileCard
from src.ui.target_page import TargetPage
from src.ui.settings import SettingsPage
from src.saldo import Saldo
from src.ui.artikel_page import ArticlePage


def main(page: ft.Page):
    """Main entry point for Flet App"""
    page.fonts = {
        "Nunito": "fonts/Nunito-Regular.ttf",
        "Istok Web": "fonts/IstokWeb-Regular.ttf",
    }

    page.title = "BudgetWise Financial Management App"
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme = ft.Theme(font_family="Nunito")
    page.bgcolor = "#2A3575"

    page_container = ft.Ref[ft.Stack]()
    database = ft.Ref[db.DatabaseManager]()
    database.current = db.DatabaseManager()
    profile_card = ft.Ref[ProfileCard]()

    def change_page(index: int):
        for view in page_container.current.controls:
            view.visible = False
        page_container.current.controls[index].visible = True
        page.update()

    saldo = Saldo(db_ref=database)
    # Put the pages inside this list
    views = [
        Dashboard(expand=True, db_ref=database, saldo_value=saldo),
        ManageTransaction(db_ref=database, expand=True),
        TargetPage(db_ref=database, expand=True, saldo_value=saldo),
        ArticlePage(expand=True),
        SettingsPage(expand=True, profile_card_ref=profile_card),
    ]

    profile = load_profile()

    page.add(
        ft.Row(
            expand=True,
            spacing=0,
            controls=[
                ft.Container(
                    bgcolor="#2A3575",
                    padding=35,
                    content=ft.Column(
                        controls=[
                            ProfileCard(
                                ref=profile_card,
                                profile_name=profile["profile_name"],
                                profile_job=profile["profile_job"],
                                profile_email=profile["profile_email"],
                                profile_img_url=profile["profile_img_url"],
                            ),
                            ft.Container(
                                margin=ft.margin.only(top=70),
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
                ft.Container(
                    border_radius=ft.border_radius.only(30, 0, 30, 0),
                    bgcolor="#E9EFFD",
                    expand=True,
                    padding=35,
                    content=ft.Stack(
                        ref=page_container,
                        controls=[
                            ft.Column(controls=[view], visible=i == 0)
                            for i, view in enumerate(views)
                        ],
                    ),
                ),
            ],
        )
    )


if __name__ == "__main__":
    ft.app(target=main, assets_dir="../assets")
