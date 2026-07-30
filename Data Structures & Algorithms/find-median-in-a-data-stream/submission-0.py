class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap and num > self.max_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush_max(self.max_heap, num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            popped = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, popped)
        elif len(self.max_heap) + 1 < len(self.min_heap):
            popped = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, popped)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        else:
            return self.min_heap[0]
         