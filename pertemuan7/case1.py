plat_arr = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
def pisah(plat_arr):
    ganjil = []
    genap = []
    for i in plat_arr:
        a,b,c = i.split()
        if b%2== 0:
            genap.append(i)
        else:
            ganjil.append(i)
    return ganjil, genap

tuple_ganjil, tuple_genap = pisah(plat_arr)
list_ganjil = list(tuple_ganjil)
list_genap = list(tuple_genap)

print("plat ganjil: ", list_ganjil)
print("plat genap: ", list_genap)
pisah(plat_arr)