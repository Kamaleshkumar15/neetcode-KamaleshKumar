class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str,digits)))
        b = num + 1
        d = [int(x) for x in str(b)]
        return d
        