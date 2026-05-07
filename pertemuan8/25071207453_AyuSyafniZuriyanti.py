DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

# === BAGIAN A ===
def tebak_angka(angka_rahasia, maks_percobaan):
    while True:
        maks_percobaan = 7
        x = int(input("Masukkan tebakan: "))
        if x < angka_rahasia:
            print("Terlalu kecil")
        elif x > angka_rahasia:
            print("Terlalu besar")
        elif x == angka_rahasia:
            print("Benar!")
            return True
        elif maks_percobaan == 0:
            print("percobaan habis!")
            return False
        maks_percobaan =-1

''' fungsi yang akan meminta input berupa tebakan dari user dan akan  mengeluarkan petunjuk seperti angka tebakan terlalu besar atau terlalu kecil atau angka tebakan benar. jika maksimal percobaan = 0 atau habis, fungsi akan mencetak percobaan habis'''
            


def hitung_skor(berhasil, sisa_percobaan):
    if berhasil == True:
        skor = sisa_percobaan * 10
        return skor
    else:
        return 0
    

''' fungsi hitung_skor berguna untuk menghitung skor dari pemain dengan cara jika user berhasil menebak angka rahasia dengan benar, maka skor yang didapatkan adalah sisa percobaan dikali 10, jika user tidak berhasil maka fungsi akan mengembalikan nilai 0'''

def main_satu_ronde(nama, nomor_ronde):
    nama = input("masukkan nama: ")
    nomor_ronde = 0
    for i in nomor_ronde:
        if nomor_ronde > 10:
            angka_rahasia = DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]
        else:
            angka_rahasia = DAFTAR_ANGKA[nomor_ronde]
    nomor_ronde =+ 1
    tebak_angka()
    hitung_skor()
        
'''fungsi_main_satu_ronde akan meminta nama user, lalu menghitung ronde yang dimainkan user dengan variabel nomor_ronde bertambah satu setiap kali user bermain. jika ronde yangdimainkan lebih dari 10 maka angka rahasianya diambil dari nomor blonde saat ini dibagi dengan panjang isi daftar angka. lalu fungsi akan memanggil fungsi tebak_angka dan fungsi hitung_skor'''

riwayat = [{a, b, c}]
a = nomor
b = nama
c = skor.append(riwayat)

# === BAGIAN B ===
def tampilkan_riwayat(riwayat):
    riwayat = []
    
    if len(riwayat) == 0:
        print("Belum ada riwayat.")
    else:
        print(riwayat)
'''fungsi yang akan menampilkan riwayat, jika riwayat kosong maka fungsi akan mencetak riwayat belum ada'''

# === BAGIAN C ===
def selection_sort_riwayat(riwayat):
    baris = 0
    for i in baris:
        for j in baris:


'''fungsi mengurutkan riwayat dengan cara selection sort'''

def tampilkan_leaderboard(riwayat):
    selection_sort_riwayat()
    print(riwayat)
'''fungsi untuk menampilkan peringkat pemain berdasarkan skor dari riwayat yang bermain'''

while True:
    main_satu_ronde()
    p = input("apakah ingin bermain lagi?(jika tidak ketik 0)")
    if p == 0:
        break
        

