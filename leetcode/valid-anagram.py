class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charS, charT = {}, {}

        for i in range(len(s)):
            charS[s[i]] = 1 + charS.get(s[i], 0)
            charT[t[i]] = 1 + charT.get(t[i], 0)
        
        return charS == charT