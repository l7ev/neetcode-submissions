class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            for c in s:
                encoded.append(str(ord(c)))
                encoded.append("|")
            encoded.append("*")
        #encoded.append("#")
        answer = "".join(encoded)
        return answer
    def decode(self, s: str) -> List[str]:
        decoded = []
        word = []
        active = []
        for c in s:
            #if c == '#' 
                #return decoded
            if c == '*':
                decoded.append("".join(word))
                word = []
                continue
            if c != '|':
                active.append(c)
                continue
            word.append(chr(int("".join(active)))) 
            active = []
        return decoded