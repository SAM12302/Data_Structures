class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def InOrderTraversal(self, node=None):
        if node is None:
            node = self
        if node.left:
            self.InOrderTraversal(node.left)
        print(node.value, end=' ')
        if node.right:
            self.InOrderTraversal(node.right)

    def PreOrderTraversal(self, node=None):
        if node is None:
            node = self
        print(node.value, end=' ')
        if node.left:
            self.PreOrderTraversal(node.left)
        if node.right:
            self.PreOrderTraversal(node.right)

    def PostOrderTraversal(self, node=None):
        if node is None:
            node = self
        if node.left:
            self.PostOrderTraversal(node.left)
        if node.right:
            self.PostOrderTraversal(node.right)
        print(node.value, end=' ')

    def BreadthFirstSearch(self, node=None):
        if node is None:
            node = self

        q = [node]  # queue starts with the root

        while q:
            current = q.pop(0)  # dequeue first element
            print(current.value, end=' ')

            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        print(q)

    def DepthFirstSearch(self, node=None):
        if node is None:
            node = self

        stack = [node]  # start with root on stack

        while stack:
            current = stack.pop()  # take top of stack
            print(current.value, end=' ')

            # push right first, so left is processed first
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)


n1 = Node(2)
n2 = Node(4)
n3 = Node(5)
n4 = Node(7)
n5 = Node(8)
n6 = Node(10)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n6

n1.BreadthFirstSearch()
n1.DepthFirstSearch()
