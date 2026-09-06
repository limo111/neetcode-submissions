class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=''
        for st in strs:
            encoded+=str(len(st))+'#'+st
        return encoded


    def decode(self, s: str) -> List[str]:
        i=0
        output=[]
        while s and i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            start=j+1
            end=j+1+length
            output.append(s[start:end])
            i=end
        return output

