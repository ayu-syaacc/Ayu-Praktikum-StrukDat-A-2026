pengunjung_hari_ini = [ 
    {"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi", "kembali": False}, 
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True}, 
    {"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi", "kembali": False}, 
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True}, 
    {"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains", "kembali": False}, 
    {"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum", "kembali": False}, 
]

def info_perpustakaan(pengunjung_hari_ini):
    perpustakaan = ("Perpustakaan Kampus Terpadu", "Jl. Pendidikan No. 5, Pekanbaru ", "0761-54321")
  
    print('info perpustakaan')
    print('nama    :', perpustakaan[0])
    print('alamat  :', perpustakaan[1])
    print('telp :', perpustakaan[2])

info_perpustakaan(pengunjung_hari_ini)

def rekap_kategori(pengunjung_hari_ini):
    kategori_unik = set([p['kategori'] for p in pengunjung_hari_ini])
    print("\nKategori Buku Unik:", kategori_unik)
    print("Jumlah kategori:", len(kategori_unik))

    rekap = {}
    print("\nRekap per kategori:")
    for p in pengunjung_hari_ini:
      kategori = p['kategori']
        
      if kategori in rekap:
        rekap[kategori] += 1
      else:
        rekap[kategori] = 1

    maximum = max(rekap.values())
    for i,j in rekap.items():
        if j == maximum:
            print(f'{i} : {j} pengunjung')
      
    print(f'kategori terbanyak: ', end='')
    for i,j in rekap.items():
        print(f', {i}', end='')
    print(f' ({maximum} pengunjung)')
    
rekap_kategori(pengunjung_hari_ini)
  