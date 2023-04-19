"""Component for a article"""
import flet as ft
from src.ui.artikel_konten import artikel


class Article(ft.UserControl):
    """Article Component"""

    def __init__(self, article_title: str, article_body: str, **kwargs):
        super().__init__(**kwargs)
        self.article_title = article_title
        self.article_body = article_body

    def build(self):
        return ft.Container(
            width=800,
            height=400,
            bgcolor="#FFFFFF",
            padding=ft.Padding(15, 15, 15, 15),
            margin=ft.Margin(20, 5, 20, 5),
            border_radius=15,
            content=ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.Container(
                        content=ft.Text(
                            value=self.article_title,
                            text_align=ft.TextAlign.LEFT,
                            size=32,
                            weight=ft.FontWeight.W_800,
                            color="black",
                        )
                    ),
                    ft.Container(
                        content=ft.Text(
                            value=self.article_body,
                            text_align=ft.TextAlign.JUSTIFY,
                            size=16,
                            color="black",
                        )
                    ),
                ],
            ),
        )
