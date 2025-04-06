import sys
input = sys.stdin.readline

n = int(input())
a = [0] + [int(input()) for _ in range(n)]
vis = [False] * (n+1)
mx = 0

for i in range(1,n+1):
    if vis[i]:continue
    u,d = i,0
    while not vis[u]:
        vis[u] = True
        u= a[u]
        d += 1
    mx = max(mx,d)
    
print(mx)