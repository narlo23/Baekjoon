n = int(input())
expression = input()
op = ['*', '/', '+', '-']
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
stack = list()

num = dict()
for i in range(n):
    num[alpha[i]] = int(input())

def calc(o):
    global stack
    b = stack.pop()
    a = stack.pop()
    if o == '*':
        return a * b
    elif o == '/':
        return a / b
    elif o == '+':
        return a + b
    else:
        return a - b

for c in expression:
    if c in op:
        stack.append(calc(c))
    else:
        stack.append(num[c])

print("{:.2f}".format(stack[-1]))
