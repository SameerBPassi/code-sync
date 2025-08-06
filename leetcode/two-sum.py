class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[num] = i