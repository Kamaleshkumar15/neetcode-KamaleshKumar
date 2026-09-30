class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for x in s:
            if x.isalnum():
                new = new + x.lower()
        pre = new
        rev = new[::-1] 

        if pre == rev:
            return True
        else:
            return False         
        