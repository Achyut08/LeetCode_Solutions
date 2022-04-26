class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        path = []
        n = len(points)
        for i in range(n-1):
            for j in range(i+1, n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                path.append((dist, i, j))
        res = 0        
        path.sort(key = lambda x:x[0])
        uf = UnionFind(n)
        
        for d, x, y in path:
            if uf.connected(x, y):
                pass
            else:
                res += d
                uf.union(x, y)
        return res