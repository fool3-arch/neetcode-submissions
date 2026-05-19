class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=len(strs[0])
        for i in strs:
            x=min(len(i),x)
        n=strs[0]
        for j in strs[1:]:
            while x>0:
                if n[0:x] == j[0:x]:
                    break
                else:
                    x-=1
            if x==0:
                return ""
        return n[0:x]

        