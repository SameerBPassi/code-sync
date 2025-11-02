class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)

        speed_heap = []
        speed_sum, max_perf = 0, 0

        for eff, spd in engineers:
            heapq.heappush(speed_heap, spd)
            speed_sum += spd

            if len(speed_heap) > k:
                speed_sum -= heapq.heappop(speed_heap)
            
            max_perf = max(max_perf, speed_sum * eff)
        return max_perf % MOD