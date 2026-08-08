class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #array is already sorted
        low, high = 0, len(nums) - 1 
        while high >= low:
            middle = (high + low) // 2
            if nums[middle] == target: return middle

            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle  + 1 

        return -1 