class Solution {
    public boolean checkInclusion(String s1, String s2) {

        if(s1.length() > s2.length()) {
            return false;
        }

        int[] freqS1 = new int[26], freqS2 = new int[26];

        for(int i = 0; i < s1.length(); i++) {
            freqS1[(int)s1.charAt(i) - (int)'a'] += 1;
            freqS2[(int)s2.charAt(i) - (int)'a'] += 1;
        }

        int matches = 0;
        for(int i = 0; i < freqS1.length; i++) {
            if(freqS1[i] == freqS2[i]) {matches += 1;}
        }

        int left = 0;
        for(int right = s1.length(); right < s2.length(); right++) {
           
            if(matches == 26) {return true;}

            int indexRight = (int)s2.charAt(right) - (int)'a';
            freqS2[indexRight] += 1;
            if(freqS1[indexRight] == freqS2[indexRight]) {
                matches += 1;
            }
            else if(freqS1[indexRight] + 1 == freqS2[indexRight]) {
                matches -= 1;
            }

            int indexLeft = (int)s2.charAt(left) - (int)'a';
            freqS2[indexLeft] -= 1;
            if(freqS1[indexLeft] == freqS2[indexLeft]) {
                matches += 1;
            }
            else if(freqS1[indexLeft] - 1 == freqS2[indexLeft]) {
                matches -= 1;
            }

            left++;
        }
        return matches == 26;
    }
}
