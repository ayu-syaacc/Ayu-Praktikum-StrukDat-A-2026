x = 9
y = "jokowi"
print(x)
print(y)

#casting yaitu proses mengubah tipe data ke tipe data lain
a = str(3)    # a jadi '3'
b = int(3)    # b jadi 3
c = float(3)  # c jadi 3.0
print(a, b, c)

#cara mengetahui tipe data dengan fungsi type()
x = 2
y = "mbg prabowo"
print(type(x))
print(type(y))

#nama variabel itu case-sensitive(huruf besar dan kecil dianggap beda)
a = 2
A = "rawr"

#nama variabel
namavariabel = "ayu"
nama_variabel = "ayu"
ini_nama_variabel = "ayu"
namaVariabel = "ayu"
NAMAVARIABEL = "ayu"
namaVariabel2 = "ayu"

#multi words nama variabel
#ada beberapa cara
#Camel Case
iniNamaVariabel = "hello" #setiap awal kata kapital kecuali kata pertama

#Pascal Case
IniNamaVariabel = "hello" #setiap awal kata kapital termasuk kata pertama

#Snake Case
ini_nama_variabel = "hello" #setiap kata dipisah dengan garis bawah _
print(ini_nama_variabel)

#assign beberapa nilai ke variabel
a, b, c = "sate", "bakso", "nasi goreng" #assign nilai-nilai ke beberapa variabel sekaligus dalam satu baris
print(a)
print(b)
print(c)

#assign 1 nilai ke beberapa variabel
f = g = h = "ayam geprek" #assign 1 nilai ke beberapa variabel sekaligus dalam satu baris

#unpack sebuah koleksi
ternak = ["ayam", "sapi", "kambing"] #list
a, b, c = ternak
print(a)
print(b)
print(c)

#output variabel
o = 'makan angin'
print(o)

print("gweh suka " + o) #menggabungkan string dengan variabel

a = 8
b = 4
c = "coklat"
print("hasil dari a + b adalah " + str(a + b)) #menggabungkan string dengan variabel angka harus di-cast dulu ke string
print(a - b) #untuk angka menggunakan operator aritmatika
print(c, a) #menggabungkan string dengan variabel menggunakan koma

#variabel global, yaitu variabel yang dibuat diluar fungsi
e = "hehe" 

def fungsinya():
    print("dia bilang " + e)

fungsinya()


