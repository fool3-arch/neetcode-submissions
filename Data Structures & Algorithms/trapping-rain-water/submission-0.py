class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        i=0
        j=len(height)-1
        area=0
        leftmax,rightMax=height[i],height[j]
        while i<j:
            if leftmax<rightMax:
                i+=1
                leftmax=max(leftmax,height[i])
                area+=leftmax-height[i]
            else:
                j-=1
                rightMax=max(rightMax,height[j])
                area+=rightMax-height[j]
        return area 
            