class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+","-","*","/"}:
                # Pop right operand first
                b = stack.pop()
                # Pop left operand second
                a = stack.pop()

                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[-1]
