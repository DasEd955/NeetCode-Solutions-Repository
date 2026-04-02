class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        if s == t:   
            return s

        window, freqT, left = dict(), dict(), 0
        freqMet, minLen, minStart = 0, float("inf"), 0

        for char in t:
            freqT[char] = 1 + freqT.get(char, 0) 

        for right in range(len(s)):

            window[s[right]] = 1 + window.get(s[right], 0)
            if s[right] in freqT and window[s[right]] == freqT[s[right]]:
                freqMet += 1

            while freqMet == len(freqT):
                windowLen = (right - left + 1)
                if windowLen < minLen:
                    minLen = windowLen
                    minStart = left
                window[s[left]] -= 1

                if s[left] in freqT and window[s[left]] < freqT[s[left]]:
                    freqMet -= 1
                left += 1        

        if minLen == float("inf"):
            return ""

        return s[minStart:minStart+minLen]        

                   
    
        