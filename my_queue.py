# without tail pointer
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class My_Queue():
    def __init__(self, head=None):
        self.head = head

    def Enqueue(self, new_node):
        current = self.head
        if current is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def DeQueue(self):
        current = self.head
        if current is None:
            print("Empty Queue")
        else:
            current = current.next
            self.head = current

    def PrintQueue(self):
        current = self.head
        if current is None:
            print("Empty Queue")
        else:
            while current is not None:
                print(f"{current.value}", end=' <- ')
                current = current.next


n1 = Node(2)
n2 = Node(3)
n3 = Node(5)
n4 = Node(10)

s1 = My_Queue()

s1.Enqueue(n1)
s1.Enqueue(n2)
s1.Enqueue(n3)
s1.DeQueue()
s1.Enqueue(n4)
s1.PrintQueue()

