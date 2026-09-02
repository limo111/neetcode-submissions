class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ClosetoOpen={')':'(','}':'{',']':'['}
        for c in s:
            if c in ClosetoOpen:
                if stack and stack[-1]==ClosetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
        