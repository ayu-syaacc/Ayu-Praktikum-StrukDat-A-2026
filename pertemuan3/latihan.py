class Person:
    def __init__(self, nama, jenisKelamin, umur):
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.umur = umur

p = Person("ayu", "perempuan", 19)

print(p.nama)

class Karyawan(Person):
    def __init__(self, nama, jenisKelamin, umur, gaji):
        super().__init__(nama, jenisKelamin, umur)
        self.__gaji = gaji

    def get_gaji(self):
        return self.__gaji

    def set_gaji(self, gaji):
        self.__gaji = gaji

k = Karyawan("uya", "lakik", 70, "200 jt")
print(k.get_gaji())

class Rekening(Person):
    def __init__(self, noRek, pin):
        self.noRek = noRek
        self.__pin = pin

    def get_pin(self):
     return self.__pin

    def set_pin(self, pin):
     self.__pin = pin

rek = Rekening("251234", 5555)

print(rek.noRek)
rek.set_pin(9999)
print(rek.get_pin())