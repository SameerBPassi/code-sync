class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_size = {}
        id_ = 2 # since grid is made up of 1s and 0s

        def dfs(r, c, id_):
            grid[r][c] = id_
            size = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    size += dfs(nr, nc, id_)
            return size
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_size[id_] = dfs(r, c, id_)
                    id_ += 1
        
        res = max(island_size.values() or [0])

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    s = 1
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                    s += sum(island_size[i] for i in seen)
                    res = max(res, s)
        return res