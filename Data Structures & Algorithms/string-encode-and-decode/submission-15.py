class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedStr = str()

        for string in strs:
            encodedStr += f"{len(string)}#{string}"

        return encodedStr    

    def decode(self, s: str) -> List[str]:

        decodedStrs, i = list(), 0

        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decodedStrs.append(s[j+1:j+1+length])
            i = j + 1 + length

        return decodedStrs    
