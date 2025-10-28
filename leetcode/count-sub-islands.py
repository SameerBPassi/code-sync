class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid2[r][c] == 0:
                return True
            
            grid2[r][c] = 0

            isSub = grid1[r][c] == 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                isSub = dfs(r + dr, c + dc) and isSub
            
            return isSub
        
        subIslandCount = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        subIslandCount += 1
        return subIslandCount