class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l,r):
            while l<=r:
                m=(l+r)//2
                if target>nums[m]:
                    l=m+1
                elif target<nums[m]:
                    r=m-1
                else:
                    return m
            return -1
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m

        if target< nums[l]:
            return -1
        r=len(nums)-1
        if nums[l]<=target<=nums[r]:
            return binarySearch(l,len(nums)-1)
        else:
            return binarySearch(0,l-1)
           
            
        