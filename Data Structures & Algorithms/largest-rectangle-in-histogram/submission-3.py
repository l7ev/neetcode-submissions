class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestRect = 0
        stack = [] # [bin height, index]
        index = 0
        for i, h in enumerate(heights):
            index = i            
            while stack and h < stack[-1][0]:
                size = (i - stack[-1][1]) * stack[-1][0]
                largestRect = max(largestRect, size)
                index = stack[-1][1]
                stack.pop() 

            stack.append([h,index])
            ## cleaner one line for checking values still on stack. No need to pop off. 
        for h, i in stack:
            largestRect = max(largestRect, (len(heights) - i) * h) 
        return largestRect