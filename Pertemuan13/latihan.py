# Soal Latihan Struktur Data - Hash 
# Sistem Penyimpanan Data Buku Perpustakaan

class HashTable: #Kelas untuk mengelola hash table
    def __init__(self):
        self.bucket = [[] for _ in range(10)] #Inisialisasi hash table dengan 10 bucket

    def hash_function(self, key):
        return sum(ord(char) for char in key) % len(self.bucket)

    def insert(self, kode, judul):
        index = self.hash_function(kode)
        for i, (k, _) in enumerate(self.bucket[index]):
            if k == kode:
                self.bucket[index][i] = (kode, judul)  # Update existing book
                return
        self.bucket[index].append((kode, judul))  # Insert new book

    def search(self, kode):
        index = self.hash_function(kode)
        for k, judul in self.bucket[index]:
            if k == kode:
                return judul
        return "Buku tidak ditemukan"

    def delete(self, kode):
        index = self.hash_function(kode)
        for i, (k, _) in enumerate(self.bucket[index]):
            if k == kode:
                del self.bucket[index][i]  # Remove the book
                return

    def display(self):
        for i, bucket in enumerate(self.bucket):
            if bucket:
                print(f"Bucket {i}:")
                for kode, judul in bucket:
                    print(f"  {kode} : {judul}")

# Contoh penggunaan
hash_table = HashTable()

#input
print("Input data:")
hash_table.insert("BK111", "Mahir C++ Dalam Satu Jam")
hash_table.insert("BK222", "Python Dasar")
hash_table.insert("BK333", "Matematika Diskrit")
hash_table.insert("BK444", "Atomic Habits")

#display
hash_table.display()

#insert
print("\nInsert data:")
hash_table.insert("BK045", "Mein Kampf")
hash_table.insert("BK111", "Bumi Manusia")

#display
hash_table.display()

#search
print("\nSearch data:")
print(hash_table.search("BK222"))  # Output: Python Dasar
print(hash_table.search("BK999"))  # Output: Buku tidak ditemukan

#delete
print("\nDelete data:")
hash_table.delete("BK333")

#display
hash_table.display()

