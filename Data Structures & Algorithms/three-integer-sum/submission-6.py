class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        ans=[]
        while i<len(nums) and nums[i]<=0 :
            target = abs(nums[i])
            m=i+1
            n=len(nums)-1
            while m<n:
                if nums[m]+nums[n]==target:
                    ans.append([nums[i],nums[m],nums[n]])
                    while m<n and nums[m+1]==nums[m]:
                        m+=1
                    while m<n and nums[n-1]==nums[n]:
                        n-=1
                    m+=1
                    n-=1
                elif nums[m]+nums[n]>target:
                    n-=1
                elif nums[m]+nums[n]<target:
                    m+=1
            while i<len(nums)-1 and nums[i+1]==nums[i]:
                i+=1
            i+=1
        return ans