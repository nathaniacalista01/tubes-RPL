"""Target component module"""

import datetime

from flet import ProgressBar, Divider, Icon, alignment
from flet_core import (
    UserControl,
    Column,
    CrossAxisAlignment,
    Container,
    Padding,
    Margin,
    Text,
    TextAlign,
    Row,
    border,
    ElevatedButton,
    TextField,
)

class Target(UserControl):
    """Budgetwise Target Component"""

    def __init__(
        self,
        target_title: str = "Target Title",
        target_description: str = "Target Description",
        percentage: float = 0.3,
        start_date: datetime = datetime.date.today(),
        end_date: datetime = datetime.date(datetime.datetime.now().year + 1, datetime.datetime.now().month, datetime.datetime.now().day),
        icon: str = "fact_check",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.target_title = target_title
        self.target_description = target_description
        self.percentage = percentage
        self.start_date = start_date
        self.end_date = end_date
        self.icon = icon

    def build(self):
        return Column(
            width=230,
            # alignment=alignment.top_center,
            alignment=CrossAxisAlignment.CENTER,
            controls=[
                Container(
                    bgcolor="#F1ECFF",
                    padding=Padding(15,15,15,15),
                    margin=20,
                    border_radius=20,
                    border=border.all(color="black"),
                    content=Column(
                        spacing=0,
                        controls=[
                            Row(
                                controls=[
                                    Container(
                                        Icon(name=self.icon,size=50),
                                    ),
                                    Column(
                                        spacing=3,
                                        width=100,
                                        height=70,
                                        controls=[
                                            Container(
                                                content=Text(
                                                    value=self.target_title,
                                                    text_align=TextAlign.LEFT,
                                                    size=11,
                                                    color="black",
                                                ),
                                            ),
                                            Divider(height=0,color="black"),
                                            Container(
                                                padding=Padding(0,0,0,10),
                                                content=Text(
                                                    value=self.target_description,
                                                    text_align=TextAlign.LEFT,
                                                    size=7,
                                                    color="black",
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            ProgressBar(width=190,bar_height=10,color="#1FC3E8",bgcolor="#385682",value=self.percentage),
                            Container(
                                alignment=alignment.center_right,
                                content=Text(value=str(self.percentage*100) + "% completed", color="#6182B2", size=8, text_align=TextAlign.RIGHT),
                                padding=Padding(0,0,0,10)
                            ),
                            Row(
                                controls=[
                                    Column(
                                        spacing=2,
                                        controls=[
                                            Text(value="Start Date :", color="#2B9F18",size=9),
                                            Text(value="End Date   :", color="#EF6161",size=9)
                                        ]
                                    ),
                                    Column(
                                        spacing=2,
                                        controls=[
                                            Text(value=self.start_date.strftime("%d %B %Y"), size=9),
                                            Text(value=self.end_date.strftime("%d %B %Y"), size=9)
                                        ]
                                    ),
                                ]
                            )
                        ]
                    )
                ),
                Container(
                    height=20, width=230,
                    padding=Padding(20,0,20,0),
                    content=Row(
                        controls=[
                            ElevatedButton(text="Edit",color="black",bgcolor="#D9D9D9",width=90),
                            ElevatedButton(text="Delete",color="black",bgcolor="#D9D9D9",width=90),
                        ]
                    )                         
                )
            ]
        )
    

class TargetForm(UserControl):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Column(
            width=1070,
            controls=[
                Container(
                    bgcolor="white",                     
                    height=270,
                    padding=Padding(10,10,10,10),
                    margin=Margin(20,20,20,10),
                    border_radius=20,
                    content=Column(
                        controls=[
                            Container(
                                height=25,
                                content=TextField(label="Title",text_size=12)
                            ),
                            Container(
                                height=25,
                                content=TextField(label="Nominal",text_size=12)
                            ),
                            Container(
                                height=25,
                                content=TextField(label="Target Date",text_size=12)
                            ),
                            Container(
                                height=100,
                                content=TextField(label="Descriptions",border="underline",text_size=12,multiline=True)
                            ),
                            Container(
                                alignment=alignment.center_right,
                                content=ElevatedButton(text="Add Target", bgcolor="#00FF47")
                            )
                        ]
                    )
                ),
            ]
        )