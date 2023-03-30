n, k = map(int, input().split())
num = [int(a) for a in input()]

stack = list()
count = 0

for i in range(n):
    while len(stack) > 0 and count < k:
        if stack[-1] < num[i]:
            stack.pop()
            count += 1
        else:
            break
    stack.append(num[i])

stack = stack[:n-k]
print(''.join(map(str, stack)))
