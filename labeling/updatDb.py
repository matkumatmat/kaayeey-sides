import sqlite3

# --- KONFIGURASI ---
DB_NAME = 'DbLabeling.db'
TABLE_NAME = 'TujuanKirim'

def update_pt_tujuan_column():
    """
    Menjalankan perintah SQL UPDATE untuk mengisi kolom 'pt_tujuan'
    berdasarkan gabungan dari kolom 'pt' dan 'tujuan'.
    """
    try:
        # Buat koneksi ke database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Ini adalah perintah SQL-nya.
        # '||' adalah operator untuk menggabungkan teks di SQLite.
        sql_command = f"""
        UPDATE {TABLE_NAME}
        SET pt_tujuan = pt || '  ' || tujuan
        WHERE pt_tujuan IS NULL OR pt_tujuan = '';
        """
        # Kondisi WHERE ditambahkan untuk efisiensi,
        # hanya meng-update baris yang pt_tujuan-nya masih kosong.

        print("Menjalankan perintah UPDATE pada database...")
        print(f"SQL Command: \n{sql_command}")
        
        # Eksekusi perintah SQL
        cursor.execute(sql_command)
        
        # Dapatkan jumlah baris yang berhasil di-update
        rows_affected = cursor.rowcount
        
        # Commit (simpan permanen) perubahan ke database
        conn.commit()
        
        print("\n-------------------------------------------")
        print("BERHASIL!")
        print(f"{rows_affected} baris di tabel '{TABLE_NAME}' telah di-update.")
        print("-------------------------------------------")

    except sqlite3.Error as e:
        print(f"\nTerjadi error saat mengakses database: {e}")
    except Exception as e:
        print(f"\nTerjadi error tak terduga: {e}")
    finally:
        # Pastikan koneksi selalu ditutup
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == '__main__':
    update_pt_tujuan_column()
