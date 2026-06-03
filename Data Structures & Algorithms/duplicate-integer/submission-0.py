class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Setup empty hashset
        seen = set()

        # Iterate through array
        for num in nums:
            # If current value exists in set, return true
            if num in seen:
                return True
            # If current value doesn't exist in set, add into set
            seen.add(num)
        # If no numbers are duplicates, return false
        return False