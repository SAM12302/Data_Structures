class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        pass
    def PushBack(self, new_node):
        current = self.head
        if current is not None:
            # Loop over the List
            while current.next is not None:
                current = current.next
            current.next = new_node
        else:
            # Empty list so equal the new node to head node
            self.head = new_node

    def PrintList(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def PushFront(self, new_node):
        current = self.head
        if current is None:
            self.head = new_node
        else:
            current = new_node
            new_node.next = self.head
            self.head = current



l1 = LinkedList()
n1 = Node(2)
n2 = Node(4)
n3 = Node(3)
n4 = Node(10)

l1.PushBack(n1)
l1.PushBack(n2)
l1.PushFront(n3)
l1.PrintList()

