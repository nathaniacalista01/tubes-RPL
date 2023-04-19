"""Handle BudgetWise's Database"""


class Database:
    """Parent class for all other database's classes"""

    def __init__(self, name, attributes, attribute_description):
        self.name = name
        self.attributes = attributes
        self.attribute_description = attribute_description


class Pemasukan(Database):
    """Class for Pemasukan"""

    def __init__(self):
        name = "Pemasukan"
        attributes = ["id_pemasukan", "nominal", "tanggal", "kategori", "catatan"]
        attribute_description = [
            "INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 10000",
            "INTEGER",
            "TEXT",
            "TEXT",
            "TEXT",
        ]
        super().__init__(name, attributes, attribute_description)


class Transaksi(Database):
    """Class for Transaksi"""

    def __init__(self):
        name = "Transaksi"
        attributes = ["id_transaksi", "tipe_transaksi", "id_sumber"]
        attribute_description = [
            "INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 30000",
            "TEXT",
            "INTEGER REFERENCES Pemasukan(id_pemasukan) ON DELETE CASCADE, FOREIGN KEY (id_sumber) REFERENCES Pengeluaran(id_pengeluaran) ON DELETE CASCADE",
        ]
        super().__init__(name, attributes, attribute_description)


class Target(Database):
    """Class to handle Target Database"""

    def __init__(self):
        name = "Target"
        attributes = [
            "id_target",
            "judul",
            "nominal_target",
            "catatan",
            "tanggal_dibuat",
            "tanggal_tercapai",
        ]
        attribute_description = [
            "INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 90000",
            "TEXT",
            "INTEGER",
            "TEXT",
            "DATE",
            "DATE",
        ]
        super().__init__(name, attributes, attribute_description)


class Pengeluaran(Database):
    """Class to handle Pengeluaran Database"""

    def __init__(self):
        name = "Pengeluaran"
        attributes = ["id_pengeluaran", "nominal", "tanggal", "kategori", "catatan"]
        attribute_description = [
            "INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 20000",
            "INTEGER",
            "TEXT",
            "TEXT",
            "TEXT",
        ]
        super().__init__(name, attributes, attribute_description)
