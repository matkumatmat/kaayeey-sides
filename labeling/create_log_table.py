import sqlite3

# --- KONFIGURASI ---
DB_NAME = 'DbLabeling.db'
TABLE_NAME = 'LogLabelingAlamat'

def create_log_table():
    """Membuat tabel baru untuk mencatat semua aktivitas printing."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Hapus tabel jika sudah ada (opsional, berguna saat testing)
        cursor.execute(f'DROP TABLE IF EXISTS {TABLE_NAME}')

        # Membuat tabel 'LogLabelingAlamat'
        # 'tujuan_kirim_id' adalah foreign key ke tabel 'TujuanKirim'
        cursor.execute(f'''
        CREATE TABLE {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tujuan_kirim_id INTEGER NOT NULL,
            box_number TEXT,
            produk TEXT,
            qty_produk TEXT,
            petugas TEXT,
            berat TEXT,
            status TEXT DEFAULT 'printed',
            printer_ip TEXT,
            tanggal_print DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (tujuan_kirim_id) REFERENCES TujuanKirim (id)
        )
        ''')

        print(f"Database '{DB_NAME}' berhasil diperbarui dengan tabel '{TABLE_NAME}'.")
        conn.commit()

    except Exception as e:
        print(f"Terjadi error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    create_log_table()
