"""Driver for database"""
import src.database.database_manager as database_manager

db = database_manager.DatabaseManager()
# Contoh insert
# columns = ["nominal", "tanggal", "kategori", "catatan"]
# values = [1000, "2022-01-01", "Gaji", "Pembayaran gaji bulan Januari"]
columns = ["nominal", "tanggal", "kategori", "catatan"]
values = [
    [2000, "2022-01-02", "Bonus", "Pembayaran bonus bulan Januari"],
    [1500, "2022-01-03", "Gaji", "Pembayaran gaji bulan Februari"],
    [3000, "2022-01-04", "Bonus", "Pembayaran bonus bulan Februari"],
]

for value in values:
    db.insert_data("Pemasukan", columns, value)

# Contoh update
# columns = ["nominal", "tanggal"]
# values = [1500, "2022-01-02"]
# condition = "id_pemasukan=1"
# db.update_data("Pemasukan", columns, values, condition)


# Contoh delete
# condition = "id_pemasukan=1"
# db.delete_data("Pemasukan", condition)

# Contoh select
# rows = db.select_data("Pemasukan")
# for row in rows:
#     print(row["id_pemasukan"], row["nominal"], row["tanggal"], row["kategori"], row["catatan"])

# columns = ["nominal", "tanggal"]
# rows = db.select_data("Pemasukan", columns)
# for row in rows:
#     print(row["nominal"], row["tanggal"])

# Buat cek data
# db.show_data("Pemasukan")
rows = db.fetch_data("Pemasukan")
for row in rows:
    print(
        row["id_pemasukan"],
        row["nominal"],
        row["tanggal"],
        row["kategori"],
        row["catatan"],
    )
