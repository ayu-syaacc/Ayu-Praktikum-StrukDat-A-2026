#strings
print("ayu syafni zuriyanti") #string dengan kutip 2
print('ayu syafni zuriyanti') #string dengan kutip 1
print("12345") #string angka

#kutip dalam kutip, bisa digunakan selama kutipnya berbeda
print("kamu bilang 'iya'") #kutip 1 dalam kutip 2
print('kamu bilang "tidak"') #kutip 2 dalam kutip 1

#assign string ke variabel
nama = "ayu syafni zuriyanti"
print(nama)

#multiline string
alamat = """pekanbaru
riau
indonesia"""
print(alamat)

#atau
alamat2 = 'pekanbaru\nriau\nindonesia' #\n untuk membuat baris baru
print(alamat2)

#atau
alamat3 = '''pekanbaru #menggunkan 3 tanda kutip tunggal 
riau
indonesia'''
print(alamat3)

#string adalah array
a = "ayu"
print(a[0]) #mengakses karakter pertama
print(a[1]) #mengakses karakter kedua
print(a[2]) #mengakses karakter ketiga

#looping string
for x in "ayu":
    print(x)

#panjang string
a = 'ayu lagi'
print(len(a)) #menghitung panjang string dengan fungsi len()

#cek string
txt = "teknik informatika universitas Riau"
print("informatika" in txt) #mengembalikan nilai True karena ada kata informatika dalam txt

txt2 = "teknik sipil universitas Riau"
if "sipil" in txt2:
    print("ada kata sipil dalam txt2")
else:
    print("tidak ada kata sipil dalam txt2")

#memotong string (slicing)
a = "dunia tidak abadi"
print(a[0:5]) #mengambil karakter dari index 0 sampai 4
print(a[6:13]) #mengambil karakter dari index 6 sampai 12
print(a[:5]) #mengambil karakter dari awal sampai index 4
print(a[6:]) #mengambil karakter dari index 6 sampai akhir
print(a[-6:-1]) #mengambil karakter dari index -6 sampai -2
print(a[-6:]) #mengambil karakter dari index -6 sampai akhir

#ubah string
#upper case
a ="nasi nasgor goreng"
print(a.upper()) #mengubah string menjadi huruf kapital
#lower case
b ="NASI NASGOR GORENG"
print(b.lower()) #mengubah string menjadi huruf kecil
#remove whitespace
c = "   ayam geprek   "
print(c.strip()) #menghapus whitespace di awal dan akhir string
#replace string
print(a.replace("nasgor", "nasi goreng")) #mengganti "nasgor" dengan "nasi goreng"
#split string
d = "matriks, aljabar, kalkulus"
print(d.split(", ")) #memisahkan string berdasarkan koma dan spasi

#gabung string
a = 'ayu'
b = ' syafni'
c = ' zuriyanti'
print(a + b + c) #menggabungkan string

#format string
ipk = 5
txt = "ipk ayu adalah " + str(ipk)
print(txt) 

#F-string
ipk2 = 4.0
txt2 = f"ipk ayu adalah {ipk2}" 
print(txt2)

#placeholder and modifier
jumlah = 1000
txt = f"jumlah mahasiswa: {jumlah} orang"
print(txt)

#escape character
txt = "unri memiliki jurusan \"teknik informatika\" dan \'teknik sipil\'" 
print(txt)
