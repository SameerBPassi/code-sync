class Solution:
    def expand(self, s: str) -> List[str]:
        groups = []
        i = 0

        while i < len(s):
            if s[i] == '{':
                j = i
                while s[j] != '}':
                    j += 1
                groups.append(sorted(s[i + 1:j].split(',')))
                i = j + 1
            else:
                groups.append([s[i]])
                i += 1
        
        res = []

        def backtrack(index, path):
            if index == len(groups):
                res.append("".join(path))
                return
            for ch in groups[index]:
                backtrack(index + 1, path + [ch])
        
        backtrack(0, [])
        return res