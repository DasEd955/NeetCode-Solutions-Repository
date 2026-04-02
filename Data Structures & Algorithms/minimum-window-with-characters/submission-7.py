class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t:
            return ""
        if len(s) < len(t):
            return ""
        if s == t:   
            return s

        window, freqT, left = dict(), dict(), 0
        freqMet, minStart = 0, 0
        minLen = float("inf")

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

        return s[minStart:minStart+minLen] if minLen != float("inf") else ""     

                   
    
        