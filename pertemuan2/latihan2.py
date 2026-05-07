#list
nilai = [75, 80, 65, 90, 85]

nilai.append(95)
nilai.sort()
nilai.pop(0)
print("nilai tertinggi: ", nilai[-1])
print("nilai terendah: ", nilai[0])
print("jumlah data:", len(nilai))
print("rata-rata nilai: ", sum(nilai)/len(nilai))
print(nilai)

#Tuple
#1
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print("nama dosen:", dosen[1])
print("Mata kuliah yang diampu:", dosen[2])

#2
for x in dosen:
    print(x)

#3
y = list(dosen)
y[3] = 14

#4. Kelebihan tuple dibandingkan list adalah data di dalam tuple tidak bisa diubah sehingga lebih aman.

#Set
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

print("keahlian yang dimiliki oleh kedua mahasiswa: ", keahlian_A.intersection(keahlian_B))
print("keahlian yang hanya dimiliki mahasiswa A: ", keahlian_A.difference(keahlian_B))
print("keahlian unik dari kedua mahasiswa: ", keahlian_A.symmetric_difference(keahlian_B))

print("apakah \"Java\" termasuk keahlian mahasiswa B: " , "Java" in keahlian_B)

#Dictionary
mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80}
}

