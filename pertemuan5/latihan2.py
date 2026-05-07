#1
stok_barang = [15, 40, 30, 10, 25]

stok_barang[3] = 50
print(stok_barang)

stok_barang.append(5)
stok_barang.sort(reverse=True)

print(stok_barang)

sum(stok_barang)
print("jumlah stok barang: ",sum(stok_barang))

stokAman = sum(stok_barang) / len(stok_barang)
if stokAman >= 20:
    print("Stok Aman")
else:
    print("waspada")

#2
data_aktivitas = (("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70))
for x in data_aktivitas:
    a, b = x
    if b >= 80:
        print(a, "mendapatkan predikat gold")
    elif b >= 80 and b <= 50:
        print(a, "mendapatkan predikat silver")
    else:
        print(a, "mendapatkan predikat bronze")

#3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

coding = ukm_coding.difference(ukm_robotik)
print("yang hanya megikuti ukm coding: ", coding)

duaDua = ukm_coding.symmetric_difference(ukm_robotik)
print("daftar mahasiswa unik: ", duaDua)

print("andi" in ukm_robotik)

#4
gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20}
]
for barang in gudang_pc:
    if barang.get("item") == "Keyboard":
        barang.update({"kategori": "aksesoris"})

gudang_pc.append({"item": "Headset", "harga": 35000, "stok": 8})
print(gudang_pc)

for barang in gudang_pc:
    total = barang["harga"]*barang["stok"]
    print(f"item: {barang["item"]} | Total Aset: Rp{total}")