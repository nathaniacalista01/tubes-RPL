"""Database Manager"""
import os.path
import sqlite3

from src.database import Pemasukan, Pengeluaran, Transaksi, Target


class DatabaseManager:
    """Class for database manager"""

    def __init__(self):
        self.pemasukan = Pemasukan()
        self.pengeluaran = Pengeluaran()
        self.transaksi = Transaksi()
        self.target = Target()
        filepath = os.path.join(os.path.dirname(__file__), "BudgetWise.db")
        self.connection = sqlite3.connect(filepath, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.initialize_tables()

    def create_table(self, table):
        """Function to create new table"""
        columns = ", ".join(
            [
                f"{column} {description}"
                for column, description in zip(
                    table.attributes, table.attribute_description
                )
            ]
        )
        self.connection.execute(f"CREATE TABLE IF NOT EXISTS {table.name} ({columns})")
        self.commit_changes()

        if table.name == "Pemasukan":
            self.insert_data(
                table.name,
                ["id_pemasukan", "nominal", "tanggal", "kategori", "catatan"],
                [9999, 9999, "2023-04-17", "dummy_kategori", "dummy_catatan"],
            )
            self.delete_data(table.name, "id_pemasukan = 9999")
        elif table.name == "Pengeluaran":
            self.insert_data(
                table.name,
                ["id_pengeluaran", "nominal", "tanggal", "kategori", "catatan"],
                [19999, 19999, "2023-04-17", "dummy_kategori", "dummy_catatan"],
            )
            self.delete_data(table.name, "id_pengeluaran = 19999")
        elif table.name == "Transaksi":
            self.insert_data(
                table.name,
                ["id_transaksi", "tipe_transaksi", "id_sumber"],
                [29999, "pemasukan", 29999],
            )
            self.delete_data(table.name, "id_transaksi = 29999")
        elif table.name == "Target":
            self.insert_data(
                table.name,
                [
                    "id_target",
                    "judul",
                    "nominal_target",
                    "catatan",
                    "tanggal_dibuat",
                    "tanggal_tercapai",
                ],
                [89999, "dummy_judul", 0, "dummy_catatan", "2023-04-17", "2023-04-17"],
            )
            self.delete_data(table.name, "id_target = 89999")
        print(f"Table {table.name} created")

    def initialize_tables(self):
        """Function to initialize table"""
        self.create_table(self.pemasukan)
        self.create_table(self.pengeluaran)
        self.create_table(self.transaksi)
        self.create_table(self.target)
        self.create_transactions_expense_view()
        self.create_transactions_income_view()

    def insert_data(self, table_name, columns, values, returning=False):
        """Function to insert data"""
        placeholders = ", ".join(["?" for _ in range(len(values))])
        query = (
            f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
            + (" RETURNING *" if returning else "")
        )
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        return_value = None
        print(f"Data inserted into {table_name}")
        if returning:
            try:
                return_value = cursor.fetchone()
            except StopIteration:
                return_value = None
        self.commit_changes()
        return return_value

    def update_data(self, table_name, columns, values, condition):
        """Function to update data"""
        set_statement = ", ".join([f"{column}=?" for column in columns])
        query = f"UPDATE {table_name} SET {set_statement} WHERE {condition}"
        self.connection.execute(query, values)
        self.commit_changes()
        print(f"Data updated in {table_name}")

    def delete_data(self, table_name, condition):
        """Function to delete data"""
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.connection.execute(query)
        self.commit_changes()
        print(f"Data deleted from {table_name}")

    def select_data(self, table_name, columns=None, condition=None):
        """Function to select data on some conditions"""
        column_list = "*" if columns is None else ",".join(columns)
        query = f"SELECT {column_list} FROM {table_name}"
        if condition is not None:
            query += f" WHERE {condition}"
        result = self.connection.execute(query)
        rows = result.fetchall()
        return rows

    def create_transactions_expense_view(self):
        """Function to create view of 2 tables"""
        query = """
                    create view if not exists transaksi_pengeluaran  as
                    select t.id_transaksi,t.tipe_transaksi,p.id_pengeluaran
                    ,p.nominal,p.tanggal,p.kategori,p.catatan
                    from Transaksi as t, Pengeluaran as p
                    where t.id_sumber = p.id_pengeluaran; 
                """
        self.connection.execute(query)

    def create_transactions_income_view(self):
        """Procedure to create view of transactions and income"""
        query = """
                    create view if not exists transaksi_pemasukan  as
                    select t.id_transaksi,t.tipe_transaksi,p.id_pemasukan
                    ,p.nominal,p.tanggal,p.kategori,p.catatan
                    from Transaksi as t, Pemasukan as p
                    where t.id_sumber = p.id_pemasukan;
                """
        self.connection.execute(query)

    def execute_query(self, query):
        """Function to execute query"""
        result = self.connection.execute(query)
        rows = result.fetchall()
        return rows

    def reset_database(self):
        """Function to reset database"""
        self.connection.execute("DROP TABLE IF EXISTS Pemasukan")
        self.connection.execute("DROP TABLE IF EXISTS Pengeluaran")
        self.connection.execute("DROP TABLE IF EXISTS Transaksi")
        self.connection.execute("DROP TABLE IF EXISTS Target")
        self.commit_changes()
        self.initialize_tables()
        print("Database reset")

    def commit_changes(self):
        """Function to make changes"""
        self.connection.commit()

    def show_data(self, table_name):
        """Function to show all datas from a table"""
        schema_query = f"PRAGMA table_info({table_name})"
        schema_result = self.connection.execute(schema_query)
        schema = schema_result.fetchall()

        data_query = f"SELECT * FROM {table_name}"
        data_result = self.connection.execute(data_query)
        data = data_result.fetchall()

        print("Table schema:")
        for column in schema:
            print(f"- Column '{column[1]}': {column[2]}")

        print("Table data:")
        for row in data:
            print(row)

    def fetch_data(self, table_name):
        """Function to fetch data from database"""
        query = f"SELECT * FROM {table_name}"
        result = self.connection.execute(query)
        rows = result.fetchall()
        return rows

    def get_income(self):
        """Get income"""
        total_pemasukan = self.execute_query("SELECT SUM(nominal) FROM Pemasukan")[0][
            "SUM(nominal)"
        ]
        if total_pemasukan:
            pass
        else:
            total_pemasukan = 0
        return total_pemasukan

    def get_expense(self):
        """Get expense"""
        total_pengeluaran = self.execute_query("SELECT SUM(nominal) FROM Pengeluaran")[
            0
        ]["SUM(nominal)"]
        if total_pengeluaran:
            pass
        else:
            total_pengeluaran = 0
        return total_pengeluaran

    def get_saldo(self):
        """Get saldo"""
        return self.get_income() - self.get_expense()

    def group_expense_by_category(self):
        """Group by category"""
        query = """
                    SELECT SUM(nominal) as total, kategori from Pengeluaran
                    GROUP BY kategori 
                    ORDER BY SUM(nominal) DESC
                    LIMIT 3
                """
        result = self.connection.execute(query)
        data = []
        for rows in result:
            data.append(
                {
                    "kategori": rows["kategori"],
                    "total": rows["total"],
                    "persen": rows["total"] / self.get_expense() * 100,
                }
            )
        if len(data) < 3:
            return data
        else:
            total = 0
            for item in data:
                total += item["total"]
            if total < self.get_expense():
                other_value = self.get_expense() - total
                data.append(
                    {
                        "kategori": "other",
                        "total": other_value,
                        "persen": other_value / self.get_expense() * 100,
                    }
                )
                return data
            return data

    def group_income_by_category(self):
        """Group by category"""
        query = """
                    SELECT SUM(nominal) as total, kategori from Pemasukan
                    GROUP BY kategori 
                    ORDER BY SUM(nominal) DESC
                    LIMIT 3
                """
        result = self.connection.execute(query)
        data = []
        for rows in result:
            data.append(
                {
                    "kategori": rows["kategori"],
                    "total": rows["total"],
                    "persen": rows["total"] / self.get_income() * 100,
                }
            )
        if len(data) < 3:
            return data
        else:
            total = 0
            for item in data:
                total += item["total"]
            if total < self.get_income():
                other_value = self.get_income() - total
                data.append(
                    {
                        "kategori": "other",
                        "total": other_value,
                        "persen": other_value / self.get_income() * 100,
                    }
                )
                return data
            return data
