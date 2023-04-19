from typing import Optional
import flet as ft
from src.ui.dashboard import WelcomeMessage


class ProfileCardForms(ft.UserControl):
    """Component for target's forms"""

    def __init__(
        self,
        profile_name: str = "Name",
        profile_job: str = "Job",
        profile_email: str = "Email",
        profile_img_url: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.profile_name = profile_name
        self.profile_job = profile_job
        self.profile_email = profile_email
        self.profile_img_url = profile_img_url

    @staticmethod
    def new_forms(name: str, keyboard_type: ft.KeyboardType):
        """Components for new form's input"""
        return ft.Container(
            # expand=True,
            height=45,
            bgcolor="#ebebeb",
            border_radius=ft.border_radius.all(6),
            margin=ft.margin.only(top=10),
            padding=ft.padding.all(8),
            content=ft.Column(
                spacing=1,
                controls=[
                    ft.TextField(
                        border_color="transparent",
                        height=30,
                        text_size=13,
                        label=name,
                        label_style=ft.TextStyle(size=13),
                        content_padding=ft.padding.only(top=30),
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                        keyboard_type=keyboard_type,
                    )
                ],
            ),
        )

    def build(self):
        return ft.Container(
            # expand=True,
            bgcolor="#FFFFFF",
            border=ft.border.all(1, "#ebebeb"),
            border_radius=20,
            padding=15,
            margin=ft.margin.only(top=10),
            content=ft.Column(
                # expand=True,
                controls=[
                    ft.Text(
                        value="Profile Settings",
                        size=32,
                        weight=ft.FontWeight.W_600,
                    ),
                    self.new_forms("Name", ft.KeyboardType.TEXT),
                    self.new_forms("Job", ft.KeyboardType.NUMBER),
                    self.new_forms("Email", ft.KeyboardType.EMAIL),
                    self.new_forms("Profile Image URL", ft.KeyboardType.URL),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.ElevatedButton(
                                width=200,
                                bgcolor="#6761B9",
                                color="white",
                                text="Change Profile",
                            ),
                        ],
                    ),
                ],
            ),
        )


class SettingsPage(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Column(controls=[WelcomeMessage(), ProfileCardForms()])
