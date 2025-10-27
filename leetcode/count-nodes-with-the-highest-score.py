class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[parents[i]].append(i)
        
        self.max_score = 0
        self.count = 0

        def dfs(node):
            size = 1
            score = 1
            for child in graph[node]:
                sub = dfs(child)
                size += sub
                score *= sub
            remaining = n - size
            if remaining > 0:
                score *= remaining
            if score > self.max_score:
                self.max_score, self.count = score, 1
            elif score == self.max_score:
                self.count += 1
            return size
        dfs(0)
        return self.count