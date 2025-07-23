import pyautogui
import time

def ketik_teks_dari_file(nama_file_txt):
    """
    Membaca seluruh teks dari file TXT dan mengetikkannya di aplikasi yang aktif.
    Menambahkan jeda 1 detik antar setiap karakter.
    Pastikan aplikasi target (misal: Word) sudah terbuka dan kursor siap.
    """
    try:
        with open(nama_file_txt, 'r', encoding='utf-8') as f:
            teks_untuk_diketik = f.read()
        print(f"File '{nama_file_txt}' berhasil dibaca. Akan mengetik '{len(teks_untuk_diketik)}' karakter.")
    except FileNotFoundError:
        print(f"ERROR: File '{nama_file_txt}' tidak ditemukan. Pastikan nama file dan lokasinya benar.")
        return
    except Exception as e:
        print(f"ERROR: Terjadi kesalahan saat membaca file: {e}")
        return

    print("\n=======================================================")
    print("      SIAP-SIAP! BOT AKAN MULAI MENGETIK DALAM 5 DETIK!")
    print("   SEGERA KLIK JENDELA MICROSOFT WORD-mu, DAN SIAPKAN KURSOR!")
    print("=======================================================\n")

    time.sleep(5) # Jeda 5 detik

    pyautogui.write(teks_untuk_diketik, interval=0.018)

    print("\nSelesai mengetik! Silakan cek di Microsoft Word-mu.")

# --- CARA PAKAI ---
# 1. Pastikan kamu sudah punya file TXT, misalnya namanya 'text.txt'
#    dengan isi teks yang ingin kamu ketik.
# 2. Pastikan Microsoft Word sudah terbuka dan kursornya berkedip siap nulis.
# 3. Jalankan script ini. Setelah ada pesan 'SIAP-SIAP!', segera klik jendela Word-mu.

# Ganti 'text.txt' dengan nama file TXT-mu yang sebenarnya jika berbeda
ketik_teks_dari_file('text.txt')