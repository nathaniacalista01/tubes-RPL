from typing import Optional, Any
import flet as ft
from src.ui.dashboard import WelcomeMessage
from src.ui.profile_card import ProfileCard


class ProfileCardForms(ft.UserControl):
    """Component for target's forms"""

    def __init__(
        self,
        # form_title: str,
        # default_values: Optional[ProfileCard] = None,
        profile_card_ref: ft.Ref[ProfileCard],
        ref: Optional[ft.Ref["ProfileCardForms"]] = None,
        on_submit: Any = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.profile_name = ft.Ref[ft.TextField]()
        self.profile_job = ft.Ref[ft.TextField]()
        self.profile_email = ft.Ref[ft.TextField]()
        self.profile_img_url = ft.Ref[ft.TextField]()
        self.ref = ref
        # self.ref.current = self
        self.on_submit = on_submit
        self.profile_card_ref = profile_card_ref
        self.default_values.profile_name = profile_card_ref.current.profile_name
        self.default_values.profile_job = profile_card_ref.current.profile_job
        self.default_values.profile_email = profile_card_ref.current.profile_email
        self.default_values.profile_img_url = profile_card_ref.current.profile_img_url
        # self.form_title = form_title

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
                        # error_text=ref.current.error_text
                        # if ref.current is not None
                        # else None,
                        value=value,
                    )
                ],
            ),
        )

    # @staticmethod
    # def new_forms(name: str, keyboard_type: ft.KeyboardType):
    #     """Components for new form's input"""
    #     return ft.Container(
    #         # expand=True,
    #         height=45,
    #         bgcolor="#ebebeb",
    #         border_radius=ft.border_radius.all(6),
    #         margin=ft.margin.only(top=10),
    #         padding=ft.padding.all(8),
    #         content=ft.Column(
    #             spacing=1,
    #             controls=[
    #                 ft.TextField(
    #                     border_color="transparent",
    #                     height=30,
    #                     text_size=13,
    #                     label=name,
    #                     label_style=ft.TextStyle(size=13),
    #                     content_padding=ft.padding.only(top=30),
    #                     cursor_color="black",
    #                     cursor_width=1,
    #                     cursor_height=18,
    #                     color="black",
    #                     keyboard_type=keyboard_type,
    #                 )
    #             ],
    #         ),
    #     )


    def submit(self, event: ft.ControlEvent):
        event.control.data = ProfileCard(
            profile_name=self.profile_name.current.value, 
            profile_job=self.profile_job.current.value,
            profile_email=self.profile_email.current.value, 
            profile_img_url=self.profile_img_url.current.value,
        )
        self.profile_name.current.value = ""
        self.profile_job.current.value = ""
        self.profile_email.current.value = ""
        self.profile_img_url.current.value = ""
        self.update()
        self.on_submit(event)

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
                    self.new_forms("Name",
                                   ft.KeyboardType.TEXT, 
                                   self.profile_name,
                                   None 
                                   if self.default_values is None 
                                   else self.default_values.profile_name),
                    self.new_forms("Job", 
                                   ft.KeyboardType.NUMBER,
                                   self.profile_job,
                                   None
                                   if self.default_values is None
                                   else self.default_values.profile_job),
                    self.new_forms("Email", 
                                   ft.KeyboardType.EMAIL,
                                   self.profile_email,
                                   None 
                                   if self.default_values is None 
                                   else self.default_values.profile_email),
                    self.new_forms("Profile Image URL", 
                                   ft.KeyboardType.URL,
                                   self.profile_img_url,
                                   None 
                                   if self.default_values is None 
                                   else self.default_values.profile_img_url),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.ElevatedButton(
                                width=200,
                                bgcolor="#6761B9",
                                color="white",
                                text="Change Profile",
                                on_click=self.submit
                            ),
                        ],
                    ),
                ],
            ),
        )


class SettingsPage(ft.UserControl):
    def __init__(self, profile_card_ref: ft.Ref[ProfileCard],**kwargs):
        self.profile_card_ref = profile_card_ref
        super().__init__(**kwargs)

    def build(self):
        return ft.Column(controls=[WelcomeMessage(), ProfileCardForms(profile_card_ref=self.profile_card_ref)])
