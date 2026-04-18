class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = list()
        for task, freq in count.items():
            heapq.heappush(maxHeap, (-freq, task))
            
        time = 0
        cooldown = deque()
        while maxHeap or cooldown:
            time += 1
            if maxHeap:
                freq, task = heapq.heappop(maxHeap)
                freq += 1
                if freq < 0:
                    cooldown.append((time+n, freq, task))
        
            if cooldown and cooldown[0][0] == time:
                _, freq, task = cooldown.popleft()
                heapq.heappush(maxHeap, (freq, task))
        
        return time
        