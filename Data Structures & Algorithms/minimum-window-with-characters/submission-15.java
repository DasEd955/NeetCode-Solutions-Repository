class Solution {
    public String minWindow(String s, String t) {

        HashMap<Character, Integer> window = new HashMap<>(),
                                    freqT = new HashMap<>();
        int minStart = 0, freqMet = 0;
        int minLen = Integer.MAX_VALUE;

        for(char c : t.toCharArray()) {
            freqT.put(c, freqT.getOrDefault(c, 0) + 1);
        }

        int left = 0;
        for(int right = 0; right < s.length(); right++) {
            char rightChar = s.charAt(right);
            window.put(rightChar, window.getOrDefault(rightChar, 0) + 1);
            if(freqT.containsKey(rightChar) && freqT.get(rightChar) == window.get(rightChar)) {
                freqMet++;
            }
            while(freqMet == freqT.size()) {
                int windowLen = right - left + 1;
                if(windowLen < minLen) {
                    minLen = windowLen;
                    minStart = left;
                }
                char leftChar = s.charAt(left);
                window.put(leftChar, window.get(leftChar) - 1);
                if(freqT.containsKey(leftChar) && freqT.get(leftChar) > window.get(leftChar)) {
                    freqMet--;
                }
                left++;
            }
        }
        if(minLen != Integer.MAX_VALUE) {
            return s.substring(minStart, minStart + minLen);
        }
        else {
            return "";
        }
    }
}
