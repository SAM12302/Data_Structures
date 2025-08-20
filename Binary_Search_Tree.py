class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def Find(self, key, node=None):
        if node is None:
            node = self
        if node is None:
            return None
        if node.value == key:
            return node
        elif key < node.value:
            if node.left is None:
                return node
            else:
                return self.Find(key, node.left)
        else:  # key > node.value
            if node.right is None:
                return node
            else:
                return self.Find(key, node.right)

    def Insert(self, key):
        parent = self.Find(key)

        if parent.value == key:
            # Key already exists
            return False

        if key < parent.value:
            parent.left = Node(key)
        else:
            parent.right = Node(key)
        return True

    def PrintTree(self, node=None):
        if node is None:
            node = self
        # In-order traversal: left, root, right
        if node.left:
            self.PrintTree(node.left)
        print(node.value, end=' ')
        if node.right:
            self.PrintTree(node.right)

    def Next(self, key):
        successor = float('inf')
        while self:
            if self.value > key:
                successor = min(successor, self.value)
                self = self.left
            else:
                self = self.right
        return successor

# Usage
n1 = Node(2)

print(n1.Insert(1))  # True, inserted
print(n1.Insert(3))  # True, inserted
print(n1.Insert(3))  # False, already exists
print(n1.Next(2))
print(n1.Find(5).value)  # Prints the node value where 5 would be inserted (3 in this case)

n1.PrintTree()  # Should print: 1 2 3
