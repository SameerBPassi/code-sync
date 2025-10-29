class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = [], []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        
        cols.sort()

        row_mid = rows[len(rows) // 2]
        col_mid = cols[len(cols) // 2]

        dist = 0
        dist += sum(abs(r - row_mid) for r in rows)
        dist += sum(abs(c - col_mid) for c in cols)
        return dist