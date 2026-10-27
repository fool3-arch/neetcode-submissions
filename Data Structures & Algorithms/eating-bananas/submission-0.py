class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r=max(piles)
        l=1
        ans=r
        while l <= r:
            temp=0
            m = (l+r)//2
            for i in piles:
                temp+=math.ceil((i)/m)
            if h>=temp:
                ans=min(m,ans)
                r=m-1
            else:
                l=m+1
        return ans 