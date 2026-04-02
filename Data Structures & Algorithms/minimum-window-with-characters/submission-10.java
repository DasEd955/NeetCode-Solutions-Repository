class Solution {
    public String minWindow(String s, String t) {

        if(s.length() < t.length() || t.isEmpty()) {
            return "";
        }
        if(s == t) {
            return s;
        }

        HashMap<Character, Integer> window = new HashMap<>();
        HashMap<Character, Integer> freqT = new HashMap<>();
        int left = 0, freqMet = 0, minStart = 0;
        float minLen = Float.POSITIVE_INFINITY;

        for(int i = 0; i < t.length(); i++) {
            freqT.put(t.charAt(i), freqT.getOrDefault(t.charAt(i), 0) + 1);
        }

        for(int right = 0; right < s.length(); right++) {
            window.put(s.charAt(right), window.getOrDefault(s.charAt(right), 0) + 1);
            if(freqT.containsKey(s.charAt(right)) && window.get(s.charAt(right)) == freqT.get(s.charAt(right))) {
                freqMet++;
            }    
            while(freqMet == freqT.size()) {
                int windowLen = right - left + 1;
                if(windowLen < minLen) {
                    minLen = windowLen;
                    minStart = left;
                }
                window.put(s.charAt(left), window.getOrDefault(s.charAt(left), 0) - 1);
                if(freqT.containsKey(s.charAt(left)) && window.get(s.charAt(left)) < freqT.get(s.charAt(left))) {
                    freqMet--;
                }
                left++;
            }
        }
        if(minLen != Float.POSITIVE_INFINITY) {
            return s.substring(minStart, minStart+(int)minLen);
        }
        else {
            return "";
        }
    }
}
