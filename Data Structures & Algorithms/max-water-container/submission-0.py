class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r-l
            largest = max(min(heights[l], heights[r]) * width, largest)
            if heights[l] > heights[r]:
                while heights[l] > heights[r] and l < r:              
                    r -= 1
                    width = r - l 
                    largest = max(min(heights[l], heights[r]) * width, largest)
            elif heights[r] > heights[l]:
                while heights[r] > heights[l] and l < r:
                    l += 1
                    width = r - l
                    largest = max(min(heights[l], heights[r]) * width, largest)
            else:
                width = r - l
                largest = max(min(heights[l], heights[r]) * width, largest)
                if heights[r-1] > heights[l-1]:
                    r -= 1
                else:
                    l += 1
            
        return largest