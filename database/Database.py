class Database:
    def __init__(self):
        self.name = None
        self.attributes = None
        self.attributeDescription = None

    def insertData(self, tableName, columns, values):
        ...
    
    def updateData(self, tableName, columns, values, condition):
        ...

    def deleteData(self, tableName, condition):
        ...

class Pemasukan(Database):
    def __init__(self):
        Database.__init__(self)
        self.name = "Pemasukan"
        self.attributes = ["id_pemasukan", "nominal", "tanggal", "kategori", "catatan"]
        self.attributeDescription = ["INTEGER PRIMARY KEY AUTOINCREMENT", "INTEGER", "TEXT", "TEXT", "TEXT"]

class Transaksi(Database):
    def __init__(self):
        Database.__init__(self)
        self.name = "Transaksi"

class Target(Database):
    def __init__(self):
        Database.__init__(self)
        self.name = "Target"

class Pengeluaran(Database):
    def __init__(self):
        Database.__init__(self)
        self.name = "Pengeluaran"