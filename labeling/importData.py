import pandas as pd
import sqlite3

# --- KONFIGURASI (Sesuai dengan file Anda) ---
EXCEL_FILE = 'KIRIMAN.xlsx'
SHEET_NAME = 'ALAMAT MASTER'
DB_NAME = 'DbLabeling.db'
TABLE_NAME = 'TujuanKirim'

def import_data_from_excel():
    """Membaca data dari file Excel dan mengimpornya ke database SQLite."""
    try:
        # 1. Baca data dari file Excel menggunakan pandas
        print(f"Membaca file '{EXCEL_FILE}' dari sheet '{SHEET_NAME}'...")
        df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
        print(f"Berhasil membaca {len(df)} baris data.")

        # --- Bagian yang diperbaiki ---
        print("Membersihkan dan men-transformasi data...")

        # 2. Definisikan mapping kolom SEBELUM loop
        column_mapping = {
            'PT': 'pt',
            'PT_TUJUAN': 'pt_tujuan',
            'INSTANSI': 'instansi',
            'TUJUAN': 'tujuan',
            'ALAMAT': 'alamat',
            'PROVINSI': 'provinsi',
            'KONTAK': 'kontak'
        }

        # 3. Lakukan pembersihan data per kolom
        for col_excel in column_mapping.keys():
            if col_excel in df.columns:
                # Cast kolom ke tipe string secara eksplisit untuk mengatasi FutureWarning
                # dan mengubah NaN menjadi string 'nan'
                df[col_excel] = df[col_excel].astype(str)
                
                # Ganti string 'nan' dan string kosong/spasi dengan placeholder '-'
                # .str.strip() untuk menghapus spasi di awal/akhir
                # lalu replace string kosong yang tersisa
                df[col_excel] = df[col_excel].str.strip()
                df[col_excel].replace({'nan': '-', '': '-'}, inplace=True)
            else:
                print(f"Peringatan: Kolom '{col_excel}' tidak ditemukan di Excel.")

        # 4. Ganti nama kolom sesuai mapping
        df.rename(columns=column_mapping, inplace=True)
        
        # 5. Pastikan hanya kolom yang ada di tabel DB yang akan diimpor
        final_columns = [col for col in column_mapping.values() if col in df.columns]
        df_to_import = df[final_columns]

        # 6. Buat koneksi ke database SQLite
        conn = sqlite3.connect(DB_NAME)

        # 7. Gunakan to_sql untuk mengimpor DataFrame ke tabel
        print(f"Mengimpor data ke tabel '{TABLE_NAME}'...")
        df_to_import.to_sql(TABLE_NAME, conn, if_exists='append', index=False)

        print(f"Selesai! Data berhasil diimpor ke database '{DB_NAME}'.")

    except FileNotFoundError:
        print(f"Error: File '{EXCEL_FILE}' tidak ditemukan. Pastikan file ada di folder yang sama.")
    except ValueError as e:
        print(f"Error: Mungkin nama Sheet '{SHEET_NAME}' salah. Error detail: {e}")
    except Exception as e:
        print(f"Terjadi error tak terduga: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == '__main__':
    import_data_from_excel()
