class Solution {
    public boolean checkInclusion(String s1, String s2) {

        if(s1.length() > s2.length()) {
            return false;
        }

        int[] freqS1 = new int[26], freqS2 = new int[26];

        for(int i = 0; i < s1.length(); i++) {
            freqS1[(int)s1.charAt(i) - 'a']++;
            freqS2[(int)s2.charAt(i) - 'a']++;
        }

        int matches = 0;
        for(int i = 0; i < freqS1.length; i++) {
            if(freqS1[i] == freqS2[i]) {
                matches++;
            }
        }

        int left = 0;
        for(int right = s1.length(); right < s2.length(); right++) {
            if(matches == 26) {return true;}
            int index = (int)s2.charAt(right) - 'a';
            freqS2[index]++;
            if(freqS1[index] == freqS2[index]) {
                matches++;
            }
            else if(freqS1[index] + 1 == freqS2[index]) {
                matches--;
            }
            index = (int)s2.charAt(left) - 'a';
            freqS2[index]--;
            if(freqS1[index] == freqS2[index]) {
                matches++;
            }
            else if(freqS1[index] - 1 == freqS2[index]) {
                matches--;
            }
            left++;
        }
        return matches == 26;
    }
}
