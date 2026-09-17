class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for digit in tokens:
            if digit == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            elif digit == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif digit == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            elif digit == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(digit))
        return stack[0]

        