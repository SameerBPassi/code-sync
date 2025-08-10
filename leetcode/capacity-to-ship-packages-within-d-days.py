class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def shippable(capacity):
            ships, curCap = 1, cap
            for weight in weights:
                if curCap < weight:
                    ships += 1
                    if ships > days:
                        return False
                    curCap = cap
                curCap -= weight
            return True

        while l <= r:
            cap = (l + r) // 2
            if shippable(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res