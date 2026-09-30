class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = sorted(set(nums))
        arr = []
        m = 0

        for i in range(len(a)):
            if i == 0 or a[i] == a[i-1] + 1:
                arr.append(a[i])
            else:
                arr = [a[i]]
            m = max(m,len(arr))    

        return m       