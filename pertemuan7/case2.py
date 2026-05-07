class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def travertambahKendaraan(head):
    carNode = head
    while carNode:
        print(carNode.data, end=" -> ")
        carNode = carNode.next
    print("null")

def hapusKendaraan(head, nodeToDelete, plat):
  if head == nodeToDelete:
    return head.next
  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head
