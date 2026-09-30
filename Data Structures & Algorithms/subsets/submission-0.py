class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            arr = []

            for subset in result:
                arr.append(subset + [num])

            result = result + arr

        return result
        