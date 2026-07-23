class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r-l
            largest = max(min(heights[l], heights[r]) * width, largest)
            if heights[l] > heights[r]:             
                r -= 1
            else:
                l += 1     
        return largest