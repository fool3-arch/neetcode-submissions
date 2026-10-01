class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        count={}
        maxfre=0
        ans=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            maxfre=max(count[s[right]],maxfre)  
            if (right-maxfre-left+1)>k:
                count[s[left]]-=1
                left+=1               
            ans=max(ans,right-left+1)
        return ans