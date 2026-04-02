class Solution {
    public int characterReplacement(String s, int k) {
        
        int longest = 0, left = 0;
        HashMap<Character, Integer> window = new HashMap<>();

        for(int right = 0; right < s.length(); right++) {
            window.put(s.charAt(right), window.getOrDefault(s.charAt(right), 0) + 1);
            while((right - left + 1) - Collections.max(window.values()) > k) {
                window.put(s.charAt(left), window.get(s.charAt(left)) - 1);
                left++;
            }
            longest = Integer.max(longest, right - left + 1);
        }
        return longest;
    }
}
