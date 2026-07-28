class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> seen = new HashMap<>();

        for(char c : s.toCharArray()) {
            seen.put(c, 1 + seen.getOrDefault(c, 0));
        }

        for(int i = 0; i < s.length(); i++) {
            if(seen.getOrDefault(s.charAt(i), 0) == 1) {return i;}
        }

        return -1;
    }
}