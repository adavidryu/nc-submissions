class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26

        for task in tasks:
            counts[ord(task) - ord('A')] += 1

        max_heap = []
        
        for count in counts:
            if count != 0:
                heapq.heappush_max(max_heap, count)
        
        q = deque()
        time = 0

        while q or max_heap:
            time += 1

            if max_heap:
                # Execute most frequent task
                count = heapq.heappop_max(max_heap)
                count -= 1

                # If same tasks type remains -> add to cooldown queue
                if count > 0:
                    q.append((count, time + n))
            
            # If next available queue task is ready, push to heap
            if q and q[0][1] == time:
                count, available_time = q.popleft()
                heapq.heappush_max(max_heap, count)
        
        return time

