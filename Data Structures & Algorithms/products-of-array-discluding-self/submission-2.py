class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        while i < len(nums):
            builder = 1
            for x in range(len(nums)):
                if x != i:
                    builder *= nums[x]
                else:
                    continue    
            output.append(builder)
            i += 1
        
        return output