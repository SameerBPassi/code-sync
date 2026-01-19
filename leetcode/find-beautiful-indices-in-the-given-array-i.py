class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        A, B = [], []

        for i in range(len(s) - len(a) + 1):
            if s[i:i + len(a)] == a:
                A.append(i)
        
        for i in range(len(s) - len(b) + 1):
            if s[i:i + len(b)] == b:
                B.append(i)
                
        res = []
        j = 0
        for i in A:
            while j < len(B) and B[j] < i - k:
                j += 1
            if j < len(B) and abs(B[j] - i) <= k:
                res.append(i)
        return res