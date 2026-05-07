mahasiswa = {
    "M001": {"nama": "Rina", "prodi": "Informatika", "ipk": 3.60},
    "M002": {"nama": "Doni", "prodi": "Sistem Informasi", "ipk": 3.25},
    "M003": {"nama": "Lina", "prodi": "Informatika", "ipk": 3.80}
}
for mahasiswa_ in mahasiswa.values():
    if mahasiswa_["ipk"] >= 3.5 and mahasiswa_["prodi"] == "Informatika":
        print(mahasiswa_["nama"])

rata = sum(mahasiswa_["ipk"] for mahasiswa_ in mahasiswa.values()) / len(mahasiswa)
print("Rata-rata IPK:", rata)


