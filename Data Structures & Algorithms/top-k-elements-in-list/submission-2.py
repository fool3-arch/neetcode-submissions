class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for i in nums :
            count[i]=count.get(i,0)+1
        freq=[[] for _ in range(len(nums)+1)]
        for i,j in count.items():
            freq[j].append(i)
        ans=[]
        for m in range(len(freq)-1,-1,-1):
            for ele in freq[m]:
                ans.append(ele)
                if len(ans)==k:
                    return ans
