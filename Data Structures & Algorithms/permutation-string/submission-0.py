class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = False
        for i in range(len(s2) - len(s1) + 1):
            if sorted(s2[i:i+len(s1)]) == sorted(s1):
                ans = True
                break

        return(ans)