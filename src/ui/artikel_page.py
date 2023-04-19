import flet as ft
from src.ui.artikel import Article
from src.ui.dashboard import WelcomeMessage

class ArticlePage(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def build(self):
        return ft.Container(
            margin=ft.margin.only(left=40, top=10),
            content=ft.Column(
                controls=[
                    WelcomeMessage(),
                    Article(), # artikel 1
                    Article(), # artikel 2
                    Article(), # artikel 3
                ]
            )
        )