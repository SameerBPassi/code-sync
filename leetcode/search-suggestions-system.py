class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []

        def binary_search(target, start):
            l, r = start, len(products)
            while l < r:
                mid = l + (r - l) // 2
                if products[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        start = 0
        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]
            start = binary_search(prefix, start)
            suggestions = []

            for j in range(start, min(start + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
                else:
                    break
            res.append(suggestions)
        return res