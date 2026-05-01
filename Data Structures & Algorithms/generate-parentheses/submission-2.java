class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        char[] current = new char[n * 2];
        int openCount = 0, closeCount = 0;

        dfs(openCount, closeCount, 0, result, current, n);
        return result;
    }

    private void dfs(int openCount, int closeCount, int index, List<String> result, char[] current, int n) {
        if(index == n * 2) {
            result.add(new String(current));
            return;
        }

        if(openCount < n) {
            current[index] = '(';
            dfs(openCount+1, closeCount, index+1, result, current, n);
        }

        if(closeCount < openCount) {
            current[index] = ')';
            dfs(openCount, closeCount+1, index+1, result, current, n);
        }
    }
}
