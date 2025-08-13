class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, head=None):
        self.head = head
    
    def Push(self, new_node):
        current = self.head
        if current is None:
            self.head = new_node
        else:
            current = new_node
            new_node.next = self.head
            self.head = current

    def Pop(self):
        current = self.head
        if current is None:
            print("Empty Stack")
        elif current.next is None:
            popped_value = current.value
            self.head = None
        else:
            popped_value = current.value
            current = current.next
            self.head = current

        return print(f"Popped Element: {popped_value}")

    def PrintStack(self):
        current = self.head
        if current is None:
            print("Empty Stack")
        else:
            while current is not None:
                print(f"{current.value}", end=' -> ')
                current = current.next
            print("None")

n1 = Node(2)
n2 = Node(3)
n3 = Node(5)

s1 = Stack()

s1.Push(n1)
s1.Push(n2)
s1.Push(n3)
s1.Pop()
s1.PrintStack()