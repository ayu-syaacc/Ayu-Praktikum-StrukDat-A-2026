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

'''
🔥 OKE INI KISI-KISI UTS LU — gue ubah jadi **contekan strategi + template siap pakai**
Fokus: biar kamu **bisa ngerjain walau belum paham penuh**

---

# 🧠 GAMBAR BESAR UTS

Soalnya bakal kayak:
👉 **program lengkap (bukan potongan kecil)**

Alurnya biasanya:

1. input user
2. loop (main program)
3. function dipanggil
4. simpan data (list / matrix)
5. sorting (leaderboard)

---

# ⚡ BAGIAN A — FUNCTION + LOGIKA (WAJIB BANGET)

## 🔥 TEMPLATE WAJIB

```python
def fungsi_saya(x):
    """Fungsi untuk memproses nilai"""
    if x > 0:
        return "Positif"
    else:
        return "Negatif"
```

---

## 🔥 FUNCTION RETURN LIST

```python
def input_data():
    """Mengambil data dari user"""
    data = []
    while True:
        x = input("Masukkan (0 untuk berhenti): ")
        if x == "0":
            break
        data.append(x)
    return data
```

---

## 🔥 FUNCTION PANGGIL FUNCTION

```python
def hitung(a, b):
    """Menjumlahkan"""
    return a + b

def proses():
    """Memanggil fungsi hitung"""
    x = int(input())
    y = int(input())
    return hitung(x, y)
```

---

# ⚡ BAGIAN B — MATRIX 2D

## 🔥 TEMPLATE MATRIX

```python
def input_matrix():
    """Input matrix"""
    baris = int(input("Baris: "))
    kolom = int(input("Kolom: "))

    mat = []

    for i in range(baris):
        row = []
        for j in range(kolom):
            x = int(input(f"[{i}][{j}]: "))
            row.append(x)
        mat.append(row)

    return mat
```

---

## 🔥 TAMPILKAN MATRIX

```python
def tampil_matrix(mat):
    """Menampilkan matrix"""
    if len(mat) == 0:
        print("Data kosong")
        return

    for row in mat:
        for x in row:
            print(x, end=" ")
        print()
```

---

# ⚡ BAGIAN C — SELECTION SORT (WAJIB HAFAL)

## 🔥 TEMPLATE AMAN

```python
def selection_sort(data):
    """Sorting manual"""
    arr = data[:]  # copy biar asli tidak berubah

    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
```

---

## 🔥 LEADERBOARD

```python
def tampil_leaderboard(data):
    """Menampilkan ranking"""
    for i in range(len(data)):
        print(i+1, ".", data[i])
```

---

# ⚡ PROGRAM UTAMA (INI YANG DINILAI BANGET)

## 🔥 TEMPLATE FULL

```python
def main():
    """Program utama"""
    data = []

    while True:
        x = input("Masukkan data (0 untuk keluar): ")
        if x == "0":
            break
        data.append(int(x))

    hasil = selection_sort(data)

    print("Hasil sorting:")
    tampil_leaderboard(hasil)


main()
```

---

# ⚡ HAL WAJIB BIAR NILAI AMAN

## ✅ 1. DOCSTRING (WAJIB ADA)

```python
"""Penjelasan fungsi"""
```

---

## ✅ 2. JANGAN PAKAI

❌ `sort()`
❌ `sorted()`
❌ `random`

---

## ✅ 3. PAKAI INI

* `for`
* `while`
* `if`
* `list`
* `return`

---

# 🔥 POLA YANG HARUS NGENA DI OTAK

Kalau lu blank → ingat ini:

```python
data = []

while True:
    x = input()
    if x == "0":
        break
    data.append(int(x))
```

---

```python
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
```

---

```python
if kondisi:
    return sesuatu
```

---

# 💀 STRATEGI PAS UTS

👉 Jangan mikir terlalu jauh
👉 Copy pola → ubah dikit

---

# ⚡ PRIORITAS BELAJAR (SISA WAKTU LU)

1. Function + return
2. While loop input
3. Selection sort
4. Matrix loop

---

# 🚀 REAL TALK

Lu nggak perlu jago
👉 cukup:

* ngerti pola
* bisa nulis ulang
* jangan kosong

---

Kalau mau last boost:
👉 bilang aja: **“simulasi soal uts”**
gue kasih soal + jawabannya sekalian biar otak lu langsung kebiasa 🔥
🔥 OKE INI KISI-KISI UTS LU — gue ubah jadi **contekan strategi + template siap pakai**
Fokus: biar kamu **bisa ngerjain walau belum paham penuh**

---

# 🧠 GAMBAR BESAR UTS

Soalnya bakal kayak:
👉 **program lengkap (bukan potongan kecil)**

Alurnya biasanya:

1. input user
2. loop (main program)
3. function dipanggil
4. simpan data (list / matrix)
5. sorting (leaderboard)

---

# ⚡ BAGIAN A — FUNCTION + LOGIKA (WAJIB BANGET)

## 🔥 TEMPLATE WAJIB

```python
def fungsi_saya(x):
    """Fungsi untuk memproses nilai"""
    if x > 0:
        return "Positif"
    else:
        return "Negatif"
```

---

## 🔥 FUNCTION RETURN LIST

```python
def input_data():
    """Mengambil data dari user"""
    data = []
    while True:
        x = input("Masukkan (0 untuk berhenti): ")
        if x == "0":
            break
        data.append(x)
    return data
```

---

## 🔥 FUNCTION PANGGIL FUNCTION

```python
def hitung(a, b):
    """Menjumlahkan"""
    return a + b

def proses():
    """Memanggil fungsi hitung"""
    x = int(input())
    y = int(input())
    return hitung(x, y)
```

---

# ⚡ BAGIAN B — MATRIX 2D

## 🔥 TEMPLATE MATRIX

```python
def input_matrix():
    """Input matrix"""
    baris = int(input("Baris: "))
    kolom = int(input("Kolom: "))

    mat = []

    for i in range(baris):
        row = []
        for j in range(kolom):
            x = int(input(f"[{i}][{j}]: "))
            row.append(x)
        mat.append(row)

    return mat
```

---

## 🔥 TAMPILKAN MATRIX

```python
def tampil_matrix(mat):
    """Menampilkan matrix"""
    if len(mat) == 0:
        print("Data kosong")
        return

    for row in mat:
        for x in row:
            print(x, end=" ")
        print()
```

---

# ⚡ BAGIAN C — SELECTION SORT (WAJIB HAFAL)

## 🔥 TEMPLATE AMAN

```python
def selection_sort(data):
    """Sorting manual"""
    arr = data[:]  # copy biar asli tidak berubah

    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
```

---

## 🔥 LEADERBOARD

```python
def tampil_leaderboard(data):
    """Menampilkan ranking"""
    for i in range(len(data)):
        print(i+1, ".", data[i])
```

---

# ⚡ PROGRAM UTAMA (INI YANG DINILAI BANGET)

## 🔥 TEMPLATE FULL

```python
def main():
    """Program utama"""
    data = []

    while True:
        x = input("Masukkan data (0 untuk keluar): ")
        if x == "0":
            break
        data.append(int(x))

    hasil = selection_sort(data)

    print("Hasil sorting:")
    tampil_leaderboard(hasil)


main()
```

---

# ⚡ HAL WAJIB BIAR NILAI AMAN

## ✅ 1. DOCSTRING (WAJIB ADA)

```python
"""Penjelasan fungsi"""
```

---

## ✅ 2. JANGAN PAKAI

❌ `sort()`
❌ `sorted()`
❌ `random`

---

## ✅ 3. PAKAI INI

* `for`
* `while`
* `if`
* `list`
* `return`

---

# 🔥 POLA YANG HARUS NGENA DI OTAK

Kalau lu blank → ingat ini:

```python
data = []

while True:
    x = input()
    if x == "0":
        break
    data.append(int(x))
```

---

```python
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
```

---

```python
if kondisi:
    return sesuatu
```

---

---
'''