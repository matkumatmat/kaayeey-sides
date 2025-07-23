import sqlite3 as sq

conn = sq.connect('DbLabeling')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE TujuanKirim(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       PT TEXT NOT NULL ,
       PT_TUJUAN TEXT NOT NULL,
       INSTANSI TEXT NOT NULL,
       TUJUAN TEXT NOT NULL,
       ALAMAT TEXT NOT NULL,
       PROVINSI TEXT NOT NULL,
       KONTAK TEXT,
)
''')
print( f"db Labeling {conn} dan tabel 'TujuanKirim' berhasil dibuat ")
conn.commit()
conn.close()
