class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1charfreqs, pperm = {}, {}
        l= 0
        if len(s2) < len(s1): return False
        ## removed redundant loop
        for r in range(len(s1)):
            s1charfreqs[s1[r]] = 1 + s1charfreqs.get(s1[r], 0)
            pperm[s2[r]] = 1 + pperm.get(s2[r], 0)

        while r + 1 < len(s2):
            if pperm == s1charfreqs: ## simpler logic
                return True
            if (pperm[s2[l]] - 1) == 0: ## can use match logic here rather than popping 
                pperm.pop(s2[l])        ## make counts be the # of each letter from 
            else:                       ## the entire alphabet in the string
                pperm[s2[l]] -= 1
            l += 1
            r += 1
            pperm[s2[r]] = 1 + pperm.get(s2[r], 0)

        return pperm == s1charfreqs ## simpler instead of if else