class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for i in strs:
            ans+=str(len(i))+"#"+i
        return ans 

    def decode(self, s: str) -> List[str]:
        i=0
        j=0
        ans=[]
        while i < len(s):
            if s[i]=="#":
                n=int(s[j:i])
                ans.append(s[i+1:i+n+1])
                j=i+n+1
                i=i+n
            i+=1
        return ans 