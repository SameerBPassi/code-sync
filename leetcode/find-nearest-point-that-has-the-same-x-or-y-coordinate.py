class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        res = -1

        for i, (xi, yi) in enumerate(points):
            if xi == x or yi == y:
                dist = abs(xi - x) + abs(yi - y)
                if dist < min_dist:
                    min_dist = dist
                    res = i
        return res