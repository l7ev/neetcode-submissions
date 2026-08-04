class Solution:
    def minWindow(self, s: str, t: str) -> str: 
            if t == "": return "" 
            seen, tchars = {}, {}
            bestlen, beststart = float('inf'), 0
            l = 0

            for c in t:
                tchars[c] = 1 + tchars.get(c, 0)
            matches = 0

            for r in range(len(s)):
                
                if s[r] in tchars:
                    seen[s[r]] = 1 + seen.get(s[r], 0)
                    
                    if seen[s[r]] == tchars[s[r]]: 
                        matches += 1
                
                while matches == len(tchars):
                    if r-l + 1 < bestlen:
                        bestlen = r-l+1
                        beststart = l
            
                    if s[l] in tchars:
                        seen[s[l]] -= 1
                        
                        if seen[s[l]] < tchars[s[l]]: 
                            matches -= 1   
                    l +=1
            
            return "" if bestlen == float('inf') else s[beststart : beststart + bestlen]
