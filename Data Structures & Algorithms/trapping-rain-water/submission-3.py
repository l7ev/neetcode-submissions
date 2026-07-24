class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0

        l,r,v = 0, len(height)-1, 0
        lmax, rmax = height[l], height[r]
        
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                v += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                v += rmax - height[r]
        return v


