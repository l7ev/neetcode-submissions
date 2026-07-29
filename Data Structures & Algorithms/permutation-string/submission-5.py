class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1charfreqs, pperm = {}, {}
        l= 0
        if len(s2) < len(s1): return False

        for c in range(len(s1)):
            s1charfreqs[s1[c]] = 1 + s1charfreqs.get(s1[c], 0)

        for r in range(len(s1)):
            pperm[s2[r]] = 1 + pperm.get(s2[r], 0)

        while r + 1 < len(s2):
            if pperm == s1charfreqs: ## simpler logic
                return True
            if (pperm[s2[l]] - 1) == 0: 
                pperm.pop(s2[l]) 
            else: 
                pperm[s2[l]] -= 1
            l += 1
            r += 1
            pperm[s2[r]] = 1 + pperm.get(s2[r], 0)

        return pperm == s1charfreqs ## simpler instead of if else