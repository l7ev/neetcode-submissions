class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        counts = {}
        topkfreq = []
        
        for num in nums:
            counts[num] = counts.get(num,0) +1

        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for num, freq in counts.items():
            buckets[freq-1].append(num)

        elements = 0
        i = n -1 
        while i >= 0:
            if buckets[i] == []:
                i -= 1
                continue
            for num in buckets[i]:
                if elements == k:
                    return topkfreq
                topkfreq.append(num)
                elements +=1
            i -= 1    
        
        return topkfreq
