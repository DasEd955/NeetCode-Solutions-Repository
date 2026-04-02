public class Solution {

    public String encode(List<String> strs) {

        if(strs.size() == 0) {return "";}

        StringBuilder encodedStr = new StringBuilder();

        for(String string: strs) {
            int length = string.length();
            encodedStr.append(length)
                      .append('#')
                      .append(string);
        }

        return encodedStr.toString();
    }

    public List<String> decode(String s) {

        List<String> decodedStrs = new ArrayList<>();
        int i = 0;

        if(s.length() == 0) {return new ArrayList<String>();}
        
        while(i < s.length()) {
            int j = i;
            while(s.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(s.substring(i, j));
            decodedStrs.add(s.substring(j+1, j+1+length));
            i = j + 1 + length;
        }

        return decodedStrs;
    }
}
