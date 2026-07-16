class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        answer = "".join(encoded)
        return answer
    def decode(self, s: str) -> List[str]:
        decoded = []
        i, j = 0, 0

        while i < len(s):

            while s[j] != '#':
                j+= 1

            length = int(s[i:j]) #string slicing and converting to int 
            i = j + 1
            j = i + length #moving j to the end of word,  
            decoded.append(s[i:j]) #adding word to array
            i = j
                
        return decoded