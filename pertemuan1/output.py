#print text
print("informatika") #kutip 2
print('informatika') #kutip 1
print("ini contoh", end= " ")
print("contoh print tanpa garis baru")

#print numbers
print(999)
print(110)

print(9-9) #bisa menghitung dalam print()

#campur text dan numbers
print("tadi sisa kue ada", 2, "potong")

for i in range(3):
    print(f"\nInput Gadget ke-{i+1}")

"""
catatan

1.1 Inisialisasi Variabel

Variabel dibuat langsung tanpa tipe data.

nama = "Yuchee"
umur = 18
tinggi = 170.5

Python adalah loosely typed / dynamically typed
→ tipe data tidak perlu ditentukan.

1.2 Melihat Tipe Data
print(type(nama))
print(type(umur))

Output contoh:

<class 'str'>
<class 'int'>
1.3 Input dan Output
Input
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))

Kenapa int()?
Karena input() selalu menghasilkan string.

Output
print("Halo", nama)

atau

print(f"Halo {nama}")
1.4 Percabangan (If)
umur = 18

if umur >= 17:
    print("Boleh membuat KTP")
else:
    print("Belum boleh")
1.5 Perulangan (Loop)
For Loop
for i in range(5):
    print(i)

Output:

0
1
2
3
4
Loop pada List
buah = ["apel", "jeruk", "mangga"]

for b in buah:
    print(b)
2. FUNGSI DAN PROCEDURE

Di Python fungsi dan procedure sama-sama menggunakan def.

Perbedaannya:

Jenis	Mengembalikan Nilai	Keyword
Procedure	Tidak	tidak pakai return
Function	Ya	pakai return
2.1 Procedure

Procedure hanya menjalankan perintah.

Contoh
def sapa():
    print("Halo dunia")
Memanggil
sapa()

Output:

Halo dunia
Procedure dengan Parameter
def sapa(nama):
    print("Halo", nama)

Memanggil:

sapa("Andi")
2.2 Function

Function mengembalikan nilai menggunakan return

Contoh
def tambah(a, b):
    return a + b

Memanggil:

hasil = tambah(3, 4)
print(hasil)

Output:

7
Function dengan Perhitungan
def luas_persegi(sisi):
    return sisi * sisi

Memanggil

print(luas_persegi(5))
3. TIPE DATA COLLECTION

Collection adalah tipe data yang bisa menyimpan banyak nilai.

Ada 4 utama:

Tipe	Ciri
List	bisa diubah
Tuple	tidak bisa diubah
Set	tidak ada duplikat
Dictionary	key : value
3.1 LIST

List adalah kumpulan data yang berurutan dan bisa diubah.

Inisialisasi
buah = ["apel", "jeruk", "mangga"]
Mengakses
print(buah[0])

Output:

apel
Mengubah
buah[1] = "pisang"
Menambah Data
buah.append("anggur")
Menghapus
buah.remove("apel")

atau

buah.pop()
Panjang List
print(len(buah))
Loop List
for b in buah:
    print(b)
3.2 TUPLE

Tuple adalah collection yang tidak bisa diubah (immutable).

Inisialisasi
angka = (1, 2, 3, 4)
Mengakses
print(angka[1])

Output:

2

Tidak bisa:

angka[0] = 10

Karena tuple immutable.

3.3 SET

Set adalah collection yang:

tidak berurutan

tidak boleh duplikat

Inisialisasi
data = {1,2,3,4}

atau

data = set([1,2,3])
Menambah
data.add(5)
Menghapus
data.remove(2)
Contoh Duplikat
data = {1,1,2,3}
print(data)

Output:

{1,2,3}
3.4 DICTIONARY

Dictionary menyimpan data dalam bentuk:

key : value
Inisialisasi
mahasiswa = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Informatika"
}
Mengakses
print(mahasiswa["nama"])

Output:

Andi
Mengubah
mahasiswa["umur"] = 21
Menambah
mahasiswa["alamat"] = "Pekanbaru"
Loop Dictionary
for key in mahasiswa:
    print(key, mahasiswa[key])
4. COLLECTION DALAM FUNCTION

Contoh function dengan list.

def total(data):
    jumlah = 0
    for d in data:
        jumlah += d
    return jumlah

Pemanggilan:

angka = [1,2,3,4]
print(total(angka))

Output:

10

1. POLA DASAR MENULIS FUNGSI VALIDASI

Soal seperti registrasi gadget biasanya punya pola ini:

1️⃣ terima parameter
2️⃣ cek kondisi (validasi)
3️⃣ jika salah → print error + return None
4️⃣ jika benar → buat dictionary → return

Template yang bisa kamu ingat
def nama_fungsi(parameter):
    
    # validasi
    if kondisi_salah:
        print("Pesan error")
        return None
    
    # jika valid
    data = {
        "key1": nilai1,
        "key2": nilai2
    }
    
    return data
2. VALIDASI STRING DAN ANGKA
Validasi panjang string
if len(sn) < 5:
    print("Serial number minimal 5 karakter")
    return None
Validasi angka
if harga <= 1000000:
    print("Harga harus di atas 1 juta")
    return None
3. MEMBUAT DICTIONARY
Struktur dasar
data = {
    "merk": merk,
    "tipe": tipe,
    "harga": harga,
    "sn": sn,
    "status": "Tersedia"
}
4. LIST OF DICTIONARY (SANGAT SERING DIKUIS)

Contoh:

inventaris = [
    {"merk": "Samsung", "tipe": "S23", "harga": 12000000},
    {"merk": "Oppo", "tipe": "Reno 10", "harga": 6000000}
]
Mengakses data
for g in inventaris:
    print(g["merk"], g["harga"])

g adalah 1 dictionary di dalam list

5. MENAMBAHKAN DATA KE LIST
inventaris = []

data = registrasi_gadget(...)

if data != None:
    inventaris.append(data)
6. LOOP INPUT BEBERAPA DATA

Biasanya dosen suka seperti ini:

inventaris = []

for i in range(3):
    print(f"\nInput Gadget ke-{i+1}")
    
    merk = input("Merk: ")
    tipe = input("Tipe: ")
    harga = float(input("Harga: "))
    sn = input("Serial Number: ")

    data = registrasi_gadget(merk, tipe, harga, sn)

    if data != None:
        inventaris.append(data)
7. FILTER LIST OF DICTIONARY

Ini pola yang sangat sering keluar.

Template filtering
def filter_harga(data, min_harga, max_harga):

    hasil = []

    for g in data:
        if g["harga"] >= min_harga and g["harga"] <= max_harga:
            hasil.append(g)

    return hasil
Memanggil fungsi
min_harga = int(input("Harga minimum: "))
max_harga = int(input("Harga maksimum: "))

hasil = filter_harga(stok_gadget, min_harga, max_harga)
Mengecek jika kosong
if len(hasil) == 0:
    print("Tidak ada gadget dalam rentang harga tersebut")
else:
    for g in hasil:
        print(g)
8. PROCEDURE UPDATE DATA DI LIST

Procedure biasanya mengubah data yang sudah ada.

Template
def update_stok(katalog, sn_target, jumlah_tambah):

    for g in katalog:
        if g["sn"] == sn_target:
            
            if "stok" not in g:
                g["stok"] = 0
            
            g["stok"] += jumlah_tambah
9. CEK KEY DI DICTIONARY

Kadang key belum ada.

if "stok" not in g:
    g["stok"] = 0
10. SET UNTUK DATA UNIK

Set digunakan untuk menghilangkan duplikat.

Inisialisasi
daftar_merk = set()
Menambahkan
daftar_merk.add(g["merk"])
Mengisi dari list
for g in katalog:
    daftar_merk.add(g["merk"])
11. TUPLE DAN TUPLE OF TUPLE

Contoh pada soal komisi:

skema_komisi = (
    (100000000, 10),
    (50000000, 5),
    (20000000, 2),
    (0, 0)
)

Cara akses:

print(skema_komisi[0][0])  # 100000000
print(skema_komisi[0][1])  # 10
12. FUNGSI REKURSI

Rekursi = fungsi memanggil dirinya sendiri.

Template dasar
def fungsi(data, index=0):

    if kondisi_berhenti:
        return nilai
    
    return fungsi(data, index+1)
Pola untuk soal komisi
def hitung_komisi(total_penjualan, skema, index=0):

    target = skema[index][0]
    persen = skema[index][1]

    if total_penjualan >= target:
        return persen
    else:
        return hitung_komisi(total_penjualan, skema, index+1)
13. MENGHITUNG KOMISI
persen = hitung_komisi(total, skema_komisi)

komisi = total * persen / 100
14. MENU PROGRAM (WHILE LOOP)

Ini pola menu interaktif.

Template penting
while True:

    print("1. Tambah Gadget")
    print("2. Inventaris")
    print("3. Update Stok")
    print("4. Cek Komisi")
    print("5. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        pass

    elif pilih == "2":
        pass

    elif pilih == "3":
        pass

    elif pilih == "4":
        pass

    elif pilih == "5":
        print("Terima kasih")
        break
15. MENAMPILKAN DATA DENGAN F-STRING

Contoh tabel sederhana.

for g in inventaris:
    print(f"{g['merk']} | {g['tipe']} | {g['harga']} | {g['sn']}")
16. HAL YANG PALING SERING JADI BUG DI KUIS

Biasanya mahasiswa salah di:

1️⃣ lupa return
return data
2️⃣ salah akses dictionary

SALAH

g.harga

BENAR

g["harga"]
3️⃣ tidak cek None
data = registrasi_gadget(...)

if data != None:
    inventaris.append(data)
4️⃣ salah indentasi

Python sangat sensitif indentasi.

17. POLA BERPIKIR SAAT KUIS

Biasanya soal dosen mengikuti pola:

Soal	Konsep
1	Function + dictionary
2	Filtering list
3	Procedure + set
4	Rekursi + tuple
5	Menu program
18. CHEAT STRUCTURE (INI YANG PALING AMAN)

Kalau kamu lupa saat kuis, pakai struktur ini:

Function
def fungsi(parameter):
    
    if kondisi_error:
        print("Error")
        return None

    data = {}
    return data
Filtering
hasil = []

for item in data:
    if kondisi:
        hasil.append(item)

return hasil
Update data
for item in data:
    if item["key"] == target:
        item["value"] += tambah
Rekursi
def fungsi(data, index=0):

    if kondisi:
        return nilai

    return fungsi(data, index+1)
"""