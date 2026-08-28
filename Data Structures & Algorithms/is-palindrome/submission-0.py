class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=''.join(c.lower() for c in s if c.isalnum())
        r,l=0,len(ss)-1
        while r<=l:
            if ss[r]!=ss[l]:
                return False
            r+=1
            l-=1
        return True