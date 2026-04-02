class Solution {
    public String minWindow(String s, String t) {

        HashMap<Character, Integer> window = new HashMap<>();    
        HashMap<Character, Integer> freqT = new HashMap<>();
        int minStart = 0, freqMet = 0;
        int minLen = Integer.MAX_VALUE;

        for(char c : t.toCharArray()) {
            freqT.put(c, 1 + freqT.getOrDefault(c, 0));
        }

        int left = 0;

        for(int right = 0; right < s.length(); right++) {
            window.put(s.charAt(right), window.getOrDefault(s.charAt(right), 0) + 1);
            if(freqT.containsKey(s.charAt(right)) && freqT.get(s.charAt(right)) == window.get(s.charAt(right))) {
                freqMet++;
            }
            while(freqMet == freqT.size()) {
                int windowLen = right - left + 1;
                if(windowLen < minLen) {
                    minLen = windowLen;
                    minStart = left;
                }
                window.put(s.charAt(left), window.get(s.charAt(left)) - 1);
                if(freqT.containsKey(s.charAt(left)) && freqT.get(s.charAt(left)) > window.get(s.charAt(left))) {
                freqMet--;
                }
                left++;
            }
        }
        if(minLen != Integer.MAX_VALUE) {
            return s.substring(minStart, minStart+minLen);
        }
        else {
            return "";
        }
    }
}
