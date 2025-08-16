class DisjointSet:
    def __init__(self):
        self.parent = {}  # maps element -> parent
        self.rank = {}    # helps keep trees flat

    def MakeSet(self, x):
        """Creates a new set with a single element x."""
        if x not in self.parent:
            self.parent[x] = x  # parent of itself
            self.rank[x] = 0    # initial rank

    def Find(self, x):
        """Finds the representative of the set containing x (with path compression)."""
        if self.parent[x] != x:
            # path compression step
            self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    def Union(self, x, y):
        """Unites the sets that contain x and y (union by rank)."""
        root_x = self.Find(x)
        root_y = self.Find(y)

        if root_x == root_y:
            return  # already in the same set

        # attach smaller rank tree under larger rank root
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


# Example usage
ds = DisjointSet()

for i in range(1, 6):
    ds.MakeSet(i)

ds.Union(1, 2)
ds.Union(3, 4)
ds.Union(2, 3)

print(ds.Find(1))  # representative of set containing 1
print(ds.Find(4))  # same as above because {1,2,3,4} are connected
print(ds.Find(5))  # separate set
