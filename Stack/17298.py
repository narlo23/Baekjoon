n = int(input())
num = list(map(int, input().split()))

stack = list()
result = [-1] * n
for i in range(n-1, -1, -1):
    while stack and stack[-1] <= num[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1]
    stack.append(num[i])

for i in result:
    print(i, end=" ")
