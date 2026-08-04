class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        winmax = deque()
        res = []
        for i in range(len(nums)):

            while winmax and nums[i] >= nums[winmax[-1]]: #need to make sure that winmax is not empty
                winmax.pop()
            winmax.append(i)
            if winmax[0] < i -k + 1:
                winmax.popleft()
            if i >= k-1:
                res.append(nums[winmax[0]])

        return res
