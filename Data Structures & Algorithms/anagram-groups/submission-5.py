class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_grouped = []
        anagrams = []
        found = set()
        for pos, word in enumerate(strs):
            if pos in found:
                continue
            anagrams.append(word)
            for i, pana in enumerate(strs):
                if i != pos and i not in found:
                    if self.isAnagram(word,pana):
                        anagrams.append(pana)
                        found.add(i)
            anagrams_grouped.append(anagrams)
            anagrams = []
        return anagrams_grouped
            
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT