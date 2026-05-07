pengunjung_hari_ini = [ 
    {"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi", "kembali": False}, 
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True}, 
    {"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi", "kembali": False}, 
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True}, 
    {"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains", "kembali": False}, 
    {"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum", "kembali": False}, 
]

def tampilkan_pengunjung(pengunjung_hari_ini):
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama   | Usia | Kategori | Status Kembali ")
    print("---+------+--------+------+----------+---------------")
    for i in range( len(pengunjung_hari_ini)+1):
        if pengunjung_hari_ini[i]["kembali"]:
            status = "sudah kembali"
        else:
            status = "Belum Kembali"


    print(f'{i}  | {pengunjung_hari_ini[i-1]["id"]} | {pengunjung_hari_ini[i-1]["nama"]}| {pengunjung_hari_ini[i-1]["usia"]} | {pengunjung_hari_ini[i-1]["kategori"]} | {pengunjung_hari_ini[i-1]["kembali"]}')

tampilkan_pengunjung(pengunjung_hari_ini)

def filter_belum_kembali(pengunjung_hari_ini):
    for p in pengunjung_hari_ini:
        if p in pengunjung_hari_ini:
            belum = [p["nama"]]
        else:
            belum = [p["kembali"]]
    belum.sort()
    print("\n===== PENGUNJUNG BELUM KEMBALI =====")
    for i in range(len(belum)):
        print(f'{i+1}. {belum[i]}')
    print('total belum kembali :', len(belum))
    
filter_belum_kembali(pengunjung_hari_ini)