class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=''
        for s in strs:
            encoded+=str(len(s))+'#'+s
        return encoded
        

    def decode(self, s: str) -> List[str]:
        output=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            start=j+1
            output.append(s[start:start+length])
            i=start+length
        return output
        





