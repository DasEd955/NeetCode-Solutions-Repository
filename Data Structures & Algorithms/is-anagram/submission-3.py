class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenChars1, seenChars2 = dict(), dict()
        for char in s:
            if char in seenChars1:
                seenChars1[char] += 1
            else:
                seenChars1[char] = 1
        for char in t:
            if char in seenChars2:
                seenChars2[char] += 1
            else:
                seenChars2[char] = 1

        if seenChars1 == seenChars2:
            return True
        else:
            return False                                   
                           
        