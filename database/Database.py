class Database:
    def __init__(self, name, attributes, attributeDescription):
        self.name = name
        self.attributes = attributes
        self.attributeDescription = attributeDescription

class Pemasukan(Database):
    def __init__(self):
        name = "Pemasukan"
        attributes = ["id_pemasukan", "nominal", "tanggal", "kategori", "catatan"]
        attributeDescription = ["INTEGER PRIMARY KEY AUTOINCREMENT", "INTEGER", "TEXT", "TEXT", "TEXT"]
        super().__init__(name, attributes, attributeDescription)

class Transaksi(Database):
    def __init__(self):
        name = "Transaksi"
        attributes = ["id_transaksi", "tipe_transaksi", "id_sumber"]
        attributeDescription = ["INTEGER PRIMARY KEY AUTOINCREMENT", "TEXT", "INTEGER"]
        super().__init__(name, attributes, attributeDescription)

class Target(Database):
    def __init__(self):
        name = "Target"
        attributes = ["id_target", "judul", "nominal_target", "catatan", "tanggal_dibuat", "tanggal_tercapai"]
        attributeDescription = ["INTEGER PRIMARY KEY AUTOINCREMENT", "TEXT", "INTEGER", "TEXT", "TEXT", "TEXT"]
        super().__init__(name, attributes, attributeDescription)

class Pengeluaran(Database):
    def __init__(self):
        name = "Pengeluaran"
        attributes = ["id_pengeluaran", "nominal", "tanggal", "kategori", "catatan"]
        attributeDescription = ["INTEGER PRIMARY KEY AUTOINCREMENT", "INTEGER", "TEXT", "TEXT", "TEXT"]
        super().__init__(name, attributes, attributeDescription)