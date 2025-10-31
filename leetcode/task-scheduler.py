class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        maxHeap = [-cnt for cnt in count if cnt > 0]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap) + 1
                if freq:
                    q.append((time + n, freq))
            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q.popleft()[1])
        return time