class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freqS1, freqS2 = [0] * 26, [0] * 26
        
        for i in range(len(s1)):
            freqS1[ord(s1[i]) - ord('a')] += 1
            freqS2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if freqS1[i] == freqS2[i] else 0)

        left = 0
        for right in range(len(s1), len(s2)):

            if matches == 26:
                return True

            index = ord(s2[right]) - ord('a')
            freqS2[index] += 1
            if freqS1[index] == freqS2[index]:
                matches += 1
            elif freqS1[index] + 1 == freqS2[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            freqS2[index] -= 1
            if freqS1[index] == freqS2[index]:
                matches += 1
            elif freqS1[index] - 1 == freqS2[index]:
                matches -= 1    
            
            left += 1

        return matches == 26    