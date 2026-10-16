class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append([temperatures[i],i])
                continue
            else:
                while stack and temperatures[i]>stack[-1][0]:
                    removed=stack.pop()
                    res[removed[1]]=i-removed[1]
                stack.append([temperatures[i],i])
        return res