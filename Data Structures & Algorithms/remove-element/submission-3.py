class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=len(nums)-1
        i=0
        k=0
        while i<=j:
            if nums[i]==val:
                while nums[j]==val and j>i:
                    j-=1
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                j-=1
            else:
                k+=1
                i+=1
        return k