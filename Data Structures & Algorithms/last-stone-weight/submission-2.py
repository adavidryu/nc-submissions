class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Smash two heaviest stones, x and y
        # If values equal -> both destroyed
        # If x value < y value -> x destroyed, y loses value and reorganized
        # Repeat until one or no stones remain

        h = []

        for stone in stones:
            heapq.heappush(h, -stone)
        
        while len(h) > 1:
            y = -heapq.heappop(h)
            x = -heapq.heappop(h)

            if x < y:
                y = y - x
                heapq.heappush(h, -y)
        
        if h:
            return -h[0]
        
        return 0