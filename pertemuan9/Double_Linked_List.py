class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul):
        new_node = Node(judul)


    def print_forward(self):
        current = self.head
        while current:
            print(current.next)
            current = current.next
        print("tida ada")

    def print_backward(self):
        current = self.head
        while current and current.next:
            current = current.next

        while current:
            print(current.judul, current.pengarang)
            current = current.prev

    def delete_by_judul(self, judul):
        current = self.head
        while current: 
            if current.judul == "Bumi Manusia":
                self.head = current.next
                if self.head:
                    self.head.prev = None
            else:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
        return
        current = current.next

# Contoh penggunaan
dll = DoublyLinkedList()
dll.insert_tail("Laskar Pelangi")
dll.insert_tail("Bumi Manusia")
dll.insert_tail("Sang Pemimpi")
print("Forward")
dll.print_forward()
print("\nBackward")
dll.print_backward()
print("\nHapus 'Bumi Manusia'")
dll.delete_by_judul("Bumi Manusia")
print("\nForward setelah hapus")
dll.print_forward()