n = int(input())
h = list(map(int, input().split()))

stack = list()
result = ['0'] * n
for i in range(n):
    while stack:
        if stack[-1][1] > h[i]:
            result[i] = str(stack[-1][0])
            stack.append([str(i+1), h[i]])
            break
        else:
            stack.pop()
    stack.append([i+1, h[i]])


print(" ".join(result))
