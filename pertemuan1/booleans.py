#nilai boolean hanya ada 2 yaitu True dan False

print(8<79) #True
print(9==10) #False
print(5>2) #True

a = 666
b = 777

if a < b:
    print("a lebih kecil dari b") #akan mencetak karena kondisi bernilai True
else:
    print("a tidak lebih kecil dari b")

#evaluasi nilai boolean dengan fungsi bool()
print(bool("ayu")) #True karena string tidak kosong
print(bool("")) #False karena string kosong

#hampir semua nilai dianggap True
bool("ayu")
bool(547)
bool([1, 2, 3])

#fungsi bisa mengembalikan boolean
def iniFungsi():
    return True
print(iniFungsi())

#isistance
x = 999999.9
print(isinstance(x, float))