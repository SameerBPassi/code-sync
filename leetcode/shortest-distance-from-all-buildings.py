class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        distSum = [[0] * cols for _ in range(rows)]
        reachCount = [[0] * cols for _ in range(rows)]

        totalBuildings = sum(cell == 1 for row in grid for cell in row)

        def bfs(sr, sc):
            visited = [[False] * cols for _ in range(rows)]
            q = deque([(sr, sc, 0)])
            visited[sr][sc] = True

            while q:
                r, c, d = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        distSum[nr][nc] += d + 1
                        reachCount[nr][nc] += 1
                        q.append((nr, nc, d + 1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs(r, c)
        
        res = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and reachCount[r][c] == totalBuildings:
                    res = min(res, distSum[r][c])
        
        return res if res != float('inf') else -1