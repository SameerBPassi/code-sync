class Solution:
    def calculate(self, s: str) -> int:
        def helper(i):
            stack = []
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]

                if c.isdigit():
                    num = num * 10 + int(c)

                elif c == '(':
                    num, i = helper(i + 1)

                if c in '+-*/)' or i == len(s) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] *= num
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / num)

                    sign = c
                    num = 0

                    if c == ')':
                        return sum(stack), i  # return from recursion

                i += 1

            return sum(stack), i

        return helper(0)[0]