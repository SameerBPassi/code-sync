class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # count_s = Counter(s)
        # count_t = Counter(t)
        count_s = [0] * 26
        count_t = [0] * 26
        steps = 0

        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            count_t[ord(t[i]) - ord('a')] += 1

        # for c in count_s:
        for c in range(26):
            if count_s[c] > count_t[c]:
                steps += count_s[c] - count_t[c]
        return steps