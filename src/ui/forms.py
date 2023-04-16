"""Components for creating transactions forms"""

from flet_core import(
    Container,
    Row,
    Column,
    Text,
    FontWeight,
    TextField,
    TextAlign,
    border,
    UserControl, Margin,Padding,TextStyle, Dropdown, dropdown, ElevatedButton, OutlinedButton
)

class TransactionsForms(UserControl):
    def __init__(
            self,
            category : str = "Category",
            amount : str = "Transaction Amount",
            notes : str = "Notes",
            transaction_type : str = "Type",
            **kwargs
        ):
        super().__init__(**kwargs)
        self.category = category
        self.amount = amount
        self.notes = notes
        self.type = transaction_type
    
    def dropdown(self, name : str):
        return(
             Container(
                expand=True,
                height=45,
                bgcolor="#ebebeb",
                border_radius=6,
                margin= Margin(0,10,0,0),
                padding=8,
                content=
                    Column(
                        spacing=1,
                        controls=[
                            Dropdown(
                                expand=True,
                                border_color="transparent",
                                height=30,
                                text_size=13,
                                label_style = TextStyle(size=13),
                                label=name,
                                color="black",
                                content_padding=Padding(0,14,0,0),
                                options=[
                                    dropdown.Option("Expense"),
                                    dropdown.Option("Income")
                                ]
                            )
                        ]
                    )
                )
        )

    def new_forms(self, name : str):
        return(
            Container(
                expand=True,
                height=45,
                bgcolor="#ebebeb",
                border_radius=6,
                margin = Margin(0,10,0,0),
                padding=8,
                content=
                    Column(
                        spacing=1,
                        controls=[
                            # Text(value=name,size=9,color="black",weight="bold"),
                            TextField(
                                border_color="transparent",
                                height=30,
                                text_size=13,
                                label=name,
                                label_style = TextStyle(size=13),
                                content_padding=Padding(0,30,0,0),
                                cursor_color="black",
                                cursor_width=1,
                                cursor_height=18,
                                color="black"
                            )
                        ]
                    )
                )
            )
    def build(self):
        return(
            Container(
                expand=True,
                bgcolor="#FFFFFF",
                border=border.all(1,"#ebebeb"),
                border_radius=20,
                padding=15,
                margin = Margin(0,10,0,0),
                content=
                    Column(
                        expand=True,
                        controls=[
                            Text(value="Add Transactions",size=32,weight=FontWeight.W_600),
                            Row(
                                controls=[self.new_forms(self.notes)]
                            ),
                            Row(
                                controls=[
                                    self.new_forms(self.amount),
                                    self.new_forms(self.category),
                                    self.dropdown(self.type)
                                ]
                            ),
                            Container(
                                margin=Margin(0, 10, 0, 5),
                                padding=10,
                                border_radius=15,
                                width = 100,
                                bgcolor="#6761B9",
                                content=Text(
                                    value="Add",
                                    color="white",
                                    size=15,
                                    text_align=TextAlign.CENTER,
                                ),
                            ),
                        ]
                    )
            )
        )
        
