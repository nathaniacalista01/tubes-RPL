"""Target Page module"""

from ui.target import Target, TargetForm
from ui.Dashboard import WelcomeMessage
import datetime

from flet import ProgressBar, Divider, Icon, alignment
from flet_core import (
    UserControl,
    Column,
    CrossAxisAlignment,
    Container,
    Padding,
    Margin,
    BoxShadow,
    Offset,
    MainAxisAlignment,
    Text,
    TextAlign,
    FontWeight,
    Row,
)

class TargetPage(UserControl):
    """Budgetwise Target Page"""

    def __init__(
        self,
        date: datetime = datetime.date.today(),
        **kwargs
    ):
        super().__init__(**kwargs)
        self.date = date

    def build(self):
        return Container(
            margin=Margin(40,10,0,0),
            content=Column(
                width=1070,
                controls=[
                    WelcomeMessage(),
                    TargetForm(),
                    Container(
                        bgcolor="white",                     
                        height=270,
                        width=1070,
                        padding=Padding(10,10,0,0),
                        margin=Margin(0,10,20,0),
                        border_radius=20,
                        content=Column(
                                controls=[
                                    Container(
                                        content=Text(value="Targets", size=20),
                                        padding=Padding(10,5,0,0)
                                    ),
                                    Container(
                                        content=Row(
                                            controls=[
                                                Target(),
                                                Target(target_title="Beli iphone 20",
                                                    target_description="iPhone adalah kebutuhan yang aku perlukan untuk hidup :)",
                                                    percentage=0.7,icon="phone_iphone")
                                            ]
                                        )
                                    )
                                ]
                        )
                    )                          
                ]
            )
        ) 