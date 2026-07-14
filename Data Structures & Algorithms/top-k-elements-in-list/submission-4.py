class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        counts = {}
        topkfreq = []
        
        for num in nums:
            counts[num] = counts.get(num,0) +1

        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for num, freq in counts.items():
            buckets[freq].append(num)

        elements = 0
        i = n  
        while i >= 0:
            if not buckets[i]:
                i -= 1
                continue
            for num in buckets[i]:
                topkfreq.append(num)
                elements +=1
                if elements == k:
                    return topkfreq
            i -= 1    
        
        return topkfreq
