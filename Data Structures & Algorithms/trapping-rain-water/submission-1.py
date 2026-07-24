class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        l,r,v = 0, n-1, 0
        lmax, rmax = 0, 0

        lmax = max(height[l], lmax)
        rmax = max(height[r], rmax)
        
        for i in range(n-1):
            if lmax > rmax:
                r -= 1
                i = r
            else:
                l += 1
                i = l
            v += max((min(lmax, rmax) -height[i]), 0)

            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)
        return v


