class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res=[]
        l=0
        r=l+k
        maxValue=max(nums[l:r])
        res=[]
        res.append(maxValue)
        while l <=len(nums)-k-1:
            pl=l
            l+=1
            r=l+k
            if nums[pl]==maxValue:
                maxValue=max(nums[l:r])
            elif nums[r-1]>maxValue:
                maxValue=nums[r-1]
            res.append(maxValue) 
        return res
