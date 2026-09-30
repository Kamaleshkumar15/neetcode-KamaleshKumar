class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            d = [int(x) for x in str(n)]
            arr = []
            for i in d:
                arr.append(i*i)
            n = sum(arr)

        return n == 1