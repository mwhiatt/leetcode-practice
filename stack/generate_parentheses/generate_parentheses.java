package stack.generate_parentheses;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    private Stack<Character> stack;
    private ArrayList<String> res;
    private int n;

    public List<String> generateParenthesis(int n) {
        this.n = n;
        stack = new Stack<Character>();
        res = new ArrayList<String>();

        recur(0, 0);
        return res;
    }

    private void recur(int oCount, int cCount) {
        if (oCount == cCount && oCount == n) {
            Stack<Character> copyStack = new Stack<>();
            copyStack.addAll(stack);
            StringBuilder stringBuilder = new StringBuilder();
            while (!copyStack.isEmpty()) stringBuilder.insert(0, copyStack.pop());
            res.add(stringBuilder.toString());
            return;
        }

        if (oCount < n) {
            stack.push('(');
            recur(oCount + 1, cCount);
            stack.pop();
        }

        if (cCount < oCount) {
            stack.push(')');
            recur(oCount, cCount + 1);
            stack.pop();
        }
    }
}