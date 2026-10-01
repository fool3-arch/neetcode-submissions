class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        count1={}
        if len(s1)>len(s2):
            return False
        for i in s1:
            count1[i]=count1.get(i,0)+1
        count2={}
        for j in range(len(s1)):
            count2[s2[j]]=count2.get(s2[j],0)+1
        if count1==count2:
            return True
        for j in range(len(s1),len(s2)):
            count2[s2[j]]=count2.get(s2[j],0)+1
            count2[s2[left]]-=1
            if count2[s2[left]]==0:
                del count2[s2[left]]
            left+=1
            if count2==count1:
                return True
        return False

        