class Node:
    # Membuat node pasien dengan nama dan keluhan
    def __init__(self, nama, keluhan): # menyimpan nama pasien
        self.nama = nama # menyimpan keluhan pasien
        self.keluhan = keluhan
        self.next = None # pointer untuk node berikutnya
        
#antrian berbasis linked list
class Queue:
    def __init__(self):
        self.head = None #awal antrian
        self.tail = None #akhir antrian
        self._size = 0 #jumlah pasien dalam antrian
        self.no_antrian = 0 #nomor antrian pasien

    #cek apakah antrian kosong
    def is_empty(self):
        return self._size == 0

    #mengembalikan jumlah pasien dalam antrian
    def size(self):
        return self._size

    #menghapus semua pasien dalam antrian
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    #menambahkan pasien baru ke dalam antrian
    def enqueue(self, nama, keluhan):
        node_baru = Node(nama, keluhan)

        #menambah nomor antrian untuk pasien baru
        self.no_antrian += 1

        #jika antrian kosong
        if self.is_empty():
            self.head = node_baru
            self.tail = node_baru
        else:
            #menambahkan pasien baru ke akhir antrian
            self.tail.next = node_baru
            self.tail = node_baru

        self._size += 1 #menambah jumlah pasien dalam antrian

        #mengembalikan nomor antrian pasien yang baru saja didaftarkan
        return self.no_antrian

    #menghapus pasien dari depan antrian
    def dequeue(self):
        if self.is_empty():
            return None
        
        pasien = self.head #pasien paling depan
        self.head = self.head.next #geser head ke pasien berikutnya
       
        self._size -= 1 #kurangi jumlah pasien dalam antrian

        #jika antrian menjadi kosong setelah dequeu
        if self.is_empty():
            self.tail = None
        return pasien
    
    #melihat pasien paling depan tanpa menghapusnya dari antrian
    def peek(self):
        if self.is_empty():
            return None
        return self.head
    
print("\n===================================="
      "\nSISTEM ANTRIAN POLI UMUM"
      "\nRS Sehat Bersama"
      "\n====================================")

#membuat objek antrian 
antrian = Queue()

#cek apakah antrian kosong
print("[CEK] Apakah antrian kosong?", "YA, antrian masih kosong." if antrian.is_empty() else "TIDAK, antrian tidak kosong.")

#menambahkan pasien ke dalam antrian
antrian.enqueue("Budi", "demam tinggi")
print(f"[DAFTAR] Budi terdaftar dengan keluhan: demam tinggi (No. Antrian: {antrian.size()})")

antrian.enqueue("Ani", "batuk pilek")
print(f"[DAFTAR] Ani terdaftar dengan keluhan: batuk pilek (No. Antrian: {antrian.size()})")

antrian.enqueue("Citra", "sakit kepala")
print(f"[DAFTAR] Citra terdaftar dengan keluhan: sakit kepala (No. Antrian: {antrian.size()})")

#menampilkan jumlah pasien dalam antrian
print(f"[INFO] Jumlah pasien menunggu: {antrian.size()} orang")

#melihat pasien paling depan
depan = antrian.peek()

if depan:
    print(f"[PEEK] Pasien berikutnya: {depan.nama} — {depan.keluhan}")

#memanggil pasien dari antrian
panggil = antrian.dequeue()
if panggil:
    print(f"[PANGGIL] Dokter memanggil: {panggil.nama} (keluhan: {panggil.keluhan})")

#menambahkan pasien baru ke dalam antrian
antrian.enqueue("Dodi", "nyeri perut")
print(f"[DAFTAR] Dodi terdaftar dengan keluhan: nyeri perut (No. Antrian: {antrian.size()})")

#menampilkan semua pasien dalam antrian saat ini
print("[ANTRIAN SAAT INI]")

current = antrian.head
while current:
    print(f"- {current.nama} → {current.keluhan}")
    current = current.next

#memanggil pasien berikutnya
panggil = antrian.dequeue()
if panggil:
    print(f"[PANGGIL] Dokter memanggil: {panggil.nama} (keluhan: {panggil.keluhan})")

#menampilkan jumlah pasien yang masih menunggu
print(f"[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")

#mengosongkan antrian 
antrian.clear()
print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

#cek akhir
print("[CEK] Apakah antrian kosong?", "YA, antrian sudah kosong." if antrian.is_empty() else "TIDAK, antrian tidak kosong.")

print("\n===================================="
      "\nSimulasi Selesai!"
      "\n====================================")

