from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]
vis = [False for _ in range(n+1)]
indeg,tar = [0],[0]
q = deque()

for i in range(1,m+1):
    data = list(map(int,input().split()))
    indeg.append(data[0])
    tar.append(data[-1])
    for j in range(1,data[0]+1):
        adj[data[j]].append(i)

q.append(1)
while q:
    u = q.popleft()
    
    if vis[u]:continue
    vis[u] = True
    
    for i in adj[u]:
        indeg[i] -= 1
        if not indeg[i]:q.append(tar[i])

print(sum(vis))