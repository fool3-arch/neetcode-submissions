class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix=[1]*len(nums)
        prefix=[1]*(len(nums))
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            suffix[j]=suffix[j+1]*nums[j+1]
        result=[]
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])
        return result

            

        