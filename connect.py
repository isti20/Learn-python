import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = '',
)
if db.is_connected():
    print("berhasil")

# cursor = db.cursor()
# cursor.execute("CREATE DATABASE dbtest")

# Note:
# Folder module harus disimpan htdocs
# XAMPP harus dijalankan dulu baru bisa di test udah terkoneksi atau belum