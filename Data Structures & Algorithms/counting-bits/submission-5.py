class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            binary = bin(i)[2:]
            cnt = binary.count('1')
            arr.append(cnt)
        return arr    
        