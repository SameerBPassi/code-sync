class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        if k == 0:
            return sum(reward2)
        
        gains = [r1 - r2 for r1, r2 in zip(reward1, reward2)]
        heap = []

        for g in gains:
            if len(heap) < k:
                heapq.heappush(heap, g)
            elif g > heap[0]:
                heapq.heappushpop(heap, g)
        return sum(reward2) + sum(heap)