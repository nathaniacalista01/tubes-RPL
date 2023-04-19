"""Profile card component module"""

from typing import Optional

from flet_core import (
    UserControl,
    Column,
    CrossAxisAlignment,
    Container,
    Padding,
    Margin,
    BoxShadow,
    Offset,
    ShadowBlurStyle,
    MainAxisAlignment,
    CircleAvatar,
    Text,
    TextAlign,
    FontWeight,
)


class ProfileCard(UserControl):
    """BudgetWise Profile Card Component"""

    def __init__(
        self,
        profile_name: str = "Name here",
        profile_job: str = "Job here",
        profile_email: str = "Email here",
        profile_img_url: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.profile_name = profile_name
        self.profile_job = profile_job
        self.profile_email = profile_email
        self.profile_img_url = profile_img_url

    def build(self):
        return Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Container(
                    bgcolor="#222158",
                    padding=Padding(30, 35, 30, 15),
                    margin=Margin(0, 0, 0, 5),
                    border_radius=20,
                    shadow=BoxShadow(
                        spread_radius=1,
                        blur_radius=0,
                        color="#F7E322",
                        offset=Offset(3, 8),
                        blur_style=ShadowBlurStyle.NORMAL,
                    ),
                    content=Column(
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            Container(
                                content=CircleAvatar(
                                    radius=70,
                                    foreground_image_url=self.profile_img_url,
                                    content=None
                                    if self.profile_img_url is not None
                                    else Text("Picture here"),
                                ),
                            ),
                            Container(
                                margin=Margin(0, 15, 0, 0),
                                content=Text(
                                    value=self.profile_name,
                                    text_align=TextAlign.CENTER,
                                    size=20,
                                    color="white",
                                ),
                            ),
                            Container(
                                margin=Margin(0, -5, 0, 0),
                                content=Text(
                                    value=self.profile_job,
                                    text_align=TextAlign.CENTER,
                                    weight=FontWeight.BOLD,
                                    size=12,
                                    color="#61609A",
                                ),
                            ),
                            Container(
                                margin=Margin(0, 10, 0, 5),
                                padding=Padding(5, 2, 5, 2),
                                border_radius=5,
                                bgcolor="#6761B9",
                                content=Text(
                                    value=self.profile_email,
                                    color="white",
                                    size=10,
                                    text_align=TextAlign.CENTER,
                                ),
                            ),
                        ],
                    ),
                ),
                Text(
                    "© Powered by BudgetWise",
                    color="white",
                    size=8,
                ),
            ],
        )
