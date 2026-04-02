class Solution {
    public int evalRPN(String[] tokens) {

        String[] operators = {"+", "-", "*", "/"};
        Stack<Integer> stack = new Stack<>();

        for(String token : tokens) {
            if(token.equals(operators[0])) {
                stack.push(stack.pop() + stack.pop());
            }
            else if(token.equals(operators[1])) {
                int a = stack.pop(), b = stack.pop();
                stack.push(b - a);
            }
            else if(token.equals(operators[2])) {
                stack.push(stack.pop() * stack.pop());
            }
            else if(token.equals(operators[3])) {
                int a = stack.pop(), b = stack.pop();
                stack.push((int)(b / a));
            }
            else {
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.peek();
    }
}
