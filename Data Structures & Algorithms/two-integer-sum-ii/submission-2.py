class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        left = 0
        right = len(num) - 1

        while left < right:
            total = num[left] + num[right]
            if total == target:
                return[left + 1, right + 1]
            elif total < target:
                left += 1    
            else:
                right -= 1    