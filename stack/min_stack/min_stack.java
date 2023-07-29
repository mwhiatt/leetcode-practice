import java.util.Stack;

class MinStack {
  private Stack<Integer> stack;
  private Stack<Integer> min;

  public MinStack() {
      stack = new Stack<Integer>();
      min = new Stack<Integer>();
  }
  
  public void push(int val) {
      stack.push(val);
      min.push(Math.min(val, min.empty() ? val : min.peek()));
  }
  
  public void pop() {
      stack.pop();
      min.pop();
  }
  
  public int top() {
      return stack.peek();
  }
  
  public int getMin() {
      return min.peek();
  }
}