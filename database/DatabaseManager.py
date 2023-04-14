import Database
import sqlite3 as sql

class DatabaseManager:
    def __init__(self):
        self.databaseName = 'BudgetWise.db'
        self.pemasukan = Database.Pemasukan()
        self.transaksi = Database.Transaksi()
        self.target = Database.Target() 
        self.pengeluaran = Database.Pengeluaran()
        self.connection = None
        self.connectDatabase()

    def initializeTable(self):
        self.connectDatabase()
        self.createTable(self.pemasukan.name, self.pemasukan.attributes, self.pemasukan.attributeDescription)
        self.createTable(self.transaksi.name, self.transaksi.attributes, self.transaksi.attributeDescription)
        self.createTable(self.target.name, self.target.attributes, self.target.attributeDescription)
        self.createTable(self.pengeluaran.name, self.pengeluaran.attributes, self.pengeluaran.attributeDescription)
    
    def createTable(self, tableName, columns, attributeDescription):
        self.connection.execute("CREATE TABLE IF NOT EXISTS " + tableName + " (" + columns + " " + attributeDescription + ")")
        print("Table created")

    def connectDatabase(self):
        self.connection = sql.connect(self.databaseName)
        print("Database connected")

    def closeConnection(self):
        self.connection.close()
        print("Database connection closed")

    def commitChanges(self):
        self.connection.commit()
        print("Changes committed")
    
