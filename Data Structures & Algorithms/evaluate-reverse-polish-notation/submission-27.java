class Solution {
    public int evalRPN(String[] tokens) {

        Stack<Integer> stack = new Stack<>();
        String operators[] = {"+", "-", "*", "/"};

        for(String token : tokens) {
            if(token.equals(operators[0])) {
                stack.push(stack.pop() + stack.pop());
            }
            else if(token.equals(operators[1])) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b - a);
            }
            else if(token.equals(operators[2])) {
                stack.push(stack.pop() * stack.pop());
            }
            else if(token.equals(operators[3])) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b / a);
            }
            else {
                stack.push(Integer.parseInt(token));
            }
        } 
        
        return stack.peek();
    }
}
