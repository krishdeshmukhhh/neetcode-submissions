class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxarea = 0
        

        while l<r:
            currarea = min(heights[l], heights[r])*(r-l)
            maxarea = max(maxarea, currarea)

            if heights[l] <= heights[r]:
                l += 1 

            else:
                r -= 1

        return maxarea
            