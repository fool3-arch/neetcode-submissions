class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in strs:
            alp=[0]*26
            for j in i :
                alp[ord(j)-ord('a')]+=1
            dic[tuple(alp)].append(i)
        return list(dic.values())