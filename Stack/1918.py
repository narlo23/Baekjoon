calc = list(input())
stack = []
result = ''

for c in calc:
    if c.isalpha():
        result += c
    else:
        if c == '(':
            stack.append(c)
        elif c == '*' or c == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(c)
        elif c == '+' or c == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)
