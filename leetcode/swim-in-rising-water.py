class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            t, r, c = heapq.heappop(heap)
            if (r, c) == (n - 1, n - 1):
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))