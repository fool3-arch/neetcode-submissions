class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        poki=set(nums)
        longest=0
        for i in poki:
            if (i-1) not in poki:
                length=1
                while i+length in poki:
                    length+=1
                longest=max(length,longest)
        return longest