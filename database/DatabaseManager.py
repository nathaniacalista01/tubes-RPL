import sqlite3, Database

class DatabaseManager:
    def __init__(self):
        self.pemasukan = Database.Pemasukan()
        self.pengeluaran = Database.Pengeluaran()
        self.transaksi = Database.Transaksi()
        self.target = Database.Target()
        self.connection = sqlite3.connect("BudgetWise.db")
        self.connection.row_factory = sqlite3.Row

    def create_table(self, table):
        columns = ', '.join([f'{column} {description}' for column, description in zip(table.attributes, table.attributeDescription)])
        self.connection.execute(f"CREATE TABLE IF NOT EXISTS {table.name} ({columns})")
        print(f"CREATE TABLE IF NOT EXISTS {table.name} ({columns})", end='\n')
        self.commit_changes()
        print(f"Table {table.name} created")

    def initialize_tables(self):
        self.create_table(self.pemasukan)
        self.create_table(self.pengeluaran)
        self.create_table(self.transaksi)
        self.create_table(self.target)

    def insert_data(self, table_name, columns, values):
        placeholders = ', '.join(['?' for _ in range(len(values))])
        query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
        self.connection.execute(query, values)
        self.commit_changes()
        print(f"Data inserted into {table_name}")

    def update_data(self, table_name, columns, values, condition):
        set_statement = ', '.join([f"{column}=?" for column in columns])
        query = f"UPDATE {table_name} SET {set_statement} WHERE {condition}"
        self.connection.execute(query, values)
        self.commit_changes()
        print(f"Data updated in {table_name}")

    def delete_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.connection.execute(query)
        self.commit_changes()
        print(f"Data deleted from {table_name}")

    def select_data(self, table_name, columns=None, condition=None):
        column_list = '*' if columns is None else ','.join(columns)
        query = f"SELECT {column_list} FROM {table_name}"
        if condition is not None:
            query += f" WHERE {condition}"
        result = self.connection.execute(query)
        rows = result.fetchall()
        return rows
    
    def executeQuery(self, query):
        result = self.connection.execute(query)
        rows = result.fetchall()
        return rows
    
    def commit_changes(self):
        self.connection.commit()

    def show_data(self, table_name):
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
        query = f"SELECT * FROM {table_name}"
        result = self.connection.execute(query)
        rows = result.fetchall()
        return rows

