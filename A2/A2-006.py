from collections import deque

n = int(input())
A = [input() for _ in range(n)]
table = [[0]*n for _ in range(n)]

table[n-1][n-1] = 1
q = deque([(n-1,n-1)])
while q:
    i,j = q.popleft()
    if i - 1 >= 0 and A[i-1][j] != 'X' and table[i-1][j] == 0:
        table[i-1][j] = 1
        q.append((i-1,j))
    if j - 1 >= 0 and A[i][j-1] != 'X' and table[i][j-1] == 0:
        table[i][j-1] = 1
        q.append((i,j-1))

print(sum(table[i][j] for j in range(n) for i in range(n) if A[i][j] != 'X'))