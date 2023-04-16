"""Target Page module"""

from ui.target import Target, TargetForm
from typing import Optional
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
        return Column(
            width=1070,
            controls=[
                TargetForm(),
                Container(
                    bgcolor="white",                     
                    height=300,
                    width=1070,
                    padding=Padding(10,10,10,10),
                    margin=Margin(20,10,20,10),
                    border_radius=20,
                    content=Column(
                            controls=[
                                Container(
                                    content=Text(value="Targets", size=20),
                                    padding=Padding(20,10,0,0)
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