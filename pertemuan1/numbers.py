"""
ada 3 tipe data numerik di python
1. int (integer) = bilangan bulat, contoh: 5, -3, 0
2. float (floating point) = bilangan desimal, contoh: 3.14
3. complex (bilangan kompleks) = bilangan yang memiliki bagian real dan imajiner, contoh: 2 + 3j
kita bisa menggunakan fungsi type() untuk mengetahui tipe data numerik suatu nilai
"""
#contoh
a = 3 #int
b = 8752529866454321 #int
c = -34567 #int
print(type(a))
print(type(b))
print(type(c))

p = 3.14 #float
q = -0.001 #float
r = 22.0 #float
print(type(p))
print(type(q))
print(type(r))

x = 2 + 3j #complex
y = -1j #complex
z = 4 - 5j #complex
print(type(x))
print(type(y))
print(type(z))

#tipe konversi
r = 25 #int
s = 3.14 #float
t = 2 + 3j #complex

a = float(r) #konversi int ke float
b = int(s) #konversi float ke int
c = complex(r) #konversi int ke complex

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random numbers
import random

print(random.randrange(1, 7)) #menghasilkan angka random antara 1 sampai 6
