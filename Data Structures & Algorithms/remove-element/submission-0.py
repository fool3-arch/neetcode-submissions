class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        k=len(nums)
        while j>=0 and nums[j]==val:
            j-=1
        
        while i<len(nums) :
            if nums[i] == val and i<j:
                temp = nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                while j>=0 and nums[j]==val:
                    j-=1
            i+=1
        return j + 1