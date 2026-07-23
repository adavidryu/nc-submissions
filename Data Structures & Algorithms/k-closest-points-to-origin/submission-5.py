class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        res = []

        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush_max(max_heap, [dist, x, y])

            if len(max_heap) > k:
                heapq.heappop_max(max_heap)

        while max_heap:
            dist, x, y = heapq.heappop_max(max_heap)
            res.append([x, y])

        return res