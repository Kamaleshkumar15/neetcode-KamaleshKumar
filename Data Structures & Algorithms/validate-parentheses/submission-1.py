class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == "[":
                stack.append(ch)
            elif ch == "{":
                stack.append(ch)


            elif ch == ")":
                if not stack:
                    return False
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False

            elif ch == "]":
                if not stack:
                    return False
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False

            elif ch == "}":
                if not stack:
                    return False
                if stack[-1] == "{":
                    stack.pop()
                else:    
                    return False   


        return len(stack) == 0                                         

                