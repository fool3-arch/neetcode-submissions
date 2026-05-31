class Solution:
    def isValid(self, s: str) -> bool:
        stck=[]
        dic={")":"(","]":"[","}":"{",}
        for i in s:
            if i in dic.values():
                stck.append(i)
            else:
                if not stck or stck.pop()!=dic[i]:
                    return False
        return len(stck)==0
