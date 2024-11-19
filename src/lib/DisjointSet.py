class DisjointSet:
    def __init__(self, n):
        # Initialize the disjoint set with n elements.
        self.parent = list(range(n))
        self.size = [1] * n

    def findParent(self, node):
        # Find the representative (root) of the set to which the node belongs.
        if self.parent[node] == node:
            return node
        # Path compression: Update the parent of the node to the representative.
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    # works
    def unionBySize(self, node1, node2):
        root1 = self.findParent(node1)
        root2 = self.findParent(node2)
        if root1 != root2:
            if self.size[root1] >= self.size[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]
            else:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]
