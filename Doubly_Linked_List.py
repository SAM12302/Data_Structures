class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1)
    def PushFront(self, key):
        new_node = Node(key)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # O(1)
    def TopFront(self):
        return self.head.key if self.head else None

    # O(1)
    def PopFront(self):
        if not self.head:
            return None
        key = self.head.key
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return key

    # O(1) with tail
    def PushBack(self, key):
        new_node = Node(key)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # O(1) with tail
    def TopBack(self):
        return self.tail.key if self.tail else None

    # O(1) with tail
    def PopBack(self):
        if not self.tail:
            return None
        key = self.tail.key
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return key

    # O(n)
    def Find(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    # O(n)
    def Erase(self, key):
        node = self.Find(key)
        if not node:
            return False
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        return True

    # O(1)
    def Empty(self):
        return self.head is None

    # O(1) if node is given
    def AddBefore(self, node, key):
        if not node:
            return
        new_node = Node(key)
        new_node.next = node
        new_node.prev = node.prev
        if node.prev:
            node.prev.next = new_node
        else:
            self.head = new_node
        node.prev = new_node

    # O(1) if node is given
    def AddAfter(self, node, key):
        if not node:
            return
        new_node = Node(key)
        new_node.prev = node
        new_node.next = node.next
        if node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node
        node.next = new_node

    # Helper: print list forward
    def PrintForward(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.key)
            curr = curr.next
        print("Forward:", res)

    # Helper: print list backward
    def PrintBackward(self):
        curr = self.tail
        res = []
        while curr:
            res.append(curr.key)
            curr = curr.prev
        print("Backward:", res)


# Example usage:
dll = DoublyLinkedList()
dll.PushFront(1)
dll.PushBack(2)
dll.PushBack(3)
dll.PrintForward()    # Forward: [1, 2, 3]
dll.PrintBackward()   # Backward: [3, 2, 1]

print("TopFront:", dll.TopFront())  # 1
print("TopBack:", dll.TopBack())    # 3

dll.PopFront()
dll.PrintForward()  # [2, 3]

dll.PopBack()
dll.PrintForward()  # [2]

node = dll.Find(2)
dll.AddBefore(node, 5)
dll.AddAfter(node, 7)
dll.PrintForward()  # [5, 2, 7]
