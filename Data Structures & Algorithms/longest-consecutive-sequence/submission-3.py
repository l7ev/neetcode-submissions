class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_len = 1
        highest_seq = 1
        nums.sort()
        if len(nums) < 1:
            return 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] != nums[i-1] +1:
                if seq_len > highest_seq:
                    highest_seq = seq_len
                seq_len = 1
            
            else:
                seq_len += 1
                continue

        if seq_len > highest_seq:
            highest_seq = seq_len
        return highest_seq