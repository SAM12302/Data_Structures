class Node:
    def __init__(self, key, value):
        self.key = key        # e.g., person's name
        self.value = value    # e.g., phone number
        self.next = None      # pointer to next node in the chain

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size   # array of buckets
    
    def _hash(self, key):
        """Generate a hash index for a given key."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            # Chaining: add to the beginning of the linked list
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value  # update if key already exists
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None   # not found

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}:", end=" ")
            current = self.table[i]
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")

phonebook = HashTable(size=5)

phonebook.insert("Alice", "12345")
phonebook.insert("Bob", "67890")
phonebook.insert("Charlie", "54321")
phonebook.insert("David", "98765")
phonebook.insert("Eve", "11111")  # Might collide with others

phonebook.display()

print("Search Bob:", phonebook.search("Bob"))
print("Delete Alice:", phonebook.delete("Alice"))

phonebook.display()

