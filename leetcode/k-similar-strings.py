class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        queue = deque([(s1, 0)])
        visited = {s1}

        while queue:
            curr, steps = queue.popleft()
            if curr == s2:
                return steps
            
            i = 0
            while i < len(curr) and curr[i] == s2[i]:
                i += 1
            
            for j in range(i + 1, len(curr)):
                if curr[j] == s2[i] and curr[j] != s2[j]:
                    new_str = list(curr)
                    new_str[i], new_str[j] = new_str[j], new_str[i]
                    new_str = ''.join(new_str)

                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append((new_str, steps + 1))
        return -1