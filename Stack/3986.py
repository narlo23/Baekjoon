def calc(word):
    stack = list()
    stack.append(word[0])
    for i in range(1, len(word)):
        if len(stack) == 0 or word[i] != stack[-1]:
            stack.append(word[i])
        else:
            stack.pop()
    return len(stack) == 0

n = int(input())
count = 0
for i in range(n):
    word = input()

    if calc(word):
        count += 1

print(count)
