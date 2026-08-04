class Solution:
    def minWindow(self, s: str, t: str) -> str: 
            if len(s) < len(t) or t == "": return "" 
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






            #   need a curr min len and the string
            #   need two hash maps one that has the freqs that we need another that tracks what 
            #   we have seen so far for # of distict chars 
            #   that number is the matches we need
            #   if we come across a char that is in t and the # seen so far equals the # needed we 
            #   just
            #   increment and continue
            #   but if we come accross a char that is in t and then when we increment it the # seen 
            #   equals the # needed
            #   then we increment the # of matches
            #   once the # of matches equals the # of distict chars in t then we know that the 
            #   substring contains all of the chars in t 
            #   then we can save that string and its length as our res and increment the l pointer
            #   if we come accross a char that is in t then we decrement its count and check if the 
            #   amount we have in the substring is >= needed if so continue if not then we no longer 
            #   have a valid substring and we need to see if it is < our current min substring. if not 
            #   then we skip and continue incrementing the right pointer. if it is then we save it as 
            #   the curr min and continue to increment the right pointer. 