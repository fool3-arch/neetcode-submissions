class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        left=0
        ans=0
        for right in range(len(s)):
            while s[right] in a:
                a.remove(s[left])
                left+=1
            a.add(s[right])
            ans=max(ans,right-left+1)
        return ans 