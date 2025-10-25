class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]
            
            val = matrix[r][c]
            best = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > val:
                    best = max(best, 1 + dfs(nr, nc))
            
            dp[r][c] = best
            return best
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res