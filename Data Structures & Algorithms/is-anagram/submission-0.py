class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}
        for i in s :
            a[i]=a.get(i,0)+1;
        for i in t:
            b[i]=b.get(i,0)+1;
        if a==b:
            return True
        else:
            return False

        