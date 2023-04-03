n = int(input())
m = int(input())
parents = [i for i in range(n)]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

for i in range(n):
    edge = list(map(int, input().split()))
    for j in range(n):
        if edge[j] == 1:
            union(i, j)

test = list(map(int, input().split()))

result = True
for i in range(1, m):
    if parents[test[i]-1] != parents[test[0] - 1]:
        result = False
        break

if result:
    print('YES')
else:
    print('NO')
