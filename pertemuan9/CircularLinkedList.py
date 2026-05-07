class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = Node(nama)

antrian = CircularLinkedList()
antrian.insert_tail("Andi")
antrian.insert_tail("Budi")
antrian.insert_tail("Citra")
antrian.insert_tail("Dina")