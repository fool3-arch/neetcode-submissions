class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen=len(strs[0])
        minvalue=strs[0]
        for i in strs:
            if minlen >= len(i):
                minlen =len(i)
                minvalue=i
        for i in strs :
            if minvalue=="":
                return minvalue
            for j in range(minlen):
                if i[j] == minvalue[j]:
                    continue
                else:
                    minlen=j
                    minvalue=minvalue[:j]
                    break
        return minvalue