class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2 or len(s) % 2 != 0: return False
        stack = []
        closers = {'}':'{',']':'[',')':'('}
        if s[-1] not in closers or s[0] in closers: return False
        stack.append(s[0])
        for i in range(1,len(s)):
            if s[i] in closers:
                if stack.pop() == closers[s[i]]: continue
                else: return False
            stack.append(s[i])
     
        
        return True if not stack else False