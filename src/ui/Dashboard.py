from flet_core import (
    UserControl,
    Text,
    Container, 
    Column, 
    Row,
    Margin,
    FontWeight, 
    Padding,
    TextAlign, 
    BoxShadow, 
    Image, 
    MainAxisAlignment, 
    LineChartData, 
    LineChartDataPoint, 
    colors, 
    LineChart,
    ChartAxis,
    ChartAxisLabel
)

class WelcomeMessage(UserControl):
    def __init__(self, welcome_str : str = "Hello, Jane Doe",**kwargs):
        super().__init__(**kwargs)
        self.welcome_message = welcome_str 
    def build(self):
        return(
            Row(
                controls=[
                    Column(
                        controls=[
                            Text(value=self.welcome_message, size=32,weight=FontWeight.W_700),
                            Text(value="4.45 pm 15 April 2023", weight=FontWeight.W_700,size=13)
                        ]
                    )
                ]
            )
        )

class SaldoCard(UserControl):
    def __init__ (
        self,
        title : str = "Balances",
        total_income : str = "Total Income",
        total_expense : str = "Total Expense",
        total_balance : str = "Total Balance",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = title
        self.total_income = total_income
        self.total_expenes = total_expense
        self.total_balance = total_balance
    
    def build(self):
        return(
            Container(
                bgcolor = "#FFFFFF",
                margin = Margin(0,20,0,0),
                padding = Padding(20,30,20,0),
                border_radius = 20,
                expand=True,
                content=
                    Column(
                        controls=[
                            Text(value=self.title,size=32,weight=FontWeight.W_700),
                            Text(value=self.total_income, color="#793DFD"),
                            # Masukin Jumlah Pemasukan 
                            Text(value = "6.025.440,00", size=16,weight=FontWeight.W_600),

                            Text(value=self.total_expenes, color="#793DFD", size=16),
                            #Jumlah pengeluaran
                            Text(value = "4.502.440,00", size=16,weight=FontWeight.W_600),
                            
                            Text(value = self.total_balance,color="#793DFD"),
                            Text(value="2.000.000,00",size=16, weight=FontWeight.W_600)
                        ]
                    )            
            )
        )

class SaldoOverviewFirstRow(UserControl):
    def __init__(
        self,
        title : str = "Balance Overview",
        first_button : str = "All",
        second_button : str = "1M",
        third_button : str = "3M",
        fourth_button : str = "6M",
        fifth_button : str = "1Y",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = title
        self.first_button = first_button
        self.second_button = second_button
        self.third_button = third_button
        self.fourth_button = fourth_button
        self.fifth_button = fifth_button
    
    def build(self):
        return(
            Row(
                controls=[
                    Container(
                        content=Text(value=self.title,size=32,weight=FontWeight.W_600),
                        expand = 2,
                    ),
                    Container(
                        margin = Margin(0,0,10,0),
                        content =
                            Row(
                                controls = [
                                    Container(
                                        margin=Margin(0, 10, 0, 5),
                                        padding = Padding(8,2,8,2),
                                        border_radius=10,
                                        bgcolor="#FFFFFF",
                                        content=Text(
                                            value=self.first_button,
                                            color="black",
                                            size=16,
                                            text_align=TextAlign.CENTER,
                                        ),
                                        shadow= BoxShadow(
                                            spread_radius=0.01,
                                            blur_radius=0.2,                                            
                                        )
                                    ),
                                    Container(
                                        margin=Margin(0, 10, 0, 5),
                                        padding = Padding(8,2,8,2),
                                        border_radius=10,
                                        bgcolor="#FFFFFF",
                                        content=Text(
                                            value=self.second_button,
                                            color="black",
                                            size=16,
                                            text_align=TextAlign.CENTER,
                                        ),
                                        shadow= BoxShadow(
                                            spread_radius=0.01,
                                            blur_radius=0.2,
                                            color="black",
                                            
                                        )
                                    ),
                                    Container(
                                        margin=Margin(0, 10, 0, 5),
                                        padding = Padding(8,2,8,2),
                                        border_radius=10,
                                        bgcolor="#FFFFFF",
                                        content=Text(
                                            value=self.third_button,
                                            color="black",
                                            size=16,
                                            text_align=TextAlign.CENTER,
                                        ),
                                        shadow= BoxShadow(
                                            spread_radius=0.01,
                                            blur_radius=0.2,
                                            color="black",
                                            
                                        )
                                    ),
                                    Container(
                                        margin=Margin(0, 10, 0, 5),
                                        padding = Padding(8,2,8,2),
                                        border_radius=10,
                                        bgcolor="#FFFFFF",
                                        content=Text(
                                            value=self.fourth_button,
                                            color="black",
                                            size=16,
                                            text_align=TextAlign.CENTER,
                                        ),
                                        shadow= BoxShadow(
                                            spread_radius=0.01,
                                            blur_radius=0.2,
                                            color="black",
                                        )
                                    ),
                                    Container(
                                        margin=Margin(0, 10, 0, 5),
                                        padding = Padding(8,2,8,2),
                                        border_radius=10,
                                        bgcolor="#FFFFFF",
                                        content=Text(
                                            value=self.fifth_button,
                                            color="black",
                                            size=16,
                                            text_align=TextAlign.CENTER,
                                        ),
                                        shadow= BoxShadow(
                                            spread_radius=0.01,
                                            blur_radius=0.2,
                                            color="black",
                                            
                                        )
                                    )
                                ],
                                expand=1
                            )
                        )
                ]
            )
        )

class SaldoOverviewSecondRow(UserControl):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def build(self):
        return (
            Row(
                alignment= MainAxisAlignment.START,
                controls=[
                    Container(
                        expand=2,
                        margin = 0,
                        content=Row(
                                controls=[
                                    Image( src = "images/stonks.svg"),
                                    Text(value="6.5%", size=12)
                                ]
                            )),
                    Container(
                        expand=1,
                        content= Row(
                            controls=[
                                Container(
                                    expand = 1,
                                    content=(
                                        Image(
                                            src="images/green-button.svg"
                                        )
                                    )    
                                ),
                                Container(
                                    expand = 2,
                                    content=(
                                        Text(value="Income")
                                    )
                                ),
                                Container(
                                    expand = 1,
                                    content=(
                                        Image(src="images/purple-button.svg")
                                    )
                                ),
                                Container(
                                    expand = 2,
                                    content=Text(value="Expense")
                                )
                            ]
                        )
                    )
                ]
            )
        )

class SaldoChart(UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        data_1 = [
        LineChartData(
            data_points=[
                LineChartDataPoint(1, 1),
                LineChartDataPoint(3, 1.5),
                LineChartDataPoint(5, 1.4),
                LineChartDataPoint(7, 3.4),
                LineChartDataPoint(10, 2),
                LineChartDataPoint(12, 2.2),
                LineChartDataPoint(13, 1.8),
            ],
            stroke_width=4,
            color="#00DEA3",
            stroke_cap_round=True,
        ),
        LineChartData(
            data_points=[
                LineChartDataPoint(1, 1),
                LineChartDataPoint(3, 2.8),
                LineChartDataPoint(7, 1.2),
                LineChartDataPoint(10, 2.8),
                LineChartDataPoint(12, 2.6),
                LineChartDataPoint(13, 3.9),
            ],
            color=colors.PINK,
            below_line_bgcolor=colors.with_opacity(0, colors.PINK),
            stroke_width=4,
            stroke_cap_round=True,
        ),
        
    ]
        return(
            Container(
                content=
                    LineChart(
                        data_series=data_1,
                        height=200
                    )
            )
            
        )

class SaldoOverview(UserControl):
    def __init__(
        self,
        **kwargs
    ):
        
        super().__init__(**kwargs)
    
    def build(self):
        return(
            Container(
                margin = Margin(0,30,0,0),
                padding = Padding(20,30,20,0),
                border_radius = 20,
                bgcolor = "#FFFFFF",
                content=
                    Column(
                        controls=[
                            SaldoOverviewFirstRow(),
                            SaldoOverviewSecondRow(),
                            SaldoChart()
                        ]
                    )  

            )
        )

class BalanceRow(UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return(
            Container(
                expand=True,
                content=
                    Row(
                        controls=[
                            SaldoOverview(expand = 3),
                            SaldoCard(expand = 1)
                        ]
                    )
            )
            
        )

class RecentTransactions(UserControl) :
    
    def __init__(
        self,
        column_one : str = "Category\nIcon",
        column_two : str = "Category",
        column_three : str = "Transaction\nTime",
        column_four : str ="Transaction\nAmount",
        column_five: str ="Type",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.height = super().height
        self.column_one = column_one
        self.column_two = column_two
        self.column_three = column_three
        self.column_four = column_four
        self.column_five = column_five
    
    def build(self): 
        return(
            Container(
                bgcolor = "#E9EFFD",
                content =[
                    Text(value="This is table")
                ]
            )
        )

class Targets(UserControl):
    def __init__(
        self, 
        **kwargs

    ):
        super().__init__(**kwargs)
    def build(self):
        return(
            Container(
                content=[
                    Column(
                        controls=[
                            
                        ]
                    )
                ]
            )
        )

class RecentTransactionTarget(UserControl):
    def __init__(self, **kwargs,):
        super().__init__(**kwargs)
    
    def build(self):
        Container(
            content=
                Row(
                    controls=[
                        RecentTransactions(expand=5),
                    ]
                )
        )

class Dashboard(UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def build(self):
        return (
            Container(
                margin = Margin(40,30,0,0),
                content=
                    Column(
                        controls=[
                            WelcomeMessage(),
                            BalanceRow(),
                            
                        ]
                    )
                
            )
           
        )
