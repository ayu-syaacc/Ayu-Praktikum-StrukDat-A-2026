class Pengunjung:
    hehe = 0

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.hehe =+ 1

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):
        print(f"ID        : {self.__id}")
        print(f"Nama      : {self.__nama}")
        print(f"Kategori  : {self.__kategori}")
    
class PengunjungPrioritas (Pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f'Prioritas : {self.prioritas}')
        if self.prioritas == "Mendesak":
            print('** Layani segera! **')

     
p1 = Pengunjung("M001", "Rina", "Fiksi")
p2 = PengunjungPrioritas("M007", "gilang cuy", "referensi", "Mendesak")


p1.tampilkan_info()
print()

p2.tampilkan_info()
print()