class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])

        res, heap = [], []
        time, i = 0, 0
        n = len(tasks)

        while i < n or heap:
            if not heap:
                time = max(time, tasks[i][0])
            
            while i < n and tasks[i][0] <= time:
                enqueue, proc, idx = tasks[i]
                heapq.heappush(heap, (proc, idx))
                i += 1
            
            proc, idx = heapq.heappop(heap)
            time += proc
            res.append(idx)
        return res