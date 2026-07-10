class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {} #'addend' : 'index'

        for i, num in enumerate(nums):
            #sums[num] = i
            if sums.get(target - num) == None:
                sums[num] = i
                continue 
            else:
                two_sum = [sums.get(target - num), i]
                return two_sum

        return potential

        