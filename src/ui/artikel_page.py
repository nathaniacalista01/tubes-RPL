"""Article page in BudgetWise"""
import flet as ft
from src.ui.artikel import Article
from src.ui.dashboard import WelcomeMessage
from src.ui.artikel_konten import artikel


class ArticlePage(ft.UserControl):
    """Component for article page"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for a in artikel:
            print(a["judul"])

    def build(self):
        return ft.Container(
            margin=ft.margin.only(left=40, top=10),
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    Article(
                        article_title=a["judul"], article_body=a["konten"]
                    )  # artikel 1
                    for a in artikel
                ],
            ),
        )
