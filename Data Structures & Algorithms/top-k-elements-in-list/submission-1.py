class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=1+freq.get(i,0)
        bucket=[[] for i in range(len(nums)+1)]
        for f in freq.keys():   
            bucket[freq[f]].append(f)
        res=[]
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res



        