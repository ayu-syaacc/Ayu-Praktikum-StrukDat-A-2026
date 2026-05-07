from kurs import kurs
from konverter import konver
from tabulate import tabulate

print("=== KONVERTER MATA UANG ===")

data =[]
for kode, nilai in kurs.items():
    nilai_format = f"{nilai:,}".replace(",", ".")
    data.append([kode, nilai_format])
print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="pretty"))

uang_awal = input("Dari (IDR/USD/EUR/SGD/JPY): ")
uang_tuj = input("Ke (IDR/USD/EUR/SGD/JPY): ")
jumlah = float(input("Jumlah: "))

hasil = konver(uang_awal, uang_tuj, jumlah)

if uang_awal == "IDR":
    print(f"\nRp {jumlah:,.0f} = {hasil:.2f} {uang_tuj}")
elif uang_tuj == "IDR":
    print(f"\n{jumlah:.2f} {uang_awal} = Rp {hasil:,.0f}")
else:
    print(f"\n{jumlah:.2f} {uang_awal} = {hasil:.2f} {uang_tuj}")