class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in strs:
            lst=[0]*26
            for j in i :
                lst[(ord(j)-ord('a'))]+=1
            dic[tuple(lst)].append(i)

        return list(dic.values())

        