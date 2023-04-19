import flet as ft
import src.database as db


class Saldo(ft.UserControl):
    """Class to get saldo"""

    def __init__(self, db_ref=ft.Ref[db.DatabaseManager], **kwargs):
        super().__init__(**kwargs)
        self.db_ref = db_ref

    def get_saldo(self):
        """Mengembalikan nilai saldo berdasarkan query"""
        return self.db_ref.current.get_saldo()

    def get_income(self):
        """Mengembalikan nilai income"""
        return self.db_ref.current.get_income()

    def get_expense(self):
        """Mengembalikan nilai expense"""
        return self.db_ref.current.get_expense()
