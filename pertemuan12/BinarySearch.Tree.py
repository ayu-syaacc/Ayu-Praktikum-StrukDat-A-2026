# node class untuk menyimpan data buku dan pointer ke anak kiri dan kanan
class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

# class Katalog untuk mengelola operasi pada BST
class Katalog:
    def __init__(self):
        self.root = None

    # metode untuk memasukkan buku baru ke dalam BST
    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)
    
    # Jika tree masih kosong, set new_node sebagai root
        if self.root is None:
            self.root = new_node
            print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}') #menampilkan pesan berhasil memasukkan buku
            return
    
        # Jika tree tidak kosong, cari posisi yang tepat untuk new_node
        current = self.root
        while True: # looping terus sampai menemukan posisi yang tepat atau menemukan duplikat
            if id_buku < current.id_buku: # jika id_buku yang akan dimasukkan lebih kecil dari current.id_buku
                if current.left is None: # jika tidak ada anak kiri
                    current.left = new_node # set new_node sebagai anak kiri
                    print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}') #menampilkan pesan berhasil memasukkan buku
                    return # keluar dari fungsi setelah berhasil memasukkan buku
                current = current.left
        
            elif id_buku > current.id_buku: # jika id_buku yang akan dimasukkan lebih besar dari current.id_buku
                if current.right is None:
                    current.right = new_node
                    print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}') #menampilkan pesan berhasil memasukkan buku
                    return
                current = current.right

            else:
                print(f'[INSERT] Gagal memasukkan: ID {id_buku} sudah ada.')
                return

    def search(self, id_buku):  # metode untuk mencari buku berdasarkan ID
        current = self.root
        while current:
            if id_buku == current.id_buku:
                print(f'[SEARCH] Mencari ID {id_buku}... Ditemukan! Judul: {current.judul}')
                return
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        
        print(f'[SEARCH] Mencari ID {id_buku}... Data tidak ditemukan.')

    def traversal_inorder(self): # metode untuk menampilkan koleksi buku secara urut dari ID terkecil ke terbesar
        print('[INFO] Koleksi Buku (In-Order Traversal):')
        self._traversal_inorder(self.root)

    def _traversal_inorder(self, node): # metode rekursif untuk traversal inorder, menampilkan ID dan judul buku
        if node:
            self._traversal_inorder(node.left)
            print(f'{node.id_buku} - {node.judul}')
            self._traversal_inorder(node.right)

    def get_min(self): # metode untuk menemukan buku dengan ID terkecil
        current = self.root
        while current and current.left:
            current = current.left
        return current

    def get_max(self): # metode untuk menemukan buku dengan ID terbesar
        current = self.root
        while current and current.right:
            current = current.right
        return current

    def height(self): # metode untuk menghitung tinggi tree
        return self._height(self.root)

    def _height(self, node): # metode rekursif untuk menghitung tinggi tree, mengembalikan -1 jika node kosong
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height, right_height)

if __name__ == "__main__":
    print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
    print("=========================================")
  
    katalog = Katalog()
    # Menambahkan buku-buku ke dalam katalog
    katalog.insert(50, "Dasar Pemrograman")
    katalog.insert(30, "Struktur Data")
    katalog.insert(70, "Kecerdasan Buatan")
    katalog.insert(20, "Matematika Diskrit")
    katalog.insert(40, "Basis Data")
    katalog.insert(60, "Jaringan Komputer")
    katalog.insert(80, "Sistem Operasi")

    katalog.traversal_inorder()
    print()

    katalog.search(60)
    katalog.search(100)
    print()

    min_node = katalog.get_min()
    max_node = katalog.get_max()
    
    print()
    print(f'[STATISTIK] ID Terkecil: {min_node.id_buku}')
    print(f'[STATISTIK] ID Terbesar: {max_node.id_buku}')
    print(f'[INFO] Tinggi (Height) Tree: {katalog.height()}')
    print("=========================================")
    print("Simulasi Selesai!")
