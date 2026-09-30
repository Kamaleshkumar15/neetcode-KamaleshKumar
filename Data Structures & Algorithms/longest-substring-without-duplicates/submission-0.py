class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        left = 0
        mx = 0

        for right in range(len(s)):
            while s[right] in result:
                result.remove(s[left])
                left += 1
            result.add(s[right]) 
            mx = max(mx, right - left + 1)   
        return mx