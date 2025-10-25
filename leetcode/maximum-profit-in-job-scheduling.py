class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [s for s, _, _ in jobs]
        cache = {}

        def dfs(i):
            if i == len(jobs):
                return 0
            
            if i in cache:
                return cache[i]
            
            # skip current job
            res = dfs(i + 1)

            # take current job
            _, end, p = jobs[i]
            j = bisect_left(starts, end) # from bisect import bisect_left
            res = max(res, p + dfs(j))

            cache[i] = res
            return res
        return dfs(0)