class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        minVal, maxVal = min(nums), max(nums)
        if minVal == maxVal:
            return 0
        
        n = len(nums)
        bucket_size = math.ceil((maxVal - minVal) / (n - 1))
        bucket_count = (maxVal - minVal) // bucket_size + 1

        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - minVal) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        
        prev_max = minVal
        max_gap = 0

        for b_min, b_max in buckets:
            if b_min == float('inf'):
                continue
            max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max
        return max_gap