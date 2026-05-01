class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        List<String> palindrome = new ArrayList<>();

        dfs(0, s, result, palindrome);
        return result;
    }

    private void dfs(int index, String s, List<List<String>> result, List<String> palindrome) {
        if(index == s.length()) {
            result.add(new ArrayList<>(palindrome));
            return;
        }

        for(int j = index; j < s.length(); j++) {
            if(isPalindrome(s.substring(index, j+1)) == true) {
                palindrome.add(s.substring(index, j+1));
                dfs(j + 1, s, result, palindrome);
                palindrome.removeLast();
            }
        }
    }

    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while(left < right) {
            if(s.charAt(left) != s.charAt(right)) {return false;}
            left++;
            right--;
        }
        return true;
    }
}
