class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Now we have a min heap
        heap = nums
        heapq.heapify_max(heap)

        for i in range(k - 1):
            heapq.heappop_max(heap)
        
        return heapq.heappop_max(heap)

