class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        start = 0
        res = 0

        for end in range(len(s)):
            if s[end] in mp:
                start = max(mp[s[end]] + 1, start)
            mp[s[end]] = end
            res = max(res, end - start + 1)
        
        return res
        