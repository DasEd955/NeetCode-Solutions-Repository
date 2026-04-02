class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()) {return false;}

        HashMap<Character, Integer> seenChars1 = new HashMap<>();
        HashMap<Character, Integer> seenChars2 = new HashMap<>();

        for(int c = 0; c < s.length(); c++) {
            char ch = s.charAt(c);
            seenChars1.put(ch, seenChars1.getOrDefault(ch, 0) + 1);
        }

        for(int c = 0; c < t.length(); c++) {
            char ch = t.charAt(c);
            seenChars2.put(ch, seenChars2.getOrDefault(ch, 0) + 1);
        } 
        
        return seenChars1.equals(seenChars2);
    }
}
