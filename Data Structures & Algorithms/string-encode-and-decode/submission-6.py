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
            for _ in range(len(s)-1):
                if s[j]!='#':
                    j+=1
            length=int(s[i:j])
            start=j+1
            end=j+1+length
            output.append(s[start:end])
            i=end
        return output
