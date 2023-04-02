s = list(input())
explosion_s = list(input())

stack = list()

for i in s:
    stack.append(i)
    if i == explosion_s[-1] and len(stack) >= len(explosion_s):
        if stack[-len(explosion_s):] == explosion_s:
            for j in range(len(explosion_s)):
                 stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))
