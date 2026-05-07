#Bagian 1 implementasi menggunakan list biasa

class StackList:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python

    def is_empty(self):
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)
        print("Push:", self.items)

    def pop(self):
        # Tulis kode di sini (Petunjuk: pastikan tidak kosong, lalu gunakan pop)
        if not self.is_empty():
            return self.items.pop()
        return "Riwayat kosong"

    def peek(self):
        # Tulis kode di sini (Petunjuk: kembalikan elemen indeks terakhir [-1])
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        # Tulis kode di sini (Petunjuk: gunakan len())
        return len(self.items)
    
#bagian 2 Implementasi Menggunakan Linked List
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran
    
    def is_empty(self):
        # Tulis kode di sini (Petunjuk: periksa apakah top bernilai None)
        return self.top is None
    
    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
    
    def pop(self):
        if not self.is_empty():
            url = self.top.url
            self.top = self.top.next
            self.count -= 1
        return url
    
    def peek(self):
        if not self.is_empty():
            return self.top.url
    
    def size(self):
        return self.count
    
iniStack = StackLinkedList()
iniStack.push("gugel.kom")
iniStack.push("syopi.com")
iniStack.push("yutub.com")

print("peek: ", iniStack.peek())
print("pop: ", iniStack.pop())
print("is empty: ", iniStack.is_empty())
print("size: ", iniStack.size())