"""Module that manage all databases"""
import sqlite3
import database

class DatabaseManager:
    """Clas for database manager """
    def __init__(self):
        self.pemasukan = database.Pemasukan()
        self.pengeluaran = database.Pengeluaran()
        self.transaksi = database.Transaksi()
        self.target = database.Target()
        self.connection = sqlite3.connect("BudgetWise.db")
        self.connection.row_factory = sqlite3.Row
        self.initialize_tables()

    def create_table(self, table):
        """Function to create new table"""
        columns = ', '.join([f'{column} {description}' for column,
                             description in zip(table.attributes, table.attributeDescription)])
        self.connection.execute(f"CREATE TABLE IF NOT EXISTS {table.name} ({columns})")
        self.commit_changes()

        if table.name == "Pemasukan":
            self.insert_data(table.name, ["id_pemasukan", "nominal", "tanggal",
                                          "kategori", "catatan"],
                              [9999, 9999, "2023-04-17", "dummy_kategori", "dummy_catatan"])
            self.delete_data(table.name, "id_pemasukan = 9999")
        elif table.name == "Pengeluaran":
            self.insert_data(table.name, ["id_pengeluaran", "nominal", "tanggal",
                                          "kategori", "catatan"],
                              [19999, 19999, "2023-04-17", "dummy_kategori", "dummy_catatan"])
            self.delete_data(table.name, "id_pengeluaran = 19999")
        elif table.name == "Transaksi":
            self.insert_data(table.name, ["id_transaksi", "tipe_transaksi", "id_sumber"],
                              [29999, "pemasukan", 29999])
            self.delete_data(table.name, "id_transaksi = 29999")
        elif table.name == "Target":
            self.insert_data(table.name, ["id_target", "judul", "nominal_target", "catatan",
                                        "tanggal_dibuat", "tanggal_tercapai"], 
                                        [89999,"dummy_judul", 0, "dummy_catatan", "2023-04-17",
                                         "2023-04-17"])
            self.delete_data(table.name, "id_target = 89999")
        print(f"Table {table.name} created")

    def initialize_tables(self):
        """Function to initialize table"""
        self.create_table(self.pemasukan)
        self.create_table(self.pengeluaran)
        self.create_table(self.transaksi)
        self.create_table(self.target)

    def insert_data(self, table_name, columns, values):
        """Function to insert data"""
        placeholders = ', '.join(['?' for _ in range(len(values))])
        query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
        self.connection.execute(query, values)
        self.commit_changes()
        print(f"Data inserted into {table_name}")

    def update_data(self, table_name, columns, values, condition):
        """Function to update data"""
        set_statement = ', '.join([f"{column}=?" for column in columns])
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
        """Function to delete data on some conditions"""
        column_list = '*' if columns is None else ','.join(columns)
        query = f"SELECT {column_list} FROM {table_name}"
        if condition is not None:
            query += f" WHERE {condition}"
        result = self.connection.execute(query)
        rows = result.fetchall()
        return rows
    def execurte_query(self, query):
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
