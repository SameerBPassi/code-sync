class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX
        self.parent[rootY] = rootX
        self.rank[rootX] += self.rank[rootY]
        return True

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                if diff > 2:
                    return False
            return diff == 2 or diff == 0
            
        n = len(strs)
        uf = UF(n)

        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    uf.union(i, j)
        
        roots = set()
        for i in range(n):
            roots.add(uf.find(i))
        return len(roots)