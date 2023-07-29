/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
  if (tokens.length === 1) return parseInt(tokens[0]);
  stack = [];
  tokens.forEach(c => {
      if (c == '+') stack.push(stack.pop() + stack.pop());
      else if (c == '*') stack.push(stack.pop() * stack.pop());
      else if (c == '/') {
          const factor = stack.pop();
          stack.push(Math.trunc(stack.pop() / factor));
      }
      else if (c == '-') {
          const factor = stack.pop();
          stack.push(stack.pop() - factor);
      }
      else stack.push(parseInt(c));
  });
  return stack.pop();
}