class Solution:
    def merge(self,nums,mid,left,right):
        n1=mid-left+1
        n2=right-mid
        l=[0]*n1
        r=[0]*n2
        for i in range(n1):
            l[i]=nums[left+i]
        for j in range(n2):
            r[j]=nums[mid+j+1]
        i=0
        j=0
        k=left
        while i<n1 and j<n2:
            if l[i]<r[j]:
                nums[k]=l[i]
                i+=1
            else:
                nums[k]=r[j]
                j+=1
            k+=1
        while i<n1:
            nums[k]=l[i]
            i+=1
            k+=1
        while j<n2:
            nums[k]=r[j]
            j+=1
            k+=1
        
    def mergesort(self,nums,left,right):
        if left<right:
            mid=(left+right)//2
            self.mergesort(nums,left,mid)
            self.mergesort(nums,mid+1,right)
            self.merge(nums,mid,left,right)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums,0,len(nums)-1)
        return nums