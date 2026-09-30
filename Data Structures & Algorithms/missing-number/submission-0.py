class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        f = (n * (n +1)) // 2
        t = sum(nums)
        return f - t
        