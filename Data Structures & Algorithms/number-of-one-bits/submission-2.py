class Solution:
    def hammingWeight(self, n: int) -> int:
        r = list(bin(n)[2:])
        return(r.count('1'))
        