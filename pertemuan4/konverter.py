from kurs import kurs
def konver(uang_awal, uang_tuj, jumlah):
    if uang_awal == "IDR" and uang_tuj != "IDR":
        hasil = jumlah / kurs[uang_tuj]

    elif uang_awal != "IDR" and uang_tuj == "IDR":
        hasil = jumlah * kurs[uang_awal]

    elif uang_awal != "IDR" and uang_tuj != "IDR":
        hasil = (jumlah * kurs[uang_awal]) / kurs[uang_tuj]

    else:
        hasil = jumlah

    return hasil
        