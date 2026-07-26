class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        winchars = set()
        msubstring = 0
        curr_len = 0
        while r < len(s):
            if s[r] in winchars:
                l += 1
                r = l
                curr_len = 0
                winchars = set()

            else:
                winchars.add(s[r])
                curr_len += 1
                msubstring = max(curr_len, msubstring)
                r += 1
        return msubstring