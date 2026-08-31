class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water_val=0
        i=0
        j=len(heights)-1
        while i<j:
            width=j-i
            height=min(heights[i],heights[j])
            water_hold=width*height
            if water_hold>max_water_val:
                max_water_val=water_hold
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_water_val


        