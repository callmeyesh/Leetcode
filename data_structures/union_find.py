class UF:
    def __init__(self, n):
        if n <= 0:
            raise ValueError('n should be a positive number.')

        self.size = n
        self.connected_components = n
        self.ranks = [0 for _ in range(n)]
        self.parents = [_ for _ in range(n)]

    def find(self, p):
        # Path compressions
        while p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
            p = self.parents[p]
        return p

    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)

        # Both belong to the same set. Cycle detected.
        if parent_p == parent_q:
            return

        # Merge smaller set with larger set
        if self.ranks[parent_p] >= self.ranks[parent_q]:
            self.parents[parent_q] = parent_p
            if self.ranks[parent_p] == self.ranks[parent_q]:
                self.ranks[parent_p] += 1
        else:
            self.parents[parent_p] = parent_q

        # Reduce the number of sets by 1
        self.connected_components -= 1




if __name__ == "__main__":
    uf = UF(3)
    uf.union(0, 1)
    uf.union(1, 2)
    print(uf.connected_components)
