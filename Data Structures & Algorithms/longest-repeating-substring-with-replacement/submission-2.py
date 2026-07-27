class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        winfreqs = {}
        msubstring = 0
        for r in range(len(s)):
            if s[r] in winfreqs:
                winfreqs[s[r]] +=1
            else:
                winfreqs[s[r]] = 1
            while (r-l + 1) - max(winfreqs.values()) > k:
                winfreqs[s[l]] -= 1
                l += 1
            msubstring = max(msubstring, r - l + 1)

        return msubstring